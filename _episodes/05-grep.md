---
title: "Loops"
teaching: 15
exercises: 0
questions:
- "How can I perform the same actions on many different files?"
objectives:
- "Write a loop that applies one or more commands separately to each file in a set of files."
- "Trace the values taken on by a loop variable during execution of the loop."
- "Explain the difference between a variable's name and its value."
- "Explain why spaces and some punctuation characters shouldn't be used in file names."
- "Demonstrate how to see what commands have recently been executed."
- "Re-run recently executed commands without retyping them."
keypoints:
- "A `for` loop repeats commands once for every thing in a list."
- "Every `for` loop needs a variable to refer to the thing it is currently operating on."
- "Use `$name` to expand a variable (i.e., get its value). `${name}` can also be used."
- "Do not use spaces, quotes, or wildcard characters such as '*' or '?' in filenames, as it complicates variable expansion."
- "Give files consistent names that are easy to match with wildcard patterns to make it easy to select them for looping."
- "Use the up-arrow key to scroll up through previous commands to edit and repeat them."
- "Use `Ctrl-R` to search through the previously entered commands."
- "Use `history` to display recent commands, and `!number` to repeat a command by number."
---

So he has been receiving substantial money from Bishop Industries and has received many emails from Martin Bishop.

Let's find all the Martin Bishop emails

~~~
$ ls emails/martin_bishop.*
~~~
{: .bash}

And let's read one.

~~~
$ cat emails/martin_bishop.SOMEDATA.txt
~~~
{: .bash}

Oh no! It looks like it has been encrypted.

I wonder if he used a similar password for everything.

## grep

TODO: Introduce grep

## Exercise

~~~
$ grep password emails/*
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

