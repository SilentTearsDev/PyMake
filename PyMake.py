#!/usr/bin/env python3

import os
import subprocess
import sys
from pathlib import Path


def install_requirements(project_dir, venv_dir, requirements_file):
    if not venv_dir.exists():
        print("✗ Virtual environment does not exist.")
        print("Run 'pymake' first.")
        return

    if not requirements_file.exists():
        print("✗ requirements.txt does not exist.")
        return

    print("Installing requirements into the virtual environment...")
    print()

    pip = venv_dir / "bin" / "pip"

    subprocess.run(
        [str(pip), "install", "-r", str(requirements_file)],
        check=True
    )

    print()
    print("✓ Requirements installed successfully")


def create_project(project_dir):
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

    activate = venv_dir / "bin" / "activate"

    os.execv(
        "/bin/bash",
        ["/bin/bash", "--rcfile", str(activate)]
    )


def main():
    project_dir = Path.cwd()

    if len(sys.argv) > 1:
        command = sys.argv[1].lower()

        if command == "-install":
            venv_dir = project_dir / ".venv"
            requirements_file = project_dir / "requirements.txt"

            install_requirements(
                project_dir,
                venv_dir,
                requirements_file
            )
            return

    create_project(project_dir)


if __name__ == "__main__":
    main()

