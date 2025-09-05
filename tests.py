# from functions.get_files_info import get_files_info
from functions.write_file import write_file
import os

def main():
    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(result)
    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(result)
    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(result)
    
    
main()
