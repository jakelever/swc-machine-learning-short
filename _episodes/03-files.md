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
- "The shell does not have a trash bin: once something is deleted, it's really gone."
---

## Bank statements

Let's look into Dr Gill's finances. We can look into his bank statements. Try using tab-complete for this.

~~~
$ ls bank_statements/
~~~
{: .bash}

Wow, Dr Gill had a lot of bank accounts. Each file is a set of transactions in one bank account.

~~~
cat bank_statements/ACCNO_00497405_statement.txt
~~~
{: .bash}

Unfortunately a quick check of one of the statement files doesn't tell us anything. We'll need to use one of our forensics tools.

## Tools

Let's see what tools we have.

~~~
$ ls tools
~~~
{: .bash}

## The `sh` command

Typing everything again and again gets tiring. So a good idea is to save a series of shell commands to a script. By convention, we name the script with ".sh" at the end. And then we run the file using the `sh` command.

> ## Filename suffixes
>
> Suffixes like `.sh` or `.txt` are purely by convention. They don't hold special meaning to the computer, but it's an excellent idea to use these suffixes to help others understand what type of file something is.
{: .callout}

Let's look at the `display_project_summaries.sh` script in the tools directory.

~~~
$ cat tools/display_project_summaries.sh
~~~
{: .bash}

~~~
# Displays the summary of various projects
cat research_files/project_gibson/summary.txt
cat research_files/project_arcturus/summary.txt
cat research_files/project_columbia/summary.txt
cat research_files/project_asimov/summary.txt
cat research_files/project_titan/summary.txt
cat research_files/project_smith/summary.txt
~~~
{: .output}

This script is just a series of `cat` commands. Let's try running it.

~~~
$ sh tools/display_project_summaries.sh
~~~
{: .bash}

> ## Comments in code
>
> Did you see the first line of the display_project_summaries.sh script? It started with a '#'. This signifies that this is a comment and not a command that should be run. Comments are a good idea as they help someone else (or you in six months) understand what a script does.
{: .callout}

## Financial Summaries

Let's find out about the finance_summary.sh script. The code for it is a lot more complicated than `display_project_summaries.sh` so we're not going to look at it using `cat`.

What happens if we run it?

~~~
$ sh tools/finance_summary.sh
~~~
{: .bash}

~~~
ERROR: Could not find statements/ directory
~~~
{: .output}

Okay, that wasn't very helpful. let's try the --help argument.

~~~
$ sh tools/finance_summary.sh --help
~~~
{: .bash}

~~~
This tool summaries financial statements. It expects a directory called 'tmp_statements' in the current directory. The statements folder should contain a series of statement files. And it will output the results to the file 'finance_results'
~~~
{: .output}

This script wants a directory called 'tmp_statements' with the statements that we want in it.

## Moving data

First thing we need to do is make the statements directory. For that we use `mkdir` which stands for "make directory". The one argument to it is the name of the directory.

~~~
$ mkdir tmp_statements
~~~
{: .bash}

Using `ls`, we can see that a directory has been made.

~~~
$ ls
~~~
{: .bash}
~~~
bank_statements  contacts.txt  emails  email_summaries  README.md  research_files  tmp_statements  tools
~~~
{: .output}

Then we need to copy one of the account statements into the statements directory. For that we will use `cp` which stands for "copy". It takes two or more arguments. The final argument is the destination to copy to. And the remaining ones are the files to copy.

~~~
$ cp bank_statements/ACCNO_00497405_statement.txt tmp_statements/
~~~
{: .bash}

We can check the contents of 'tmp_statements' and see that the file has been copied there.

~~~
$ ls tmp_statements/
~~~
{: .bash}
~~~
ACCNO_00497405_statement.txt
~~~
{: .output}

If we check the bank_statements folder, we'll see that it hasn't be removed.

~~~
$ ls bank_statements/
~~~
{: .bash}

## Starting the Analysis

Let's try the script again.

~~~
$ sh tools/finance_summary.sh
~~~
{: .bash}
~~~
Summary saved to finance_results.txt using 1 statement(s) from the following account(s):
ACCNO_00497405
~~~
{: .output}

Yay, it worked this time. We can look at the finance_results file using `cat`.

~~~
$ cat finance_results.txt
~~~

Nothing obvious there.

## Let's try a few bank accounts

First we're going to delete the statements from tmp_statements. We're going to use the `rm` command. It stands for "remove". It can take multiple filenames as arguments (or just one) and will try to delete each one.

~~~
$ rm tmp_statements/ACCNO_00497405_statement.txt
~~~
{: .bash}

> ## Care Required
>
> If `rm` deletes a file, there is no way to recover it. The unix shell does not have the equivalent of the recycle bin. So be careful!
{: .callout}

An `ls` of the tmp_statements directory shows an empty directory.

~~~
$ ls tmp_statements/
~~~
{: .bash}

> ## Deleting directories
>
> The `rm` command cannot normally delete directories. For that there is the `rmdir` command. However the directory has to be empty for that. To make `rm` delete a directory will files in it, you would use `rm -r`. But be very careful with this! A safer way is `rm -ir` which will check with you before deleting each file.
{: .callout}

Let's copy two bank statements this time. We can use the cp command and provide two files and the destination directory.

~~~
$ cp bank_statements/ACCNO_00497405_statement.txt bank_statements/ACCNO_00885279_statement.txt tmp_statements/
~~~
{: .bash}

> ## Wildcards
>
> We can use the wildcard '*' to select multiple files. For instance bank_statements/ACCNO_00* could be used instead of explicitly naming the two files in the command above. The `cp` command below shows what that would look like.
> ~~~
> $ cp bank_statements/ACCNO_00* tmp_statements/
> ~~~
> {: .bash}
> The wildcard doesn't have to come at the end of the filename. For instance the command below, will give every statement with a bank account number ending in 0.
> ~~~
> $ ls tmp_statements/*0_statement.txt
> ~~~
> {: .bash}
{: .callout}

And run the analysis.

~~~
$ sh tools/finance_summary.sh
~~~
{: .bash}

Oh no! It won't work if there is a file called `finance_results.txt`. Let's move it.

To move a file or directory we use the `mv` command. It works similarly to `cp` except that the original file won't be there after the command is run.

~~~
$ mv finance_results.txt old_results.txt
~~~
{: .bash}

Let's try the command again.

~~~
$ sh tools/finance_summary.sh
~~~
{: .bash}

Great it worked. 

## Top and Bottom of a File

Let's have a look at the financials and see if anything sticks out.

~~~
$ cat finance_results.txt
~~~
{: .bash}

Hmm, the output is getting a little long. We should use the `head` command to get the first 10 lines of the file.

~~~
$ head finance_results.txt
~~~
{: .bash}

That's better. But there's nothing obvious here.

## Clearing out files

Let's use the wildcard to clear out the tmp_statements directory.

~~~
$ rm tmp_statements/*
~~~
{: .bash}

## Exercise
Can you calculate a summary for all the accounts together? Does anything stick out?

Don't forget to move or delete the finance_results.txt file.

> ## Solution
>
> ~~~
> $ cp bank_statements/* tmp_statements/
> $ sh tools/finance_summary.sh
> ~~~
> {: .bash}
>
{: .solution}

## Bonus Points

- What happens if you move to tools directory (using `cd`) and run the `display_project_summaries.sh` script using the `sh` command?
- Feeling adventurous? Have a look at the `finance_summary.sh` code with `cat`. Looks a bit scary, yeah? See if you can figure out the logic of any piece of it.
