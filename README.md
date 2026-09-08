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

Run this from inside the project folder:

```bash
mkdir -p ~/.local/bin
ln -s "$(pwd)/pymake" ~/.local/bin/pymake
```

Before using the command, edit `pymake` and replace:

```text
/PATH/TO/PyMake/PyMake.py
```

with the real path to `PyMake.py`.

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

## Removing it

If you only downloaded the project, just delete its folder.

If you also installed the terminal command:

```bash
rm ~/.local/bin/pymake
```

Then you can delete the project folder if you want.
