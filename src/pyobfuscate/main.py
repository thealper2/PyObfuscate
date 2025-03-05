from src.pyobfuscate.obfuscator import PythonObfuscator
from src.pyobfuscate.utils import setup_argparser


def main():
    """
    Main function to handle command-line arguments and perform obfuscation.
    """
    parser = setup_argparser()
    args = parser.parse_args()

    # Read the input file
    with open(args.input_file, "r") as f:
        source_code = f.read()

    # Create an obfuscator instance and obfuscate the code
    obfuscator = PythonObfuscator(seed=args.seed)
    obfuscated_code = obfuscator.obfuscate(
        source_code,
        remove_docstrings=args.remove_docstrings,
        compact=args.compact,
        name_length=args.name_length,
        name_type=args.type,
    )

    # Write the obfuscated code to the output file or print it
    if args.output:
        with open(args.output, "w") as f:
            f.write(obfuscated_code)
    else:
        print(obfuscated_code)
