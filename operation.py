import math

class Operations:
    def _init_(self):
        self.filename = ""
        self.file_mode = ""
        self.number = 0
        self.string = ""

    def set_file_details(self, filename, file_mode):
        self.filename = filename
        self.file_mode = file_mode

    def open_file(self):
        try:
            file = open(self.filename, self.file_mode)
            print(f"File '{self.filename}' opened in mode '{self.file_mode}' successfully.")
            file.close()
        except IOError:
            print("An error occurred while opening the file.")

    def square_root(self):
        try:
            result = math.sqrt(self.number)
            print(f"The square root of {self.number} is {result}.")
        except ValueError:
            print("Invalid input. Cannot calculate square root of a negative number.")

    def string_operations(self):
        words = self.string.split()
        print(f"The number of words in the string '{self.string}' is {len(words)}.")

class CustomException(Exception):
    def _init_(self, message):
        self.message = message

    def _str_(self):
        return f"Custom Exception: {self.message}"