# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from sklearn.preprocessing import StandardScaler
import operator
from sklearn.neighbors import KNeighborsClassifier



column_names=["variance","skewness","curtosis","entropy","Class"]
data_train=pd.read_csv("train_data_banknote_auth.csv",header=None,names=column_names)
X_train=data_train.values[:,0:4]
y_train=data_train.values[:,4]

data_test=pd.read_csv("test_data_banknote_auth.csv",header=None,names=column_names)
X_test=data_test.values[:,0:4]
y_test=data_test.values[:,4]

vars_list=["variance","skewness","curtosis","entropy"]
sns.pairplot(data_train,hue="Class", height=3, diag_kind="kde",vars=vars_list)
plt.legend(labels=["forged","genuine"])
plt.show(sns)


scaler = StandardScaler()
scaler.fit(X_train)
x_train = scaler.transform(X_train)
x_test = scaler.transform(X_test)

fig, (ax1, ax2) = plt.subplots(ncols=2,figsize=(10,5))
ax1.set_title('Before Scaling')
ax2.set_title('After scaling')
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n Input values before and after Scaling")
label_names=["variance","skewness","curtosis","entropy"]
for i in range(0,4):
    t1=[]
    t2=[]
    for row1 in X_train:
        t1.append(row1[i])
    for row2 in x_train:
        t2.append(row2[i])
    sns.kdeplot(t1,ax=ax1,label=label_names[i])
    sns.kdeplot(t2,ax=ax2,label=label_names[i])
plt.show()
  


def accuracy(y_true,y_predict):
    count = 0
    for i in range(len(y_true)):
        if(y_true[i] == y_predict[i]):
            count +=1
    return count*1.0/len(y_true)


def euclidean_distance(x1,x2):
    return np.sqrt(np.sum((x1 - x2)**2))



def get_k_neighbors(x_train,test,k):
    distance_vector={}
    for i in range(len(x_train)):
        distance_vector[i]=euclidean_distance(test,x_train[i])
    dist_sorted=sorted(distance_vector.items(),key=operator.itemgetter(1))
    neighbors=[]
    for i in range(k):
        neighbors.append(dist_sorted[i][0])
    return neighbors

def predict(neighbors,y_train,test):
    class_0=0
    class_1=0
    for i in range(len(neighbors)):
        if(y_train[neighbors[i]] == 0):
            class_0+=1
        else:
            class_1+=1
    if class_0 > class_1 :
        return 0
    else:
        return 1
    


def knn(x_train,y_train,x_test,k):
    class_pred=[]
    for i in range(0,len(x_test)):
        k_neighbors = get_k_neighbors(x_train,x_test[i],k)
        class_pred.append(predict(k_neighbors,y_train,x_test[i]))
    return class_pred


k_list=[1,3,5,7,9]

################################################################
##Using K-NN model classifier developed
test_acc=[]
train_acc=[]
for k in k_list:
    y_predict1 = knn(x_train,y_train,x_train,k)
    train_acc.append(accuracy(y_train,y_predict1))
    y_predict2 = knn(x_train,y_train,x_test,k)
    test_acc.append(accuracy(y_test,y_predict2))
    
 
print("\n\n\n#######   Training Accuracy with KNN MODEL DEVELOPED   #######")   
for i in range(0,len(k_list)):
    print("Training accuracy achieved with k = ",k_list[i]," is ",train_acc[i])
    

print("\n#######    Testing Accuracy with KNN MODEL DEVELOPED     #######")
for i in range(0,len(k_list)):
    print("Testing accuracy achieved with k = ",k_list[i]," is ",test_acc[i])

######################################################################
##Using scikit learn Knn classifier
test_acc=[]
train_acc=[]
for k in k_list: 
    clf = KNeighborsClassifier(n_neighbors=k, metric='euclidean')
    clf.fit(x_train,y_train)
    y_predict1 = clf.predict(x_train)
    y_predict2 = clf.predict(x_test)
    train_acc.append(accuracy(y_train,y_predict1))
    test_acc.append(accuracy(y_test,y_predict2))
    


print("\n#######     Training Accuracy with SCIKIT KNN MODEL     #######")
for i in range(0,len(k_list)):
    print("Training accuracy achieved with k = ",k_list[i]," is ",train_acc[i])
    
    
print("\n#######      Testing Accuracy with SCIKIT KNN MODEL      #######")
for i in range(0,len(k_list)):
    print("Testing accuracy achieved with k = ",k_list[i]," is ",test_acc[i])
    
#########################################################################    
    
print("\nThe accuaracy values for both train and test data obtained from k-NN model developed and that of the scikit learn are same")
print("\nBut the scikit model is faster than the k-NN model developed in predicting the class labels")