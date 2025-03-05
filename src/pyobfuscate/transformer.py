import ast
from typing import Dict


class ObfuscateTransformer(ast.NodeTransformer):
    """
    A custom AST NodeTransformer to traverse and modify the Python AST for obfuscation.
    """

    def __init__(
        self,
        random_generator,
        protected_names,
        name_length,
        name_type,
        remove_docstrings,
        generate_random_name,
    ):
        """
        Initializes the ObfuscateTransformer

        Args:
            random_generator: The random number generator.
            protected_names (Set[str]): Set of names that should not be obfuscated.
            name_length (int): Length of the generated random names.
            name_type (Literal['alpha', 'numeric']): Type of the generated random names.
            generate_random_name: Function to generate random names.
        """
        self.random_generator = random_generator
        self.protected_names = protected_names
        self.name_length = name_length
        self.name_type = name_type
        self.name_map: Dict[str, str] = {}  # Maps original names to obfuscated names
        self.remove_docstrings = remove_docstrings
        self._generate_random_name = generate_random_name

    def _get_obfuscated_name(self, original_name: str) -> str:
        """
        Returns an obfuscated name for the given original name.

        Args:
            original_name (str): The original name to obfuscate.

        Returns:
            str: The obfuscated name.
        """
        if original_name in self.protected_names:
            return original_name

        if original_name not in self.name_map:
            self.name_map[original_name] = self._generate_random_name(
                length=self.name_length, name_type=self.name_type
            )

        return self.name_map[original_name]

    def visit_Name(self, node: ast.Name) -> ast.Name:
        """
        Visits and obfuscated a Name node in the AST.

        Args:
            node (ast.Name): The Name code to obfuscate.

        Returns:
            ast.Name: The obfuscated Name node.
        """
        node.id = self._get_obfuscated_name(node.id)
        return node

    def visit_arg(self, node: ast.arg) -> ast.arg:
        """
        Visits and obfuscated an arg node in the AST.

        Args:
            node (ast.arg): The arg note to obfuscate.

        Returns:
            ast.arg: The obfuscated arg node.
        """
        if node.arg not in self.protected_names:
            node.arg = self._get_obfuscated_name(node.arg)

        return node

    def visit_FunctionDef(self, node: ast.FunctionDef) -> ast.FunctionDef:
        """
        Visits and obfuscated a FunctionDef node in the AST.

        Args:
            node (ast.FunctionDef): The FunctionDef node to obfuscate.

        Returns:
            ast.FunctionDef: The obfuscated FunctionDef node.
        """
        if node.name not in self.protected_names:
            node.name = self._get_obfuscated_name(node.name)

        if self.remove_docstrings:
            # # Remove docstrings from the function body
            node.body = [
                n
                for n in node.body
                if not isinstance(n, ast.Expr) or not isinstance(n.value, ast.Str)
            ]

        return self.generic_visit(node)

    def visit_ClassDef(self, node: ast.ClassDef) -> ast.ClassDef:
        """
        Visits and obfuscates a ClassDef node in the AST.

        Args:
            node (ast.ClassDef): The ClassDef node to obfuscate.

        Returns:
            ast.ClassDef: The obfuscated ClassDef node.
        """
        if node.name not in self.protected_names:
            node.name = self._get_obfuscated_name(node.name)

        if self.remove_docstrings:
            # Remove docstrings from the function body
            node.body = [
                n
                for n in node.body
                if not isinstance(n, ast.Expr) or not isinstance(n.value, ast.Str)
            ]

        return self.generic_visit(node)
