import random
import string
import ast
import astor
from typing import Optional, Set, Literal

from src.pyobfuscate.transformer import ObfuscateTransformer


class PythonObfuscator:
    """
    A class to obfuscate Python source code by renaming variables, functions, and classes
    to random names, and optionally removing docstrings and compacting the code.
    """

    def __init__(self, seed: Optional[int] = None):
        """
        Initializes the PythonObfuscator with an optional seed for random number generation.

        Args:
            seed (Optional[int]): Seed for the random number generator. If None, the system time is used.
        """
        self.random = random.Random(seed)
        # Set of protected names that should not be obfuscated (e.g., Python keywords, built-ins, etc.)
        self.protected_names: Set[str] = {
            "False",
            "None",
            "True",
            "and",
            "as",
            "assert",
            "async",
            "await",
            "break",
            "class",
            "continue",
            "def",
            "del",
            "elif",
            "else",
            "except",
            "finally",
            "for",
            "from",
            "global",
            "if",
            "import",
            "in",
            "is",
            "lambda",
            "nonlocal",
            "not",
            "or",
            "pass",
            "raise",
            "return",
            "try",
            "while",
            "with",
            "yield",
            "__name__",
            "__main__",
            "__file__",
            "self",
            "print",
            "len",
            "str",
            "int",
            "float",
            "list",
            "dict",
            "set",
            "tuple",
            "range",
            "enumerate",
            "zip",
            "map",
            "filter",
        }

    def _generate_random_name(
        self, length: int = 6, name_type: Literal["alpha", "numeric"] = "alpha"
    ) -> str:
        """
        Generates a random name of the specified type and length.

        Args:
            length (int): Length of the random name. Default is 6.
            name_type (Literal['alpha', 'numeric']): Type of the random name.
                'alpha' generates lowercase letters, 'numeric' generates digits prefixed with 'O'.

        Returns:
            str: A randomly generated name.
        """
        if name_type == "alpha":
            return "".join(self.random.choices(string.ascii_lowercase, k=length))
        else:  # numeric
            return "O" + "".join(self.random.choices(string.digits, k=length))

    def obfuscate(
        self,
        source_code: str,
        remove_docstrings: bool = False,
        compact: bool = False,
        name_length: int = 6,
        name_type: Literal["alpha", "numeric"] = "alpha",
    ) -> str:
        """
        Obfuscates the provided Python source code by renaming variables, functions, and classes,
        and optionally removing docstrings and compacting the code.

        Args:
            source_code (str): The Python source code to obfuscate.
            remove_docstrings (bool): If True, removes docstrings from the code. Default is False.
            compact (bool): If True, compacts the code into fewer lines. Default is False.
            name_length (int): Length of the generated random names. Default is 6.
            name_type (Literal['alpha', 'numeric']): Type of the generated random names. Default is 'alpha'.

        Returns:
            str: The obfuscated Python source code.
        """
        # Parse the source code into an AST
        tree = ast.parse(source_code)
        # Create and apply the obfuscation transformer
        transformer = ObfuscateTransformer(
            self.random,
            self.protected_names,
            name_length,
            name_type,
            remove_docstrings,
            self._generate_random_name,
        )
        modified_tree = transformer.visit(tree)
        ast.fix_missing_locations(modified_tree)

        # Convert the modified AST back to source code
        obfuscated_code = astor.to_source(modified_tree)

        # Compact the code if requested
        if compact:
            obfuscated_code = " ".join(
                line.strip() for line in obfuscated_code.split("\n")
            )

        return obfuscated_code
