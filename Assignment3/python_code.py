from scipy.io import loadmat
import matplotlib.pyplot as plt
from scipy.integrate import simps
import numpy as np

actual=loadmat('actual.mat');
predicted=loadmat('predicted.mat');
labels=actual['target'][:,0];
predictions=predicted['neuralOut'][:,0]; 

TPF=[]
FPF=[]

def roc_curve(labels, predictions, sample_weight):
    sig_weights = sample_weight * (labels == 1)
    bck_weights = sample_weight * (labels == 0)
    thresholds, predictions = np.unique(predictions, return_inverse=True)
    tpr = np.bincount(predictions, weights=sig_weights)[::-1].cumsum()
    fpr = np.bincount(predictions, weights=bck_weights)[::-1].cumsum()
    tpr /= tpr[-1]
    fpr /= fpr[-1]
    return fpr, tpr;



fpr,tpr=roc_curve(labels,predictions,0.5);

   

        
plt.plot(fpr,tpr);
plt.xlabel(" (FPF)--->")
plt.ylabel(" (TPF)--->")
plt.title("ROC Curve")
plt.show()
area = np.trapz(tpr, dx=0.05)
print("AUC is", area)

           



    

    
            
        
        

