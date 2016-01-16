from django.test import TestCase
from .compiler import Compiler
# Create your tests here.

#run compiler script

#show output

class CompilerTest(TestCase):

    errored_python_code = "pint 5"

    def setUp(self):
        self.file_name = "unit_test_program.py"

    def test_simple_print(self):
        """
        A simple print runs correctly
        """
        to_print = "5"
        compiler = Compiler("print " + to_print, self.file_name)
        output = compiler.compile()
        self.assertEqual(to_print + '\n', output, output + "doesn't contain the required string")

    def test_code_errors(self):
        """
        Errors are printed out
        """
        wrong_python_code = "pint 5"
        compiler = Compiler(wrong_python_code, self.file_name)
        output = compiler.compile()

        #self.assertEquals("", output)
        #self.assertContains(output, "invalid syntax")
        self.assertTrue("invalid syntax" in output, output + "doesn't contain the required string")

    def test_code_with_input(self):
        """
        A simple print of the command line arguments
        """
        python_with_input = "print [arg for arg in raw_input().split()];"
        compiler = Compiler(python_with_input, self.file_name, "500 400")
        output = compiler.compile()
        self.assertTrue("500" in output, output + "is wrong")
        self.assertTrue("400" in output)
