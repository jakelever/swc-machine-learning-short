---
title: "Evaluation"
teaching: 15
exercises: 10
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
clf = RandomForestClassifier(max_depth=2, random_state=0)

clf.fit(features_train,target_train)

pred_validation = clf.predict(features_validation)
print(calcAccuracy(target_validation,pred_validation))
~~~
{: .language-python}

#### True positives, etc

To calculate different performance metrics, we want to know where the classifier is succeeding and failing. The successes are charactered by **true positives** and **true negatives**. The failures are characterized by **false positives** and **false negatives**. Let's calculate the number of true positives.

~~~
true_positives = 0

for i in range(N_validation):
  if target_validation[i] == True and pred_validation[i] == True:
    true_positives += 1

print(true_positives)
~~~
{: .language-python}

Let's calculate the other three counts: true negatives, false positives and false negatives.

> ## Solution
> 
> ~~~
> true_positives = 0
> true_negatives = 0
> false_positives = 0
> false_negatives = 0
> 
> for i in range(N_validation):
>   if target_validation[i] == True and pred_validation[i] == True:
>     true_positives += 1
>   if target_validation[i] == False and pred_validation[i] == True:
>     false_positives += 1
>   if target_validation[i] == True and pred_validation[i] == False:
>     false_negatives += 1
>   if target_validation[i] == False and pred_validation[i] == False:
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
print(confusion_matrix(target_validation,pred_validation))

from sklearn.metrics import accuracy_score, f1_score, recall_score, precision_score

print(accuracy_score(target_validation,pred_validation))
print(precision_score(target_validation,pred_validation))
print(recall_score(target_validation,pred_validation))
print(f1_score(target_validation,pred_validation))
~~~
{: .language-python}

#### Final evaluation using the test set

We've tried a few different models and the Random Forest classifier seems to do quite well, or perhaps you found another one that does better. Let's do a final evaluation using the held-out testing set. These results would be the ones to report in any publications or report. You should only be checking against your test set once.

~~~
# Use the classifier to make the test predictions
pred_test = clf.predict(features_test)

print(accuracy_score(target_test,pred_test))
print(precision_score(target_test,pred_test))
print(recall_score(target_test,pred_test))
print(f1_score(target_test,pred_test))
~~~
{: .language-python}
