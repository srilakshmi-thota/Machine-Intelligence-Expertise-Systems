Libraries used:
->scipy.io for loading the data from .mat files
->matplotlib.pyplot for plotting the roc curve
->numpy for calculating the area under the curve


Inputs:
->actual.mat  :data file containning the actuals labels 
->predicted.mat  :data file containning classifier's output(in a range of [0,1])


Outputs:
->Plot displaying the ROC_CURVE
->AUC(the area under the ROC_CURVE is printed


User defined functions:
1.confusion_metrics
->Inputs:labels,predictions,threshold
->Ouputs:tpf,fpf
->This function essentially compares the labels(actual values)  and checks whether the predictions(classifier output) is satisfying the condition of threshold and accordingly updates the values of true_positive,false_positive,true_negative,false_negative.
Pseudo code:
if(labels[i]=1):
          if predictions[i]>=threshold:
               true_positive++;
          else:
               false_negative++;
else:
         if predictions[i]>=threshold:
               flase_positive++;
          else:
               true_negative++;
tpf = true_positive / (true_positive + false_negative);
fpf = false_positive / (false_positive + true_negative);

2.results
->Inputs:labels,predictions
->Outputs:Plot displaying the ROC_CURVE,Printing the AUC value
->This function takes the labels and the predictions and calls the confusion metrics function for all the values of thresholds ranging from 0 to 1 by increementing by a step size of 0.0002.And finally plots the ROC_curve by plotting tpf along Yaxis and fpf along Xaxis.
->Uses the trapz function from numpy library to calculate the area by integrating along the given axis using the composite trapezoidal rule.

Results file:
->Contains the Ipython console displaying the ROC_CURVE plot and the value of AUC 

P.s:The python code is included in the python_code file.



   