from operation import Operations, CustomException

# Create an instance of the Operations class
operation = Operations()

# Test file operations
operation.set_file_details("example.txt", "w")
operation.open_file()

# Test mathematical operations
operation.number = 16
operation.square_root()

# Test string operations
operation.string = "Hello, world! This is a sample string."
operation.string_operations()

# Test custom exception
try:
    raise CustomException("This is a custom exception.")
except CustomException as e:
    print(e)