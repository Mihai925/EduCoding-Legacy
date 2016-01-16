from django.test import TestCase
import autotester

# Create your tests here.
class AutotesterTest(TestCase):
    def setUp(self):
        self.sum_correct = """def sum(a, b):
    return a+b

a, b = raw_input().split()
a, b = int(a), int(b)
print sum(a, b)
    """

        self.sum_incorrect = """def sum(a, b):
    return b

a, b = raw_input().split()
a, b = int(a), int(b)
print sum(a, b)
    """

    def test_correct_code(self):
        auto_tester = autotester.AutoTester(self.sum_correct, "test1.py", True)

        self.assertTrue(auto_tester.compare("3 4", "7"))
        self.assertTrue(auto_tester.compare("3 6", "9"))
        auto_tester.remove_file()

    def test_incorrect_output(self):
        auto_tester = autotester.AutoTester(self.sum_incorrect, "test2.py")

        self.assertFalse(auto_tester.compare("1 3", "4"))