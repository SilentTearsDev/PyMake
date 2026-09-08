#!/usr/bin/env python3

import os
import subprocess
import sys
from pathlib import Path


def main():
    project_dir = Path.cwd()
    venv_dir = project_dir / ".venv"
    requirements_file = project_dir / "requirements.txt"
    main_file = project_dir / "main.py"

    print(f"Creating virtual environment in: {venv_dir}")

    if not venv_dir.exists():
        subprocess.run(
            [sys.executable, "-m", "venv", str(venv_dir)],
            check=True
        )
        print("✓ Virtual environment created")
    else:
        print("✓ Virtual environment already exists")

    if not requirements_file.exists():
        requirements_file.touch()
        print("✓ requirements.txt created")
    else:
        print("✓ requirements.txt already exists")

    if not main_file.exists():
        main_file.touch()
        print("✓ main.py created")
    else:
        print("✓ main.py already exists")

    print()
    print("Project ready!")
    print()

    # A Python process cannot activate its parent shell directly.
    # Start a new Bash shell with the venv activated.
    activate = venv_dir / "bin" / "activate"

    os.execv(
        "/bin/bash",
        ["/bin/bash", "--rcfile", str(activate)]
    )


if __name__ == "__main__":
    main()
