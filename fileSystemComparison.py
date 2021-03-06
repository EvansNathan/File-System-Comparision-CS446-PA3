# Author: Nathan Evans
# Date: 28 March 2022
# Purpose: Compare and contrast single level file directories with hierarchical file directories.

# Hierarchical and Single root directories take the same amount of space (as shown below)
# The differences begin with security. A single root file system does not allow different users to
# secure their oen file in a hierarchical structure files can be contained per user and links can be
# made to share files from a visual perspective it is easier to navigate an organized file system like
# a hierarchical but if all files were in one directory it can be hard to search with GUIs

import time
import os


def create_single_directory(num_files):
    i = 0
    single_root_path = os.path.expanduser('~') + "/singleRoot/"

    begin = time.time()
    os.mkdir(single_root_path)
    while i < num_files:
        file_text = "file" + str(i) + ".txt"
        file_path = single_root_path + file_text
        f = open(file_path, "w")
        i = i + 1
    end = time.time()

    print("Number of files: " + str(i))

    return end - begin


def create_hierarchical_directory(num_files, num_directories):
    hierarchical_root_path = os.path.expanduser('~') + "/hierarchicalRoot/"
    x = 0
    y_start = 0
    y_end = 9
    i = 0

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

    print("Number of Files: " + str(num_files + num_directories))


def single_root_traverse():
    # Single Root
    num_files = 100
    index = 0
    file_name = ""
    directory_size = 0

    file_single_root = open((os.path.expanduser('~') + "/singleRoot/singleLevelFiles.txt"), "w")

    begin = time.time()
    while index < num_files:
        file_name = "file" + str(index) + ".txt"
        directory_size = directory_size + os.path.getsize(os.path.expanduser('~') + "/singleRoot/" + file_name)
        file_single_root.write("/home/singleRoot/" + file_name + "," + str(directory_size) + "\n")
        index = index + 1

    end = time.time()
    print("Average File Size: " + str(directory_size/num_files))

    return end - begin


def hierarchical_root_traverse():
    num_directories = 10
    num_files = 10
    index = 0
    directory_size = 0

    file_hierarchical_root = open((os.path.expanduser('~') + "/hierarchicalRoot/hierarchicalFiles.txt"), "w")

    begin = time.time()
    while num_directories > 0:
        directory_name = "files" + str(index) + "-" + str(index + 9) + "/"
        while num_files > 0:
            file_name = "file" + str(index) + ".txt"
            index = index + 1
            num_files = num_files - 1
            directory_size = directory_size + os.path.getsize(os.path.expanduser('~') + "/hierarchicalRoot/"
                                                              + directory_name + file_name)
            file_hierarchical_root.write("/home/hierarchicalRoot/" + directory_name + file_name
                                         + "," + str(directory_size) + "\n")

        num_files = 10
        num_directories = num_directories - 1

    end = time.time()
    print("Average File Size: " + str(directory_size / num_files + num_directories))
    return end - begin


def main():
    num_files = 100
    num_directories = 10

    print("Single Level File System")
    create_single_directory(num_files)
    single_execution_time = single_root_traverse()
    print "Traversal Time: " + str(single_execution_time) + " seconds" + "\n"

    print("Hierarchical File System")
    create_hierarchical_directory(num_files, num_directories)
    hierarchical_execution_time = hierarchical_root_traverse()
    print "Traversal Time: " + str(hierarchical_execution_time) + " seconds" + "\n"


if __name__ == "__main__":
    main()
