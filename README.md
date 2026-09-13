# PyMake

A simple terminal tool for creating a Python virtual environment and basic project files.

## Requirements

You need:

- Python 3

### Arch / Omarchy

```bash
sudo pacman -S python
```

## How to use

Download or clone this repository, then open a terminal in the project folder.

To run the tool directly:

```bash
python3 PyMake.py
```

The tool creates:

```text
.venv/
requirements.txt
main.py
```

The virtual environment is automatically activated when the tool finishes.

## Using `pymake` as a terminal command

If you want to start the program by simply typing:

```bash
pymake
```

Run the installer from inside the project folder:

```bash
./install.sh
```

This will:

- make `PyMake.py` executable
- create `~/.local/bin` if needed
- link it as `pymake` in `~/.local/bin` (replacing any previous link)
- warn you if `~/.local/bin` isn't on your `PATH` yet

If it warns about your `PATH`, add this line to your `~/.bashrc` or `~/.zshrc`, then open a new terminal:

```bash
export PATH="$HOME/.local/bin:$PATH"
```

Then you can run it from any terminal:

```bash
cd my-python-project
pymake
```

It will create:

```text
my-python-project/
├── .venv/
├── requirements.txt
└── main.py
```

The virtual environment will be automatically activated when `pymake` finishes.

## Removing it

If you only downloaded the project, just delete its folder.

If you also installed the terminal command, run the uninstaller from inside the project folder:

```bash
./uninstall.sh
```

Then you can delete the project folder if you want.

Removing `pymake` does not delete any `.venv`, `requirements.txt`, or `main.py` files created in your project folders.