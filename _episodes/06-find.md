---
title: "Too Many Files (find)"
teaching: 15
exercises: 0
questions:
- "How can I save and re-use commands?"
objectives:
- "Use `find` to find files whose names match simple patterns."
keypoints:
- "`find` finds files with specific properties that match patterns."
---

This Martin Bishop character is beginning to look rather suspicious. It's time we look into the email communication between Dr Gill and Mr Bishop.

# The emails directory

All of Dr Gill's emails are in the emails directory.

~~~
$ ls emails/
~~~
{: .bash}

Oh dear, there are a lot of directories. The emails have been grouped by the day that they were sent or received. Let's have a look in one of them.

~~~
$ ls emails/01_01_2017
~~~
{: .bash}

It would appear each email is its own file. And they are named "RECEIVED_FROM_" or "SENT_TO_" and then the person's name and time.

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
$ find email_summaries/ -name 'Joan*'
~~~
{: .bash}

> ## The Manual
>
> On most linux machine, there is a `man` command that gives you the manual for a command. Some commands don't use `--help` and some don't have a manual page. Unfortunately git for windows doesn't support `man`. In that cause, a quick Google search for "man page" plus the name of the command will provide the relevant information.
{: .callout}

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

That's a lot of emails. We could count them by piping `find` in `wc -l`

~~~
$ find emails/ -name 'SENT_TO_Martin_Bishop*' | wc -l
~~~
{: .bash}
~~~
108
~~~
{: .output}

This says that Dr Gill emailed Martin Bishop 108 times and matches up with the email summaries file.

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
