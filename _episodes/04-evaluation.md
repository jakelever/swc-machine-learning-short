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

#### Receiver Operating Characteristic (ROC) curves and Area under the Curve (AUC)

A popular visual method to inspect classifier performance is the receiver operating characteristic (ROC) curve. Most classifier methods actually score each sample while making a prediction, with higher scores meaning a positive prediction and lower scores meaning a negative prediction. An ROC curve is a visual representation of this scoring. It shows a curve that runs from bottom-left to top-right and ideally gets as closer as possible to top-right. The curve is monotonic and can't turn back on itself. If a classifier gave the highest scores to all the positive samples, then the curve would quickly shoot up towards the top-left corner before continuing to the right. Anyway, let's calculate the data for it and plot it. We will again use some scikit-learn helper functions.

~~~
from sklearn.svm import LinearSVC
clf = LinearSVC(random_state=0)

clf.fit(features_train,target_train)

scores_test = clf.decision_function(features_test)

from sklearn.metrics import roc_curve,auc
fpr, tpr, _ = roc_curve(target_test, scores_test)
roc_auc = auc(fpr, tpr)
~~~
{: .language-python}

And then plot using matplotlib.

~~~
plt.figure()
plt.plot(fpr, tpr, color='darkorange',
         lw=2, label='ROC curve (area = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic example')
plt.legend(loc="lower right")
plt.show()
~~~
{: .language-python}

Or with plotly:

~~~
import plotly.graph_objects as go

fig = go.Figure(data=go.Scatter(x=fpr, y=tpr, line={'color':'darkorange'}))
fig.update_layout(title='Receiver operating characteristic example',
                  font=dict(family='Arial', size=16),
                  xaxis_title='False Positive Rate',
                  yaxis_title='True Positive Rate',
                  width = 600,
                  height = 500,
                  shapes=[
                      go.layout.Shape(
                          type="line",
                          x0=0,
                          y0=0,
                          x1=1,
                          y1=1,
                          line=dict(color="navy",width=2,dash="dot")
                      )
                  ])
fig.show()
~~~
{: .language-python}
