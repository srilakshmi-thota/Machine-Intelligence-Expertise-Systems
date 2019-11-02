__Libraries used:__ \
->scipy.io for loading the data from .mat files\
->matplotlib.pyplot for plotting the roc curve\
->numpy for calculating the area under the curve

__Inputs:__\
actual.mat  :data file containning the actuals labels \
predicted.mat :data file containning classifier's output(in a range of [0,1])

__Outputs:__\
->Plot displaying the ROC_CURVE\
->AUC(the area under the ROC_CURVE is printed

__User defined functions:__\
__1.confusion_metrics__\
Inputs : labels,predictions,threshold\
Ouputs : tpf,fpf\
This function essentially compares the labels(actual values)  and checks whether the predictions(classifier output) is satisfying the condition of threshold and accordingly updates the values of true_positive,false_positive,true_negative,false_negative.


__tpf__ = true_positive / (true_positive + false_negative)\
__fpf__ = false_positive / (false_positive + true_negative)

__2.results__\
Inputs:labels,predictions\
Outputs:Plot displaying the ROC_CURVE,Printing the AUC value\
This function takes the labels and the predictions and calls the confusion metrics function for all the values of thresholds ranging from 0 to 1 by increementing by a step size of 0.0002.And finally plots the ROC_curve by plotting tpf along Yaxis and fpf along Xaxis.\
Uses the trapz function from numpy library to calculate the area by integrating along the given axis using the composite trapezoidal rule.
