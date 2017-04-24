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

The image below gives a summary of the filesystem that we're going to be looking at. You can see that the email folder is inside the adventure-data folder. And that the README.md file is inside the ??? folder.

![The File System](../fig/filesystem.svg)

TODO: Make a partial filesystem with question marks for places we're going to investigate. Specifically make the tools directory something we know about and the laptop contents a mystery.

## Starting Off

Several commands are frequently used to create, inspect, rename, and delete files and directories. To start exploring them, let's open a shell window:

~~~
$
~~~
{: .bash}

The dollar sign is a **prompt**, which shows us that the shell is waiting for input;
your shell may use a different character as a prompt and may add information before
the prompt. When typing commands, either from these lessons or from other sources,
do not type the prompt, only the commands that follow it.

## Where am I?

Windows and MacOS uses a graphical user interface (GUI) to let you interact with files. You can click on folders to move around the file system and see everything presented as icons. With the shell, everything is presented as text and the way to interact is by typing commands.

First we want to know where in the filesystem we are. For that we use the `pwd` command. It stands for "print working directory". The working directory is the name used for the directory that we are currently in. All commands that we run will be based in this directory (unless we specify otherwise).

~~~
$ pwd
~~~
{: .bash}

~~~
/home/exampleuser/
~~~
{: .output}

The output will look different for you and depend on what type of system you are using and your own username. The first forward slash designates the root of the whole file system. We are then inside the home directory, and then inside the exampleuser directory.

> ### Home directory
>
> You normally start in your home directory. On Linux, this is normally /home/USERNAME, for windows it is /C/Users/USERNAME and for MacOsX it is /Users/USERNAME (where USERNAME is your username).
{: .callout}

## What is here?

With a GUI, the files appear as little icons. But with the shell, we need to use a command to get a list of files in the current working directory. For that we use `ls` which stands for "list".

~~~
$ ls
~~~
{: .bash}

~~~
documents Desktop downloads thesis.pdf
~~~
{: .output}

This gives the contents of current directory. Notice that it shows both files and directories.

> ### Arguments
>
> When you call a command, you can give it extra information on what it should do. These are often called arguments or parameters. This might be a signal to give the output in a different format, or to process a different file. It depends on the program.
{: .callout}

A useful argument for `ls` is to get more details using `-l`. Try it out. Now each file/directory is on each line with extra information.

~~~
$ ls -l
~~~
{: .bash}

~~~
drwxr-sr-x  2 exampleuser users 4096 Apr 23 15:39 documents
drwxr-sr-x  2 exampleuser users 4096 Apr 23 15:39 Desktop
drwxr-sr-x  2 exampleuser users 4096 Apr 23 15:39 downloads
-rw-r--r--  1 exampleuser users  210 Apr 23 15:39 thesis.pdf
~~~
{: .output}

The `ls` command has a lot of possible arguments. Many commands will give you more information using the `--help` argument. Give it a try with ls.

~~~
$ ls --help
~~~
{: .bash}

> ## The Manual
>
> On most linux machine, there is a `man` command that gives you the manual for a command. So `man ls` gives a similar output to `ls --help`. So commands don't use `--help` and some don't have a manual page. Unfortunately git for windows doesn't support `man`. In that cause, a quick Google search for "man page" plus the name of the command will provide the relevant information.
{: .callout}

## I want to go somewhere

It's not much fun staying in the same place, so to get moving we use `cd`. It stands for "change directory". But it normally takes one argument. In this case, the extra piece is where we should move to. The easiest is the name of a directory in our current working directory. Let's try moving to the Desktop (which is normally a directory called Desktop in your home directory.

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
> You don't have to retype every command every time. Try using the up and down arrows on the keyboard to cycle through previous commands.
{: .callout}

TODO: Maybe an ls here?
Let's keep going to the downloaded files (TODO: add a link with extra instructions).

~~~
$ cd data-shell
~~~
{: .bash}

> ## Tab-complete
>
> Shell users are lazy and typing out long filenames is tedious. If you've started typing a filename, you can press Tab and the shell will try to complete the rest (if there is only one possibility).
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

## Reading Tiny Files

The `cat` command is a very basic command that displays the contents of a file. It actually stands for concatenate as you can use it to concatenate multiple files. You should only use it to display very small files which will contain unformatted text. It can't deal with things like PDFs or Word documents. Its most basic usage involves one argument: the name of the file you want to display.

~~~
$ cat README.md
~~~
{: .bash}

## Exercise

Can you read the summary for the GIBSON project? It will be in the research_files directory.

> ## Solution
>
> The command `ls -R` lists the contents of directories recursively, i.e., lists
> their sub-directories, sub-sub-directories, and so on in alphabetical order
> at each level. The command `ls -t` lists things by time of last change, with
> most recently changed files or directories first.
> In what order does `ls -R -t` display things? Hint: `ls -l` uses a long listing
> format to view timestamps.
>
{: .solution}


