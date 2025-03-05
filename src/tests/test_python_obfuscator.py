import unittest
from src.pyobfuscate.obfuscator import PythonObfuscator


class TestPythonObfuscator(unittest.TestCase):
    def setUp(self):
        self.obfuscator = PythonObfuscator(seed=42)

    def test_generate_random_name_alpha(self):
        name = self.obfuscator._generate_random_name(length=8, name_type="alpha")
        self.assertEqual(len(name), 8)
        self.assertTrue(name.isalpha())

    def test_generate_random_name_numeric(self):
        name = self.obfuscator._generate_random_name(length=8, name_type="numeric")
        self.assertEqual(len(name), 9)
        self.assertTrue(name[1:].isdigit())

    def test_obfuscate_variable_names(self):
        source_code = "var1 = 10\nvar2 = var1 + 5"
        obfuscated_code = self.obfuscator.obfuscate(source_code)
        self.assertNotIn("var1", obfuscated_code)
        self.assertNotIn("var2", obfuscated_code)

    def test_obfuscate_function_names(self):
        source_code = "def my_func():\n    return 42"
        obfuscated_code = self.obfuscator.obfuscate(source_code)
        self.assertNotIn("my_func", obfuscated_code)

    def test_obfuscate_class_names(self):
        source_code = "class MyClass:\n    pass"
        obfuscated_code = self.obfuscator.obfuscate(source_code)
        self.assertNotIn("MyClass", obfuscated_code)

    def test_protected_names(self):
        source_code = "print(len('hello'))"
        obfuscated_code = self.obfuscator.obfuscate(source_code)
        self.assertIn("print", obfuscated_code)
        self.assertIn("len", obfuscated_code)

    def test_remove_docstrings(self):
        source_code = 'def my_func():\n    """Docstring"""\n    return 42'
        obfuscated_code = self.obfuscator.obfuscate(source_code, remove_docstrings=True)
        self.assertNotIn('"""Docstring"""', obfuscated_code)

    def test_compact_code(self):
        source_code = "var1 = 10\nvar2 = 20\nvar3 = var1 + var2"
        obfuscated_code = self.obfuscator.obfuscate(source_code, compact=True)
        self.assertEqual(obfuscated_code.count("\n"), 0)


if __name__ == "__main__":
    unittest.main()
