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
$ ls email_summaries/
~~~
{: .bash}

~~~
received  sent
~~~
{: .output}

The email summaries are split up into received and sent.

~~~
$ ls email_summaries/received
~~~
{: .bash}

This shows that there is a file for each contact.

~~~
$ ls email_summaries/received/alan
~~~
{: .bash}

Shows it is a log of when alan has contacted Dr Gill.

# Who's Popular?

It'd be good to know who contacts Dr Gill the most. For this we will use the `wc` command. It calculates various statistics on a file, including the line count. The `wc` command takes a file (or set of files) as the arguments and prints out the statistics for each file.

~~~
$ wc email_summaries/received/alan
~~~
{: .bash}

~~~
18 18 45 email_summaries/received/alan
~~~
{: .output}

The statistics that it prints out are the number of lines, the number of words and the total byte count for each file.

We only want the line count, so use the `-l` argument.

~~~
$ wc -l email_summaries/received/alan
~~~
{: .bash}

~~~
18 email_summaries/received/alan
~~~
{: .output}

# Saving a result

We can use the wildcard again to process multiple files.

~~~
$ wc -l email_summaries/received/*
~~~
{: .bash}

Notice that `wc` includes a row for the total line numbers for all the files. This can be a useful statistic.

Let's save this result to a file so we can do some further processing on it. At the end of a command, you can use a *redirection*. Normally the shell will direct the output of a program to the terminal (so it can be displayed on the screen). A redirection tells the shell to send the output of the program somewhere else, like a file. It uses the ">" character.

~~~
$ wc -l email_summaries/received/* > received_counts.txt
~~~
{: .bash}

There is also the ">>" redirection. It will save any new output to the end of the file. ">" will wipe the file first, before adding new output. So if you use ">", be sure you don't need the contents of the file that is about to be overwritten.

## Sorting things out

We want to sort the emails to see who has contacted Dr Gill the most. We can use the `sort` command. It takes one argument, a filename of a file to be sorted.Let's try it.

~~~
$ sort received_counts.txt
~~~
{: .bash}

Well that's peculiar. It's sorted them alphabetically, not numerically. We need to give an extra argument `-n` to tell sort to sort the first thing on each line numerically.

~~~
$ sort -n received_counts.txt
~~~
{: .bash}

That's great.

## Pipes

Now the power of the unix shell will come into play. We had stored our results from the `wc` command in an intermediate file before running `sort`. The unix shell has a concept known as a pipe that allows you to take the output from one command and feed into another.

Many of the commands that we've discussed including `sort` normally require at least file as an argument. However, if we "pipe" output from another program, we don't need to give any files as an argument.

The pipe approach simply involves putting a "|" character between programs when running them. For instance, to combine `wc` and `sort` we do the following.

~~~
$ wc -l email_summaries/received/* | sort -n
~~~
{: .bash}

## Exercise

Can you find out who Dr Gibbs emailed the most? Try looking in the sent folder. First trying using an intermediate file (i.e. use `wc` and save it to a file). Then try using a pipe.

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
> With an intermediate file it would be:
> ~~~
> $ wc -l email_summaries/received/* > sent_counts.txt
> $ sort -n sent_counts.txt
> ~~~
{: .bash}
>
> And with a pipe it would be:
>
> ~~~
> $ wc -l email_summaries/received/* | sort -n
> ~~~
> {: .bash}
{: .solution}



