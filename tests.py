from functions.get_files_info import get_files_info
import os

def main():
    working_dir ="calculator"
    get_files_info(working_dir)
    root_content = get_files_info(working_dir)
    print(root_content)
    pkg_contents = get_files_info(working_dir,"pkg")
    print(pkg_contents)
    bin_contents = get_files_info(working_dir,"/bin")
    print(bin_contents)
    out_of_dir = get_files_info(working_dir,"../")
    print(out_of_dir)
    # print(os.path.isdir(working_dir))
main()
