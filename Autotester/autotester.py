from Compiler.compiler import Compiler


class AutoTester():

    def __init__(self, code, file_name, reuse_file=None):
        self.code = code
        self.file_name = file_name
        self.compiler = None
        self.reuse_file = False if reuse_file is None else reuse_file

    def compare(self, input, expected_output):

        if self.compiler is None:

            self.compiler = Compiler(self.code, self.file_name, input, self.reuse_file)
        else:
            self.compiler.change_input(input)

        output = self.compiler.compile()
        return self.__compare_outputs(output.strip(), expected_output.strip())

    @staticmethod
    def __compare_outputs(expected_output, actual_output):
        return cmp(expected_output.split(), actual_output.split()) == 0
