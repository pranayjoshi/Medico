import os
directory = "./"
import sys
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith('.py'):
            file_ptr = open(file, 'r')
            old_content = file_ptr.read()
            file_ptr = open(file, 'w')
            file_ptr.write("''' \nMIT License\n\nCopyright (c) 2020 Pranay Joshi\n'''")
            file_ptr.write(old_content)