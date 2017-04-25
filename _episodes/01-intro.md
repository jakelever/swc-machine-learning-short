---
title: "Introducing the Shell Adventure"
teaching: 5
exercises: 0
questions:
- "What is a command shell and why would I use one?"
objectives:
- "Explain how the shell relates to the keyboard, the screen, the operating system, and users' programs."
- "Explain when and why command-line interfaces should be used instead of graphical interfaces."
keypoints:
- "A shell is a program whose primary purpose is to read commands and run other programs."
- "The shell's main advantages are its high action-to-keystroke ratio, its support for automating repetitive tasks, and its capacity to access networked machines."
- "The shell's main disadvantages are its primarily textual nature and how cryptic its commands and operation can be."
---

A computer program does three main things:
- Takes input from the user
- Does something with the input (i.e. processes it)
- Display the results to the user

Today, we're going to learn about the unix shell. To many, it's the classic image of older computers. There are no images or icons, just text on a black screen.

![Unix Shell Example](https://upload.wikimedia.org/wikipedia/commons/b/bf/Version_7_UNIX_SIMH_PDP11_Kernels_Shell.png)

The unix shell is just another program. It is used to run other programs. The input it takes is what program to run, and the output it gives is the results of the program. One of the advantages of the shell is that typing the commands is much faster than clicking through various menus (that is once you know the commands).

## The Story Begins

You are all digitial forensics specialists and have been given a new high profile case. The acclaimed scientist, Richard Gill, has gone missing. You have been tasked with investigating his laptop contents and research files to find any clues that may explain his disappearance.

![Police Line Image](https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/Police_Line_Crime_Scene_2498847226.jpg/640px-Police_Line_Crime_Scene_2498847226.jpg)
[Source](https://commons.wikimedia.org/wiki/File:Police_Line_Crime_Scene_2498847226.jpg)

### Details

Dr Gill was last seen working late in his office at Sandford Biotechnologies on the evening of April 12th. His wife reported him missing the next morning when she found he hadn't returned from work. His car is missing. No activity has been found on his bank accounts since his disappearance.

### Who is Richard Gill?

Dr Gill is director of research at Sandford Biotechnologies. After a distinguished research career in academia, he moved into industry and has been leading the drug development team at Sandford. He was known to be working on a project codenamed GIBSON.

### What is Sandford Biotechnologies?

Sandford Biotechnologies is a research company that focuses on developing therapeutics for a variety of human diseases.

### What files do we have?

We have his emails, his bank statements and his research files.
