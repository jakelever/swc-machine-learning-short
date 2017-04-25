---
title: "Too Many Files"
teaching: 15
exercises: 0
questions:
- "How can I save and re-use commands?"
objectives:
- "Write a shell script that runs a command or series of commands for a fixed set of files."
- "Run a shell script from the command line."
- "Write a shell script that operates on a set of files defined by the user on the command line."
- "Create pipelines that include shell scripts you, and others, have written."
keypoints:
- "Save commands in files (usually called shell scripts) for re-use."
- "`bash filename` runs the commands saved in a file."
- "`$@` refers to all of a shell script's command-line parameters."
- "`$1`, `$2`, etc., refer to the first command-line parameter, the second command-line parameter, etc."
- "Place variables in quotes if the values might have spaces in them."
- "Letting users decide what files to process is more flexible and more consistent with built-in Unix commands."
---

This Martin Bishop character is beginning to look rather suspicious. It's time we look into the email communication between Dr Gill and Mr Bishop.

# The emails directory

All of Dr Gill's emails are in the emails directory.

~~~
$ ls emails/
~~~
{: .bash}

Oh dear, there are a lot of directories.

~~~
$ ls emails/SOME_DIRECTORY
~~~
{: .bash}

It would appear each email is its own file. And they are named "RECEIVED_FROM_" or "SENT_TO_" and then the person's name.

We need a tool to be able to search for a specific file.

# Finding files.

We've already covered finding things in a single file using `grep`. Now we cover finding files within a file system using `find`. This is another very powerful file.

It takes one main argument, a directory to search, and many more arguments that define the filters use to display the files.

Let's see it without a filter:

~~~
$ find email_summaries/
~~~
{: .bash}

It will print out every file or directory within the email_summaries directory, and go into each subdirectory.

Let's try it with the `-name` filter. We specify a pattern, using a wildcard if we want, to find files or directories that match.

~~~
$ find email_summaries/ -name 'TODO*'
~~~
{: .bash}

Another filter is `-type`. To filter for files:

~~~
$ find email_summaries/ -type f
~~~
{: .bash}

And to filter for directories:

~~~
$ find email_summaries/ -type d
~~~
{: .bash}

## Email Time

Now let's see if we can find all the emails sent to Martin Bishop.

~~~
$ find emails/ -name 'SENT_TO_Martin_Bishop*'
~~~
{: .bash}

## Exercise

Find all the email received from Martin Bishop. Is there anything suspicious about the result?

> ## Solution
>
> ~~~
> $ find emails/ -name 'RECEIVED_FROM_Martin_Bishop*'
> ~~~
> {: .bash}
>
{: .solution}
