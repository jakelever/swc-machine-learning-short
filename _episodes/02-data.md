---
title: "Data"
teaching: 15
exercises: 0
questions:
- "How can I move around on my computer?"
objectives:
- "Explain the similarities and differences between a file and a directory."
keypoints:
- "The file system is responsible for managing information on the disk."
---

The most challenging part of machine learning is getting good data, and enough of it. The more complex the machine learning method, the more data you need. Data can be continious (e.g. heights of patients), binary (e.g. wears glasses or not) or categorical (e.g. ). You may have a target variable, e.g. a field which you would like to predict for new data samples. This could be whether a patient has a disease, whether an image is a cat, etc. You may not have a target variable, and want to explore the data.

### The data set

Scikit-learn comes with several example data sets. We are going to use a dataset of diabetes patients, originally published in 2004. The dataset contains measurements for 442 patients along with a disease measure.

### Loading data

We're going to load the data directly from a website using numpy. The dataset is accessible at <https://www4.stat.ncsu.edu/~boos/var.select/diabetes.tab.txt>

~~~
import numpy
diabetes_set = numpy.loadtxt('https://www4.stat.ncsu.edu/~boos/var.select/diabetes.tab.txt',skiprows=1)
~~~
{: .language-python}

We can use **type** to get the type of the object that we know have.

~~~
print(type(diabetes_set))
~~~
{: .language-python}

This is a numpy array, which is essentially a matrix with a lot of nice functions to help calculate statistics on them. First we should check how much data we have.

~~~
print(diabetes_set.shape)
~~~
{: .language-python}

We can access a specific value in the matrix using the square brackets. Python, and numpy, uses indices that start at zero. So the first row is indexed with zero. Hence to get the value in the 4th column of the 3rd row, we use the code below.

~~~
print(diabetes_set[3,2])
~~~
{: .language-python}

So we have 11 features for each of the 442 patients. We want to split off one feature that is the disease measure. And we want to use the other 10 features to try to make predictions. The code below does a slice of the diabetes_set matrix. The colon on its own asks for every row.

~~~
disease_measure = diabetes_set[:,10]
features = diabetes_set[:,0:10]
~~~
{: .language-python}

What are these 10 features? The names are in the file and are added below for simplicity.

| Column Index | Feature                |
|--------------|------------------------|
| 0            | Age                    |
| 1            | Sex                    |
| 2            | Body mass index        |
| 3            | Average blood pressure |
| 4            | S1                     |
| 5            | S2                     |
| 6            | S3                     |
| 7            | S4                     |
| 8            | S5                     |
| 9            | S6                     |

For this lesson, we are going to make a binary variable to predict, with a True or False value. We will threshold the disease_measure with a value to create a target variable which represents whether the disease progressed beyond a certain point. TODO: EXplain MORE?

~~~
target = disease_measure > 200
~~~
{: .language-python}

### Exploring data

Some min,maxes might be a good idea

### Triaging data

Could we do some plots perhaps?

### Splitting data

Into training and test to begin with!
