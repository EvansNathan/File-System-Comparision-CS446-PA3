# Author: Nathan Evans
# Date: 28 March 2022
# Purpose: Compare and contrast single level file directories with hierarchical file directories.

import time
import os


def create_single_directory(num_files):
    print "create single root directory"

    i = 0
    single_root_path = "/Users/nathanevans/Desktop/singleRoot/"
    file_path = ""

    begin = time.time()
    os.mkdir(single_root_path)
    while i < num_files:
        file_text = "file" + str(i) + ".txt"
        file_path = single_root_path + file_text
        f = open(file_path, "w")
        i = i + 1
    end = time.time()

    return end - begin


def create_hierarchical_directory():
    print "create hierarchical directory"
    hierarchical_root_path = "/Users/nathanevans/Desktop/hierarchicalRoot/"
    x = 0
    y_start = 0
    y_end = 9
    i = 0
    num_directories = 10

    begin = time.time()
    os.mkdir(hierarchical_root_path)
    while x < num_directories:
        directory_name = "files" + str(y_start) + "-" + str(y_end) + "/"
        directory_path = hierarchical_root_path + directory_name
        os.mkdir(directory_path)

        while i <= y_end:
            file_text = "file" + str(i) + ".txt"
            file_path = directory_path + file_text

            f = open(file_path, "w")
            i = i + 1

        x = x + 1
        y_start = y_start + 10
        y_end = y_end + 10

    end = time.time()

    return end - begin


def main():
    print "main"
    num_files = 100

    #single_execution_time = create_single_directory(num_files)
    #print "Execution Time: " + str(single_execution_time) + " seconds"

    #hierarchical_execution_time = create_hierarchical_directory()
    #print "Execution Time: " + str(hierarchical_execution_time) + " seconds"

    print os.path.getsize("/Users/nathanevans/Desktop/singleRoot/file0.txt")

if __name__ == "__main__":
    main()
