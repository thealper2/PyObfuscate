import unittest
import os
import tempfile
from src.pyobfuscate.main import main


class TestCLI(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.input_file = os.path.join(self.temp_dir.name, "input.py")
        self.output_file = os.path.join(self.temp_dir.name, "output.py")

        with open(self.input_file, "w") as f:
            f.write("var1 = 10\nvar2 = var1 + 5")

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_cli_with_output_file(self):
        import sys
        from io import StringIO
        from contextlib import redirect_stdout

        sys.argv = ["python_obfuscator.py", self.input_file, "-o", self.output_file]

        with redirect_stdout(StringIO()):
            main()

        self.assertTrue(os.path.exists(self.output_file))
        with open(self.output_file, "r") as f:
            content = f.read()
            self.assertNotEqual(content, "")

    def test_cli_without_output_file(self):
        import sys
        from io import StringIO
        from contextlib import redirect_stdout

        sys.argv = ["python_obfuscator.py", self.input_file]

        with redirect_stdout(StringIO()) as stdout:
            main()

        self.assertNotEqual(stdout.getvalue(), "")

    def test_cli_remove_docstrings(self):
        import sys
        from io import StringIO
        from contextlib import redirect_stdout

        with open(self.input_file, "w") as f:
            f.write('def my_func():\n    """Docstring"""\n    return 42')

        sys.argv = ["python_obfuscator.py", self.input_file, "--remove-docstrings"]

        with redirect_stdout(StringIO()) as stdout:
            main()

        self.assertNotIn('"""Docstring"""', stdout.getvalue())

    def test_cli_compact_code(self):
        import sys
        from io import StringIO
        from contextlib import redirect_stdout

        sys.argv = ["python_obfuscator.py", self.input_file, "--compact"]

        with redirect_stdout(StringIO()) as stdout:
            main()

        self.assertEqual(stdout.getvalue().count("\n"), 1)


if __name__ == "__main__":
    unittest.main()
