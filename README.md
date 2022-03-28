# File-System-Comparision-CS446-PA3
Compare and contrast single level file directories with hierarchical file directories.

General Instructions and Hints: 

Name files exactly as described in the documentation below.
When the assignment is done, zip or tarball the specified files into a folder with the name <netid>_CS446_PA3.zip or  <netid>_CS446_PA3.tar.gz (for example sarad_CS446_PA3.tar.gz).
All work should be done on a machine where you have sudoer permission. If you do not have linux on your machine, or sudo permissions on a linux machine, there is a video about ssh-ing into the school's engineering server under files -> Lecture Recordings, or you can use any of the methods outlined hereLinks to an external site., which include a remote option to access school resources. 
The assignment can be done in Python3 or C. I recommend Python, but I am also biased.
You may import the glob, numpy, sys, pandas, and/or os libraries in Python if you would like. You may include stdlib, stdio in C if you would like.
 

-Part 1-

***To be done individually.***

Background

Single level file systems store all files in a root directory. Hierarchical file systems store files in groups called directories. Each directory (/usr for example) is a subdirectory of the root directory. A single level file system is considered to be easy to implement but difficult to organize or secure. Hierarchical file systems are considered to be slightly more difficult to implement, but are better at organizing and providing a layer of security.

Directions

Implementation is up to you- however, your program should be functional (there should be multiple functions- functions typically have one purpose. For example, a write function would only write, and traverse function would only traverse directories). Name your code file either fileSystemComparison.c or fileSystemComparison.py (depending on the language you choose to use).

To construct the single level directory, do the following:

Create a directory called "/singleRoot" in /home
Within singleRoot, generate 100 files, named file1.txt ... file100.txt
To construct the hierarchical level directory, do the following:

Create a directory called "/hierarchicalRoot" in /home
Within hierarchicalRoot, generate 100 files named file1.txt ... file100.txt
Create 10 directories for your 100 files. Your first directory should be called files1-10, your second should be files11-20 and so on. 
Either create these directories first and then generate the appropriate text files within, or generate your files first and move them to the appropriate directory after generating the directory
To determine size difference between single level and hierarchical, do the following:

Starting from your new root directories (singleRoot and hierarchicalRoot), write a program that starts at the root, and then descends the file tree (if it can) from the root. 
For both singleLevel and hierarchical, save the size of all the files and the names that you find into a data structure (if python, I suggest a list or dict). Write each filename and its size to a text file in the associated root. Name it singleLevelFiles.txt and hierarchicalFiles.txt, respectively.
hierarchicalFiles.txt should contain the size of each directory as part of its contents (single level doesn't need this, because single level doesn't use other directories)
Print the number of files in each txt file (singleLevelFiles and hierarchicalFiles) to the screen
Print the average size of each file to the screen
To determine the difference in traversal time, do the following:

Import or include a time library that allows you to track how long it takes to get all of the data about files in singleLevelFiles, and how long it takes to get all of the data about files and directories in hierarchicalFiles. Print the execution time to the screen after you've printed the number of files and average size. 
In summary, you will have code to generate your singleLevel directory. You will generate 100 files within that directory. You will calculate the number of files in the singleLevel directory. You will calculate the average size of the files in the singleLevel directory. You will calculate the execution time to descend from root and gather all file names/sizes. Print each value in that order. Repeat the same exercise for hierarchical, including the subdirectory names and sizes. 

 

 

Part 1 Requirements and Hints : 

This assignment is much easier in Python. 
You are welcome to use the subprocess library if you would like.
You do not need to store anything in any of the generated files. Just create them.
The only thing in your zip or tar.gz should be your copy of fileSystemComparison.py or .c
As part of your file header comment: (Links to an external site.)

 (Links to an external site.)discuss any similarities/disimilarities in the printed output between singleLevelFiles.txt and hierarchicalFiles.txt. Explain the reason these differences or similarities exist. 
We have simple file system that only supports a single-level architecture. Files can have arbitrarily long names and the root directory can have an arbitrary number of files. How could we implement something similar to a hierarchical file system? (hint, think about approximating a path)
 
