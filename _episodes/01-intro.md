---
title: "Introduction"
teaching: 5
exercises: 0
questions:
- "What is machine learning? And what is AI? How does statistics fit into this?"
- "What is Google Colab?"
objectives:
- "Explain the relationship between machine learning, artificial intelligence and statistics."
- "Explain supervised versus unsupervisied machine learning."
- "Start up a Google Colab notebook"
keypoints:
- "Machine learning and artificial intelligence have recently come to mean similar things. Often machine learning is the task of using data to achieve a goal. Statistics is the related field focussed on gaining understanding from data."
- "Google Colab allows you to run Python code online."
---

## Getting started

### What is machine learning?

Machine learning covers many different methods:

### Machine learning versus statistics

INSERT STATISTICS to MACHINE LEARNING 

### Where does deep learning fit into this?

## Google Colab

We will use Google Colab for this workshop. It is an online notebook which can run Python code and is like Jupyter Notebook, but completely online. If you have a Google account, you can access it at <https://colab.research.google.com>.

Let's get started with it and create a new notebook. Select New Python 3 notebook from the Welcome page, or select File -> "New Python 3 notebook"

INSERT SCREENSHOT

Then rename it at the top and give it a memorable name.

INSERT SCREENSHOT

To get back to this notebook later, you can find it in the "Colab Notebooks" directory in your Google Drive.

INSERT SCREENSHOT?

> ## Python 2 versus Python 3
> For many years, Python has had two versions that different people have used, version 2 (v2.7 is the latest) and version 3, currently (v3.7 is the latest). There are small but key differences between the two. However, v2 is about to become unsupported and all Python code should now be written in v3. One example of the differences that you may see immediately are shown below with different print statements.
> ~~~
> # This is Python 2
> print "Hello"
>
> # This is Python 3
> print("Hello")
> ~~~
> {: .language-python}
{: .callout}

### Hello World

Let's write a single Python command and then run it.

You can click on the empty cell and add in the print command below.

~~~
print("Hello")
~~~
{: .language-python}

INSERT SCREENSHOT

To run that cell, press Ctrl and Enter together, or select Runtime -> Run the focused cell.

The output from running the code in the cell is shown below.

### Errors

Let's see what an error looks like and introduce a typo.

~~~
pint("Hello")
~~~
{: .language-python}

When we run the cell again (Ctrl+Enter), the error message appears below and can help us diagnose the problem.

SCREENSHOT
