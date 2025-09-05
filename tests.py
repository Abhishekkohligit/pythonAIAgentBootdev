# from functions.get_files_info import get_files_info
from functions.get_files_content import get_file_content
import os

def main():   
    # working_dir = "calculator"
    # print(get_file_content(working_dir, "lorem.txt"))
    # print(get_file_content("calculator", "lorem.txt"))
    
    result = get_file_content("calculator", "main.py")
    print(result)
    
    result = get_file_content("calculator", "pkg/calculator.py")
    print(result)
    
    result = get_file_content("calculator", "/bin/cat") 
    print(result)

    result = get_file_content("calculator", "pkg/does_not_exist.py") 
    print(result)
    
    
    
main()
