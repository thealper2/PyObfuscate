# PyObfuscate

**PyObfuscate** is a Python code obfuscation tool designed to make your Python source code harder to reverse-engineer. It renames variables, functions, and classes to random names, and optionally removes docstrings and compacts the code into fewer lines. This tool is ideal for protecting intellectual property or making your codebase less readable to unauthorized users.

1. [Features]()
2. [Installation]()
3. [Usage]()
4. [Contributing]()
5. [License]()

--- 

## :dart: Features

- **Variable, Function, and Class Obfuscation**: Renames identifiers to random names.
- **Protected Names**: Preserves Python keywords, built-in functions, and other protected names.
- **Docstring Removal**: Optionally removes docstrings from the code.
- **Code Compaction**: Compacts the code into fewer lines for additional obfuscation.
- **Customizable Random Names**: Generates random names of specified length and type (alphabetic or numeric).
- **Seed Support**: Ensures reproducible obfuscation using a random seed.

## :hammer_and_wrench: Installation

You can install pyobfuscate using pip:

```bash
pip install pyobfuscate
```

Alternatively, you can clone the repository and install it locally:

```bash
git clone https://github.com/thelper2/PyObfuscate.git
cd pyobfuscate
pip install .
```

## :joystick: Usage

### Command-Line Interface

The easiest way to use pyobfuscate is through the command-line interface (CLI). Here’s how:

```bash
pyobfuscate input_file.py [-o output_file.py] [--remove-docstrings] [--compact] [--seed SEED] [-n NAME_LENGTH] [--type {alpha,numeric}]
```

### Options

1. **input_file.py**: The Python file to obfuscate.
2. **-o, --output**: (Optional) The output file to save the obfuscated code. If not provided, the result is printed to stdout.
3. **--remove-docstrings**: (Optional) Remove docstrings from the code.
4. **--compact**: (Optional) Compact the code into fewer lines.
5. **--seed**: (Optional) Seed for random number generation (ensures reproducible obfuscation).
6. **-n, --name-length**: (Optional) Length of the generated random names (default: 6).
7. **--type**: (Optional) Type of generated random names (alpha for alphabetic, numeric for numeric; default: alpha).

### Example

```bash
pyobfuscate example.py -o obfuscated_example.py --remove-docstrings --compact --seed 42
```

### Programmatic Usage

You can also use pyobfuscate programmatically in your Python scripts:

```python
from pyobfuscate.obfuscate import PythonObfuscator

# Initialize the obfuscator
obfuscator = PythonObfuscator(seed=42)

# Obfuscate the source code
source_code = """
def my_function(x):
    return x + 1
"""

obfuscated_code = obfuscator.obfuscate(
    source_code,
    remove_docstrings=True,
    compact=True,
    name_length=8,
    name_type='alpha'
)

print(obfuscated_code)
```

## :handshake: Contributing

Contributions are welcome! If you’d like to contribute to pyobfuscate, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push them to your fork.
4. Submit a pull request with a detailed description of your changes.

## :scroll: License

This project is licensed under the MIT License. See the LICENSE file for details.