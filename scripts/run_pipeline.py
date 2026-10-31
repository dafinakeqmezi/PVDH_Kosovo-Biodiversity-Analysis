"""Execute Part I in a disposable local clone using this Python environment.

The source checkout and its data are never modified. The temporary clone and
executed notebooks remain available for inspection at the printed path.
"""
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import time

import nbformat
from nbclient import NotebookClient
from jupyter_client import KernelManager
from jupyter_client.kernelspec import KernelSpecManager


ROOT = Path(__file__).resolve().parents[1]


def main():
    folder = Path(tempfile.mkdtemp(prefix="pvdh-pipeline-"))
    workspace = folder / "repo"
    print(f"Workspace: {workspace}", flush=True)
    subprocess.run(["git", "clone", "--quiet", "--no-hardlinks", str(ROOT), str(workspace)], check=True)
    for name in ("notebooks", "scripts", "tests"):
        shutil.copytree(ROOT / name, workspace / name, dirs_exist_ok=True,
                        ignore=shutil.ignore_patterns("__pycache__", ".ipynb_checkpoints"))
    shutil.copy2(ROOT / "requirements.txt", workspace / "requirements.txt")
    source_hashes = {p: hashlib.sha256(p.read_bytes()).hexdigest()
                     for name in ("dataset", "processed") for p in (ROOT / name).glob("*") if p.is_file()}
    # Retain external API metadata and the frozen checkpoint as comparison inputs.
    retained = {"gbif_datasets_cache.csv", "biodiversity_clean.csv",
                "biodiversity_clean_schema.json", "biodiversity_clean_manifest.json"}
    for path in (workspace / "processed").iterdir():
        if path.is_file() and path.name not in retained:
            path.unlink()

    kernel_dir = folder / "kernels" / "pvdh"
    kernel_dir.mkdir(parents=True)
    (kernel_dir / "kernel.json").write_text(json.dumps({
        "argv": [sys.executable, "-m", "ipykernel_launcher", "-f", "{connection_file}"],
        "display_name": "PVDH isolated environment", "language": "python",
    }))
    kernels = KernelSpecManager(kernel_dirs=[str(kernel_dir.parent)])
    stages = [
        ("01b_analiza_burimeve.ipynb", False),
        ("01_mbledhja_kualiteti.ipynb", True),
        ("02_pastrimi.ipynb", False),
        ("01_mbledhja_kualiteti.ipynb", False),
        ("03_vetite.ipynb", False),
    ]
    results = []
    try:
        for filename, bootstrap in stages:
            notebook = nbformat.read(workspace / "notebooks" / filename, as_version=4)
            if bootstrap:
                stop = next(i for i, c in enumerate(notebook.cells)
                            if c.cell_type == "code" and 'section("8. RIKALKULIMI' in c.source)
                notebook.cells = notebook.cells[:stop]
            label = filename + (" (bootstrap before clean aggregates)" if bootstrap else "")
            print(f"RUN {label}", flush=True)
            started = time.monotonic()
            manager = KernelManager(kernel_name="pvdh", kernel_spec_manager=kernels)
            client = NotebookClient(notebook, km=manager, timeout=1200,
                                    resources={"metadata": {"path": str(workspace)}})
            try:
                client.execute()
            finally:
                if manager.has_kernel:
                    manager.shutdown_kernel(now=True)
                output = folder / ("bootstrap.ipynb" if bootstrap else filename)
                nbformat.write(notebook, output)
            results.append({"stage": label, "status": "PASS", "seconds": round(time.monotonic() - started, 2)})
            print(f"PASS {label}", flush=True)
        for command in ([sys.executable, "scripts/verify_processed.py"],
                        [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"]):
            completed = subprocess.run(command, cwd=workspace, text=True, capture_output=True)
            print(completed.stdout, flush=True)
            print(completed.stderr, flush=True)
            (folder / ("audit.txt" if "verify_processed.py" in command[1] else "tests.txt")).write_text(
                completed.stdout + completed.stderr)
            completed.check_returncode()
        results.append({"stage": "saved-output audit and tests", "status": "PASS"})
    except Exception as error:
        results.append({"stage": "pipeline", "status": "FAIL", "detail": str(error)})
        raise
    finally:
        assert all(hashlib.sha256(p.read_bytes()).hexdigest() == h for p, h in source_hashes.items())
        (folder / "execution.json").write_text(json.dumps({
            "python": sys.version, "executable": sys.executable, "workspace": str(workspace),
            "source_data_unchanged": True, "stages": results,
        }, indent=2))
        print(f"Execution record: {folder / 'execution.json'}", flush=True)


if __name__ == "__main__":
    main()
