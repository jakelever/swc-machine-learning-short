---
title: "Banking Issues"
teaching: 15
exercises: 0
questions:
- "How can I create, copy, and delete files and directories?"
- "How can I edit files?"
objectives:
- "Create a directory hierarchy that matches a given diagram."
- "Create files in that hierarchy using an editor or by copying and renaming existing files."
- "Display the contents of a directory using the command line."
- "Delete specified files and/or directories."
keypoints:
- "`cp old new` copies a file."
- "`mkdir path` creates a new directory."
- "`mv old new` moves (renames) a file or directory."
- "`rm path` removes (deletes) a file."
- "Use of the Control key may be described in many ways, including `Ctrl-X`, `Control-X`, and `^X`."
- "The shell does not have a trash bin: once something is deleted, it's really gone."
- "Nano is a very simple text editor: please use something else for real work."
---

## Starting some Analysis

Make sure we're in the data-shell directory
~~~
$ pwd
~~~
{: .bash}

~~~
$ mkdir analysis
$ ls
$ cd analysis
~~~
{: .bash}

## Tools?

~~~
$ ls ../tools
~~~
{: .bash}

Finances seem like a good place to start

TODO: Introduce `sh` command

~~~
$ sh ../tools/finance_summary.sh --help
~~~
{: .bash}

The script will load files from the statements folder and save to a summary.tsv file.


## Running a tool

TODO: Introduce each command

~~~
$ mkdir statements
~~~
{: .bash}

~~~
$ cp accounts/ADKLANSDLASD/2016-01-01.tsv statements
~~~
{: .bash}

~~~
$ cp accounts/ADKLANSDLASD/* statements
~~~
{: .bash}

~~~
$ sh ../tools/finance_summary.sh
~~~
{: .bash}

~~~
187 transactions summarized in file results.tsv
~~~
{: .output}

~~~
$ cat results.tsv
~~~
{: .bash}

Outputs file to results.tsv. BIG RED FLAG that this is a bad script!!!

Let's try it for one account
~~~
$ sh ../tools/finance_summary.sh
~~~
{: .bash}

~~~
ERROR: results.tsv already exists
~~~
{: .output}

Oh no. We'll need to move or delete the file!

~~~
$ mv results.tsv summary-ACC_9530294.tsv
~~~
{: .bash}

TODO: Fit in rm in here

## The Challenge

Can you get a summary for all the accounts?

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

## Bonus Points

Could you create a script that takes as input a directory and filename for output and runs the summary script?
