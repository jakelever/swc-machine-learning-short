---
title: "The Decrypted Truth"
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

It's rather strange that the only email from Martin Bishop arrives on the day that Dr Gill was last seen.

Let's see what it says.

~~~
$ cat emails/04_02_2017/RECEIVED_FROM_Martin_Bishop.08_23AM.txt
~~~
{: .bash}

Oh dear, it seems to be encrypted. Luckily we have a decrypting script. But if only we had the password

## The Decrypting Script

The forensic tools contain a script for decrypting emails. Unfortunately it only works for the emails in this workshop.

Let's see how it works.

~~~
$ sh tools/decrypt.sh
~~~
{: .bash}

It suggests that we try it out on a test file. Let's look at the test file.

~~~
$ cat tools/encrypted_file.txt
~~~
{: .bash}
~~~
ENCRYPTED
PBZOBQ
Vxv, vlr'sb abzovmqba qefp cfib. Zlkdoxqrixqflkp!
~~~
{: .output}

Yep, definitely encrypted. Note, that actual encrypted files don't look like this. But isn't this fun!


And if we try decrypting with the wrong password.

~~~
$ sh tools/decrypt.sh WRONG tools/encrypted_file.txt
~~~
{: .bash}

However the correct password works.
~~~
$ sh tools/decrypt.sh SECRET tools/encrypted_file.txt
~~~
{: .bash}

## Variables

We're going to introduce the concept of variables in the Unix Shell. These are placeholders to store information that are useful for running commands. For instance, we could store the word "SECRET" in the variable "password". To do this, we do the following:

~~~
$ password=SECRET
~~~
{: .bash}

When we store a value to a variable, we use the format above with an equals sign and no spaces either side (that's important). When we then want to use the variable, we put a dollar sign in front of it. For example:

~~~
$ sh tools/decrypt.sh $password tools/encrypted_file.txt
~~~
{: .bash}

> ### Lifetime of a Variable
>
> Variables live within an individual Unix shell session. If you close it, you'll lose those variables that you've set. And if you have another unix shell open, you won't be able to access those variables in that shell.
{: .callout}

## Echo

`echo` is a simple command displays its arguments to the screen.

~~~
$ echo "Hello"
~~~
{: .bash}

We can get it to print out variable names.

~~~
$ echo $password
~~~
{: .bash}

Variables can be used anywhere in the Unix shell. Their name will be replaced with their value (i.e. $password becomes SECRET) before the command is run.

## Loops

Loops allow us to run the same bit of code, but using a different value for our variable each time. Let's show this with echo.

The format for a loop is below. This is called a `for` loop. The variable name in the loop is animal (but it can be anything, as long as you are consistent). And it look loop four times, once for each of the animals. It will do everything between `do` and `done` five times. 

Try typing it in. Notice that after pressing Enter after the first line that the terminal '$' changes to '>'. This means that the terminal knows there is more to this command. It'll keep allowing you to enter the command until you enter `done` (or make a mistake).

~~~
$ for animal in "cat" "dog" "fish" "elephant"
> do
> echo $animal
> done
~~~
{: .bash}
~~~
cat
dog
fish
elephant
~~~
{: .output}

## Loops and Files

You can also use a loop to iterate over files using the wildcard operator.

~~~
$ for file in email_summaries/received/*
> do
> wc -l $file
> done
~~~
{: .bash}

## Email Decryption

~~~
$ sh tools/decrypt.sh SECRET emails/04_02_2017/RECEIVED_FROM_Martin_Bishop.08_23AM.txt
~~~
{: .bash}

Unfortunately that didn't work.

## Exercise

As digital forensic experts, we know that the five most common passwords are:

1. 123456
2. password
3. shadow
4. dragon
5. qwerty

These are real common passwords, though not exactly the top five (source: [SplashData](http://splashdata.blogspot.ca).)

Can you write a loop that will try each of them to decrypt the email?

> ## Solution
>
> ~~~
> $ for password in "123456" "password" "shadow" "dragon" "qwerty"
> $ do
> $ sh tools/decrypt.sh $password emails/04_02_2017/RECEIVED_FROM_Martin_Bishop.08_23AM.txt
> $ done
> ~~~
> {: .bash}
>
{: .solution}

