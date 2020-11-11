---
title: "Data"
teaching: 20
exercises: 10
questions:
- "How do I load data?"
- "How do I triage data?"
objectives:
- "Refresh on working with data in NumPy."
keypoints:
- "Good data is the key to success in machine learning"
- "More data allows for more complicated machine learning."
- "You will (and should) spend most of your time checking and cleaning up data."
---

The most challenging part of machine learning is getting good data, and enough of it. The more complex the machine learning method, the more data you need. Data can be continious (e.g. heights of patients), binary (e.g. wears glasses or not) or categorical (e.g. ). You may have a target variable, e.g. a field which you would like to predict for new data samples. This could be whether a patient has a disease, whether an image is a cat, etc. You may not have a target variable, and want to explore the data.

### The data set

We are going to use a simulated dataset of patients with the fictional disease Mumblemumps. The dataset contains measurements for 500 patients along with a disease status. The dataset can be viewed at <https://github.com/jakelever/swc-machine-learning-short/blob/gh-pages/data/dataset.tsv>.

### Loading data

We're going to load the data directly from the Github repo using numpy. The dataset is accessible in raw form at <https://raw.githubusercontent.com/jakelever/swc-machine-learning-short/gh-pages/data/dataset.tsv>.

~~~
import numpy
dataset = numpy.loadtxt('https://raw.githubusercontent.com/jakelever/swc-machine-learning-short/gh-pages/data/dataset.tsv',skiprows=1)
~~~
{: .language-python}

We can use **type** to get the type of the object that we know have.

~~~
print(type(dataset))
~~~
{: .language-python}

This is a numpy array, which is essentially a matrix with a lot of nice functions to help calculate statistics on them. First we should check how much data we have.

~~~
print(dataset.shape)
~~~
{: .language-python}

So that gives us the number of rows (first) and columns (second).

### Exploring data

We can access a specific value in the matrix using the square brackets. Numpy uses indices that start at zero. So the first row is indexed with zero. Hence to get the value in the 4th row (index=3) and 3rd column (index=2), we use the code below.

~~~
print(dataset[3,2])
~~~
{: .language-python}

We can use colons to create row and column ranges. For instance, if we wanted the first five rows with all the columns, we could use the line below.

~~~
print(dataset[:5,:])
~~~
{: .language-python}

So we have 10 features for each of the 500 patients. We want to split off one feature that is the disease status. And we want to use the other 9 features to try to make predictions. The code below does a slice of the diabetes_set matrix. The colon on its own asks for every row.

~~~
target = dataset[:,9]
features = dataset[:,0:9]
~~~
{: .language-python}

What are these 9 features? The names are in the file and are added below for simplicity.

| Column Index | Feature                |
|--------------|------------------------|
| 0            | Age                    |
| 1            | Sex                    |
| 2            | Height                 |
| 3            | Weight                 |
| 4            | Blood Marker A         |
| 5            | Blood Marker B         |
| 6            | Blood Marker C         |
| 7            | Blood Marker D         |
| 8            | Blood Marker E         |

The Has_Disease column has been stored into target. This is the column that we want to learn to predict, so that we can help diagnose patients with Mumblemumps.

### Triaging data

It's always a good idea to look into your data to get an idea for the ranges of the data, the types of data, etc. There may be errors in your data and you want to know this before you start using erroneous data in a machine learning system.

Numpy provides a few functions for simple statistics like minimums, maximums and averages. To calculate the minimum of the first column, we could use the command below.

~~~
print(features[:,0].min())
~~~
{: .language-python}

But it'd take a little bit of time to do that for each column for minimum, maximum and any other statistics we might want. Instead, we can do it for all the columns at the same time using all the features and the axis parameter. The axis parameter instructs Numpy to calculate the statistic for each element in the row (for axis=0). We can get a number of statistics using the lines below.

~~~
print(features.min(axis=0))
~~~

> ## Min, max and mean
> 
> Calculate the minimum, mean and maximum for each column.
> 
> > ## Solution
> > ~~~
> > print(features.min(axis=0))
> > print(features.mean(axis=0))
> > print(features.max(axis=0))
> > ~~~
> > {: .language-python}
>{: .solution}
> 
> How about the minimum of each row?
>
> > ## Solution
> > ~~~
> > print(features.min(axis=1))
> > ~~~
> > {: .language-python}
>{: .solution}
{: .challenge}

It looks like the second column for sex is represented by 1s and 2s. It is a categorical variable. We can leave it with that representation as there are only two values. An alternative representation would be to have a IsMale column and IsFemale column. This isn't need as there are just two categories in this column, but would be if there were more than two.

Another important factor when examining data is to consider the class balance. How common is the target variable? If it is a disease, how common is the disease? If it is extremely rare, then the machine learning system will not do well unless there is a huge amount of data. Let's calculate the class balance for this data set. We can use the sum function below as target contains True/False values, so sum will indicate the number of True values.

~~~
posCount = target.sum()
N = target.shape[0]
classBalance = 100 * posCount / N
print(posCount,N)
print(classBalance)
~~~
{: .language-python}

### Principal Component Analysis (PCA)

You should try to graph your data in different ways to understand the different values and see if there are any oddities to the data. One method is to calculate the principal components of the dataset. The principal components are the main axes of variance through the data. For instance, if the patients age was really the only thing that varied between the samples and the other variables changed only slightly, then the first principal component would be the age. However in the most cases, the first principal component will be a combination of multiple columns. PCA is a very powerful method but does have many limitations. There is suggested reading at the bottom.

Let's do a principal component analysis using scikit-learn. We first import the PCA method from scikit-learn, create an instance asking for two principal components, then fit and transform our data. It will now have the same number of samples but only two columns. Think of this as a compressed version of our previous data.

~~~
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
pca.fit(features)
transformed = pca.transform(features)
print(transformed.shape)
~~~
{: .language-python}

And now we will plot this data on a 2d scatter plot. The reason to do this is to see if there are any obvious clusters and outliers.

~~~
import matplotlib.pyplot as plt
plt.scatter(transformed[:,0], transformed[:,1])
plt.title('PCA of all data')
plt.xlabel('PCA 1')
plt.ylabel('PCA 2')
plt.show()
~~~
{: .language-python}

Most of the data clumps into one cluster with some data points around the edge, but none of them are extreme outliers.

### Splitting data

For machine learning, we want to have part of the data used for learning a pattern (training), a second part for helping to decide which pattern to use (validation) and a final part kept separate for our final evaluations. This is know as a training / validation / testing data split. We're going to use one of the helper functions that scikit-learn provides to do this step. It will randomly assign 80% of the data to the training/validation set, and 20% to the testing set. We then run it again to split up the training and validation sets. To get the same results as others, use the random_seed=0 parameter to get the same random distribution of samples.

~~~
from sklearn.model_selection import train_test_split
features_train, features_test, target_train, target_test = train_test_split(features, target, test_size=0.2, random_state=0)
features_train, features_validation, target_train, target_validation = train_test_split(features_train, target_train, test_size=0.2, random_state=0)

print(features_train.shape)
print(features_validation.shape)
print(features_test.shape)
print(target_train.shape)
print(target_validation.shape)
print(target_test.shape)

N_train = target_train.shape[0]
N_validation = target_validation.shape[0]
N_test = target_test.shape[0]
~~~
{: .language-python}
