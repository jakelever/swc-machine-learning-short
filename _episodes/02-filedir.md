---
title: "Last Words"
teaching: 15
exercises: 0
questions:
- "How can I move around on my computer?"
- "How can I see what files and directories I have?"
- "How can I specify the location of a file or directory on my computer?"
objectives:
- "Explain the similarities and differences between a file and a directory."
- "Translate an absolute path into a relative path and vice versa."
- "Construct absolute and relative paths that identify specific files and directories."
- "Explain the steps in the shell's read-run-print cycle."
- "Identify the actual command, flags, and filenames in a command-line call."
- "Demonstrate the use of tab completion, and explain its advantages."
keypoints:
- "The file system is responsible for managing information on the disk."
- "Information is stored in files, which are stored in directories (folders)."
- "Directories can also store other directories, which forms a directory tree."
- "`cd path` changes the current working directory."
- "`ls path` prints a listing of a specific file or directory; `ls` on its own lists the current working directory."
- "`pwd` prints the user's current working directory."
- "`whoami` shows the user's current identity."
- "`/` on its own is the root directory of the whole file system."
- "A relative path specifies a location starting from the current location."
- "An absolute path specifies a location from the root of the file system."
- "Directory names in a path are separated with '/' on Unix, but '\\\\' on Windows."
- "'..' means 'the directory above the current one'; '.' on its own means 'the current directory'."
- "Most files' names are `something.extension`. The extension isn't required, and doesn't guarantee anything, but is normally used to indicate the type of data in the file."
- "Most commands take options (flags) which begin with a '-'."
---

The part of the operating system responsible for managing files and directories
is called the **file system**.
It organizes our data into files,
which hold information,
and directories (also called "folders"),
which hold files or other directories.

The image below gives a summary of the filesystem that we're going to be looking at. You can see that the ??? folder is inside the ??? folder. And that the README.md file is inside the ??? folder.

![The File System](../fig/filesystem.svg)

### Starting Off

Several commands are frequently used to create, inspect, rename, and delete files and directories.
To start exploring them,
let's open a shell window:

~~~
$
~~~
{: .bash}

The dollar sign is a **prompt**, which shows us that the shell is waiting for input;
your shell may use a different character as a prompt and may add information before
the prompt. When typing commands, either from these lessons or from other sources,
do not type the prompt, only the commands that follow it.

### Where am I?

Using a graphical user interface (GUI), you use double-click a folder and it shows the contents of that folder in a window (known as Explorer in Windows and Finder on Macs). First we want to know where in the filesystem we are. For that we use the `pwd`

~~~
$ pwd
~~~
{: .bash}

~~~
/home/exampleuser/
~~~
{: .output}

### I want to go somewhere
cd

tab-complete
up and down arrows

### What is here?
ls

what are flags/arguments?
ls with flags

### Simple file reading
cat

### Example Problem
Let's read the README file

### Your Problem
Read the emails from the day that he disappeared
