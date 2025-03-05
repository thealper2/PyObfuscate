import argparse


def setup_argparser() -> argparse.ArgumentParser:
    """
    Sets command line arguments.

    Returns:
        argparse.ArgumentParser: Argument parser
    """
    parser = argparse.ArgumentParser(description="Python Code Obfuscator")

    parser.add_argument("input_file", help="Python file to obfuscate")
    parser.add_argument("-o", "--output", help="Output file for the obfuscated code")
    parser.add_argument(
        "--remove-docstrings",
        action="store_true",
        help="Remove docstrings from the code",
    )
    parser.add_argument(
        "--compact", action="store_true", help="Compact the code into fewer lines"
    )
    parser.add_argument("--seed", type=int, help="Seed for random number generation")
    parser.add_argument(
        "-n",
        "--name-length",
        type=int,
        default=6,
        help="Length of generated random names",
    )
    parser.add_argument(
        "--type",
        choices=["alpha", "numeric"],
        default="alpha",
        help="Type of generated random names (alpha or numeric)",
    )
    return parser
