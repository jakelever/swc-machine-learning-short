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
TODO: Make a partial filesystem with question marks for places we're going to investigate. Specifically make the tools directory something we know about and the laptop contents a mystery.

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

Using a graphical user interface (GUI), you use double-click a folder and it shows the contents of that folder in a window (known as Explorer in Windows and Finder on Macs). First we want to know where in the filesystem we are. For that we use the `pwd` command. It stands for "print working directory". The working directory is the name used for the directory that we are currently in. All commands that we run will be based in this directory (unless we specify otherwise).

~~~
$ pwd
~~~
{: .bash}

~~~
/home/exampleuser/
~~~
{: .output}

TODO: Mention home directory.

### What is here?

With a GUI, the files appear as little icons. But with the shell, we need to use a command to get a list of files in the current working directory. For that we use `ls` which stands for "list".

~~~
$ ls
~~~
{: .bash}

~~~
TODO: Results go here
~~~
{: .output}

This gives the contents of current directory.

TODO: Talk about flags here or later?

### I want to go somewhere

It's not much fun staying in the same place, so to get moving we use `cd`. It stands for "change directory". But it normally takes one "argument". An argument is an extra piece of information about what the command should do. In this case, the extra piece is where we should move to. The easiest is the name of a directory in our current working directory. Let's try moving to the Desktop (which is normally a directory called Desktop in your home directory.

~~~
$ cd Desktop
~~~
{: .bash}

And a quick check with `pwd` shows that we've moved.

~~~
$ pwd
~~~
{: .bash}

~~~
/home/exampleuser/Desktop/
~~~
{: .output}


> ## Up and Down arrows
>
> TODO: Up and Down arrows
{: .callout}

TODO: Maybe an ls here?
Let's keep going to the downloaded files (TODO: add a link with extra instructions).

~~~
$ cd data-shell
~~~
{: .bash}

> ## Tab-complete
>
> TODO: Example tab complete
{: .callout}

Let's check what we've got.

~~~
$ ls
~~~
{: .bash}

~~~
TODO: Results go here
~~~
{: .output}

Hmm, maybe that README file would tell us more about the files.

### Example Challenge

The `cat` command is a very basic command that displays the contents of a file. It actually stands for concatenate as you can use it to concatenate multiple files. You should only use it to display very small files which will contain unformatted text. It can't deal with things like PDFs or Word documents. Its most basic usage involves one argument: the name of the file you want to display.

~~~
$ cat README.md
~~~
{: .bash}

### Example Problem


### Your Challenge
Can you read the email that was received on day that JOEBLOGGS disappeared?


