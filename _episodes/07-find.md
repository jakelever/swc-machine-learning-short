---
title: "Finding Things"
teaching: 15
exercises: 0
questions:
- "How can I find files?"
- "How can I find things in files?"
objectives:
- "Use `grep` to select lines from text files that match simple patterns."
- "Use `find` to find files whose names match simple patterns."
- "Use the output of one command as the command-line parameters to another command."
- "Explain what is meant by 'text' and 'binary' files, and why many common tools don't handle the latter well."
keypoints:
- "`find` finds files with specific properties that match patterns."
- "`grep` selects lines in files that match patterns."
- "`--help` is a flag supported by many bash commands, and programs that can be run from within Bash, to display more information on how to use these commands or programs."
- "`man command` displays the manual page for a given command."
- "`$(command)` inserts a command's output in place."
---

Last but not least, we're going to find a file mentioned in the last encrypted email.

## Find

~~~
$ find emails
~~~
{: .bash}

~~~
$ find emails -f
~~~
{: .bash}

~~~
$ find emails -d
~~~
{: .bash}

~~~
$ find . -name 'README.md'
~~~
{: .bash}

~~~
$ find emails -name 'martin_bishop*'
~~~
{: .bash}


## Exercise

The name of the file mentioned in the email was "babbage.txt". Can you find it in the "research_files" directory?

~~~
$ find ./research_files -name 'babbage.txt'
~~~
{: .bash}

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

Use find to get bank statements from a specific date?

Use find to get any emails on a specific date. Think about using the wildcard!
