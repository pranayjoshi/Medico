import os
directory = "./src"

for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith('.py'):
            file_ptr = open(file, 'r')
            old_content = file_ptr.read()
            file_ptr = open(file, 'w')
            file_ptr.write("hello")
            file_ptr.write(old_content)