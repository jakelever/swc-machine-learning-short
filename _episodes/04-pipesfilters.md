---
title: "Communication Skills"
teaching: 15
exercises: 0
questions:
- "How can I combine existing commands to do new things?"
objectives:
- "Redirect a command's output to a file."
- "Process a file instead of keyboard input using redirection."
- "Construct command pipelines with two or more stages."
- "Explain what usually happens if a program or pipeline isn't given any input to process."
- "Explain Unix's 'small pieces, loosely joined' philosophy."
keypoints:
- "`cat` displays the contents of its inputs."
- "`head` displays the first few lines of its input."
- "`tail` displays the last few lines of its input."
- "`sort` sorts its inputs."
- "`wc` counts lines, words, and characters in its inputs."
- "`*` matches zero or more characters in a filename, so `*.txt` matches all files ending in `.txt`."
- "`?` matches any single character in a filename, so `?.txt` matches `a.txt` but not `any.txt`."
- "`command > file` redirects a command's output to a file."
- "`first | second` is a pipeline: the output of the first command is used as the input to the second."
- "The best way to use the shell is to use pipes to combine simple single-purpose programs (filters)."
---

Next we should check his emails.

~~~
$ ls emails/
~~~
{: .bash}

~~~
$ cat emails_summary/sent/jason.txt
~~~
{: .bash}

## Number of lines in a file

~~~
$ wc -l emails/jason.summary.txt
~~~
{: .bash}

~~~
$ wc -l emails/*
~~~
{: .bash}

## TODO: Introduce saving to file


~~~
$ wc -l emails/* > email_counts.txt
~~~
{: .bash}

~~~
$ sort email_counts
~~~
{: .bash}

That doesn't work!

~~~
$ sort -n email_counts
~~~
{: .bash}



## TODO: Introduce pipes


## Challenge

~~~
$ wc -l emails/* | sort -n
~~~
{: .bash}

~~~
$ wc -l emails/* | sort -n | tail -n 2 | head -n 1
~~~
{: .bash}

TODO: Maybe include head/tail in the reading emails exercise later?

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



