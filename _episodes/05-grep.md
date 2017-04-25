---
title: "Contacts"
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

So he has been receiving substantial money from Bishop Industries and has sent many emails to a Martin Bishop. It'd be great if we knew more about Martin Bishop.

Let's find out who Martin Bishop is. We're going to look for information in Dr Gill's contact book.

~~~
$ cat contacts.txt
~~~
{: .bash}

Oh dear, it's rather large. However it does have information against everyone's name. The first column is their name, the second is their company, the third is the position at the company and the fourth is their location.

# Searching within a file

To search within a file, we use the `grep` command. It stands for the less catchy: "global regular expression print". It is however one of the most invaluable tools in the Unix shell.

`grep` takes two arguments as standard: the search term and the file to search. It will find and print out every line in the file that contains the pattern. 

Let's search the address book for contacts based in Bolivia. Notice that quotation marks are used around the word "bolivia" in the command.

~~~
$ grep "bolivia" contacts.txt
~~~
{: .bash}

Hmm, it didn't find anything. `grep` is case-sensitive by default. To make it case-insensitive, use the `-i` argument.

~~~
$ grep -i "bolivia" contacts.txt
~~~
{: .bash}

Excellent.

## The Power of Grep

Grep has so many arguments. Let's just mention `-v`. It inverts the search query, so will print any line that doesn't contain the search query. For instance, the command below will print out every line that doesn't contain the letter "n".

~~~
$ grep -v n contacts.txt
~~~
{: .bash}

## Piping Grep

Grep is another command that can have data piped into it. Let's try using grep twice. Can we find a contact of Dr Gill's that lives in Belgium and works for Reducto Services.

~~~
$ grep "Belgium" contacts.txt | grep "Reducto Services"
~~~
{: .bash}

## Exercise

Find out who Martin Bishop is using `grep` and the contacts.tsv file.

> ## Solution
>
> ~~~
> $ grep "Martin Bishop" contacts.tsv
> ~~~
> {: .bash}
>
{: .solution}

## Bonus Points

- Find the contacts entry that lives in Singapore, has an "m" in their entry but not a "u".
