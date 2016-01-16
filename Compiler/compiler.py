import subprocess
import os


class Compiler():
    def __init__(self, code, file_name, program_input=None, reuse_file=None):
        self.code = code
        self.file_name = file_name
        self.input = program_input
        self.reuse_file = False if reuse_file is None else reuse_file
        self.file_path = os.path.dirname(os.path.realpath(__file__)) + '/hack_us/' + self.file_name
        self.has_file = False

    def change_input(self, file_input):
        self.input = file_input

    def compile(self):
        current_dir_path = os.path.dirname(os.path.realpath(__file__))
        if not self.has_file:
            f = open(self.file_path, 'w')
            f.write(self.code)
            f.close()
        command = current_dir_path + "/compile.sh python " + self.file_path + " " + ("" if self.input is None else ("\"" + self.input + "\""))
        p = subprocess.Popen([command],
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             shell=True)
        (std_out, std_err) = p.communicate()

        if not self.reuse_file:
            self.remove_file()
        else:
            self.has_file = True
        if std_err == '':
            return std_out
        return std_err


    def remove_file(self):
        os.remove(self.file_path)

