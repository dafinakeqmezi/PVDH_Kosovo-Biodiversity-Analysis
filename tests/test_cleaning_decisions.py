"""Test notebook helpers without executing its data export cells."""
import ast
import json
from pathlib import Path
import unittest

import numpy as np
import pandas as pd


NOTEBOOK = Path(__file__).resolve().parents[1] / "notebooks/02_pastrimi.ipynb"


def notebook_helpers(cell_id):
    notebook = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
    cell = next(c for c in notebook["cells"] if c.get("id") == cell_id)
    tree = ast.parse("".join(cell["source"]))
    tree.body = [node for node in tree.body if isinstance(node, ast.FunctionDef)]
    namespace = {"pd": pd, "np": np}
    exec(compile(tree, str(NOTEBOOK), "exec"), namespace)
    return namespace


class InvalidValuesTests(unittest.TestCase):
    def setUp(self):
        self.helpers = notebook_helpers("invalid-values")

    def test_threshold_uses_distribution_and_area(self):
        policy = self.helpers["uncertainty_policy"]
        threshold, radius = policy(pd.Series([10, 20, 30, np.nan, 0, -1, np.inf]), pd.Series([np.pi]))
        self.assertEqual(threshold, 20)
        self.assertAlmostEqual(radius, 1000)
        threshold, _ = policy(pd.Series([2000, 4000, 6000]), pd.Series([np.pi, np.nan]))
        self.assertAlmostEqual(threshold, 1000)
        with self.assertRaises(ValueError):
            policy(pd.Series([np.nan, 0]), pd.Series([1]))

    def test_uncertainty_boundaries_and_missing(self):
        values = pd.Series([np.nan, 0, -1, np.inf, -np.inf, 50, 100, 101])
        result = self.helpers["uncertainty_status"](values, 100)
        self.assertEqual(result.tolist(), ["unknown", "invalid", "invalid", "invalid", "invalid",
                                           "within_screening_threshold", "within_screening_threshold", "above_screening_threshold"])

    def test_species_and_finer_are_not_higher_ranks(self):
        ranks = pd.Series(["SPECIES", "SUBSPECIES", "VARIETY", "FORM", "GENUS", "FAMILY", "UNRANKED", None, "SPECIES", "UNKNOWN"])
        names = pd.Series(["a"] * 8 + [None, "a"])
        result = self.helpers["species_level_flag"](ranks, names)
        expected = pd.Series([True, True, True, True, False, False, pd.NA, pd.NA, pd.NA, pd.NA], dtype="boolean")
        pd.testing.assert_series_equal(result, expected)


if __name__ == "__main__":
    unittest.main()
