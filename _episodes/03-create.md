---
title: "Working With Files and Directories"
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

~~~
$ sh ../tools/finance_summary.sh --help
~~~
{: .bash}

## Running a tool

~~~
$ sh ../tools/finance_summary.sh ../bank_statements/2016-01/
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

Let's try it for another month
~~~
$ sh ../tools/finance_summary.sh ../bank_statements/2016-02/
~~~
{: .bash}

~~~
ERROR: results.tsv already exists
~~~
{: .output}

Oh no. We'll need to move or delete the file!

~~~
$ mv results.tsv summary-2016-01.tsv
~~~
{: .bash}
