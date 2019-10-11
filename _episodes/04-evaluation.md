---
title: "Evaluation"
teaching: 15
exercises: 0
questions:
- "How can I tell if my classifier is good?"
objectives:
- "Understand what a confusion matrix is"
- "Learn about the different metrics "
keypoints:
- "A confusion matrix shows the counts of the true positives, false positives, true negatives and false negatives that the classifier gives."
- "Various statistics can be calculate from these four numbers. The statistic to use depends on what errors you want to minimize."
- "Further reading: [Points of Significance: Classification Evaluation](https://www.nature.com/articles/nmeth.3945)"
---

Below is a refresher of the code we've been using to classify the data.

~~~
from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(random_state=0)

clf.fit(features_train,target_train)

pred_test = clf.predict(features_test)
print(calcAccuracy(target_test,pred_test))
~~~
{: .language-python}

#### True positives, etc

To calculate different performance metrics, we want to know where the classifier is succeeding and failing. The successes are charactered by **true positives** and **true negatives**. The failures are characterized by **false positives** and **false negatives**. Let's calculate the number of true positives.

~~~
true_positives = 0

for i in range(N_test):
  if target_test[i] == True and pred_test[i] == True:
    true_positives += 1

print(true_positives)
~~~
{: .language-python}

Now as an exercise, calculate the other three counts: true negatives, false positives and false negatives.

> ## Solution
> 
> ~~~
> true_positives = 0
> true_negatives = 0
> false_positives = 0
> false_negatives = 0
> 
> for i in range(N_test):
>   if target_test[i] == True and pred_test[i] == True:
>     true_positives += 1
>   if target_test[i] == False and pred_test[i] == True:
>     false_positives += 1
>   if target_test[i] == True and pred_test[i] == False:
>     false_negatives += 1
>   if target_test[i] == False and pred_test[i] == False:
>     true_negatives += 1
>     
> print(true_positives,true_negatives,false_positives,false_negatives)
> ~~~
> {: .language-python}
> 
{: .solution}

#### Metrics

With those four counts, you can calculate a variety of different metrics. These four counts make up the **confusion matrix**. For a binary classification problem (i.e. predicting positive/negative), it is a 2x2 grid. The [Wikipedia article](https://en.wikipedia.org/wiki/Confusion_matrix) gives a nice overview of the different metrics that you can calculate with these numbers. We calculate a few of the popular metrics below. All these metrics vary between 0 and 1 with higher meaning better performance.

~~~
accuracy = (true_positives + true_negatives) / (true_positives + true_negatives + false_positives + false_negatives)
precision = true_positives / (true_positives + false_positives)
recall = true_positives / (true_positives + false_negatives)
print(accuracy, precision, recall)
print(f1score)
~~~
{: .language-python}

You should really consult more than one metric to decide if your classifier is succesful. However, many use the F1-score as their main focus. It is the harmonic mean of the precision and recall scores.
~~~
f1score = 2 * (precision * recall) / (precision + recall)
print(f1score)
~~~
{: .language-python}

#### Using scikit-learn from metrics

You don't need to code this all manually next time. Scikit-learn provides a [number of functions for calculating classifier performance metrics](https://scikit-learn.org/stable/modules/classes.html#classification-metrics). We use several below, including one to calculate the confusion matrix itself. Note that the four counts are the same as we calculated previously.

~~~
from sklearn.metrics import confusion_matrix
print(confusion_matrix(target_test,pred_test))

from sklearn.metrics import accuracy_score, f1_score, recall_score, precision_score

print(accuracy_score(target_test,pred_test))
print(precision_score(target_test,pred_test))
print(recall_score(target_test,pred_test))
print(f1_score(target_test,pred_test))
~~~
{: .language-python}






> ## Generate Composite Statistics
>
> Use each of the files once to generate a dataset containing values averaged over all patients:
>
> ~~~
> filenames = glob.glob('inflammation*.csv')
> composite_data = numpy.zeros((60,40))
> for f in filenames:
>     # sum each new file's data into composite_data as it's read
>     #
> # and then divide the composite_data by number of samples
> composite_data /= len(filenames)
> ~~~
> {: .language-python}
>
> Then use pyplot to generate average, max, and min for all patients.
>
> > ## Solution
> > ~~~
> > import glob
> > import numpy
> > import matplotlib.pyplot
> >
> > filenames = glob.glob('inflammation*.csv')
> > composite_data = numpy.zeros((60,40))
> >
> > for f in filenames:
> >     data = numpy.loadtxt(fname = f, delimiter=',')
> >     composite_data += data
> >
> > composite_data/=len(filenames)
> >
> > fig = matplotlib.pyplot.figure(figsize=(10.0, 3.0))
> >
> > axes1 = fig.add_subplot(1, 3, 1)
> > axes2 = fig.add_subplot(1, 3, 2)
> > axes3 = fig.add_subplot(1, 3, 3)
> >
> > axes1.set_ylabel('average')
> > axes1.plot(numpy.mean(composite_data, axis=0))
> >
> > axes2.set_ylabel('max')
> > axes2.plot(numpy.max(composite_data, axis=0))
> >
> > axes3.set_ylabel('min')
> > axes3.plot(numpy.min(composite_data, axis=0))
> >
> > fig.tight_layout()
> >
> > matplotlib.pyplot.show()
> > ~~~
> > {: .language-python}
>{: .solution}
{: .challenge}


