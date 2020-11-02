import os
import string
from datetime import datetime
import numpy as np
import itertools
import glob
import sklearn
import matplotlib.pyplot as plt



PATH='/Users/tinku/Downloads/termproject-submission_23356/data'
alp = list(string.ascii_uppercase)
alp2 = list(map(''.join,itertools.permutations(string.ascii_uppercase,2)))

##########################################################
def feature_extractor(file,features):
    lines = [line.rstrip('\t\n') for line in open(file)]
    f_list = [event.split('\t') for event in lines]
    
    
    ##########################################################
       
    def timediff(t1,t2):
        day1=datetime.strptime(t1, "%b %a %d:%H:%M:%S.%f")
        day2=datetime.strptime(t2, "%b %a %d:%H:%M:%S.%f")
        sec = (day2-day1).total_seconds()
        return(sec)
    
    ##########################################################
    	
    KeyUps = [x for x in f_list if 'KeyUp' in x]
    KeyDowns = [x for x in f_list if 'KeyDown' in x]
    
    ###########################################################
    
    tups =  [item[5] for item in KeyUps if chr(int(item[1])) in alp]
    tdowns =  [item1[5] for item1 in KeyDowns if chr(int(item1[1])) in alp]
    try:
        letterup =  [item[1].upper() for item in KeyUps if chr(int(item[1])) in alp]
    except: 
        pass
        
    try:
        letterdown = [item1[1].upper() for item1 in KeyDowns if chr(int(item1[1])) in alp]
    except:
        pass
    
      
    #############################################################
    
    
    for i in range(0,len(tups)):
        t = i
        try:
            t1 = tdowns[i]
    
            if letterup[t] != letterdown[i]:
                j = i
        
                if i == len(tups)-1:
                    j = 0
                    while j<len(tups)-1 and letterdown[i]!= letterup[j] and i!=len(tups)-1:
                        j = j+1
        
                tj = tups[j]
                k = i
        
                if i == 0:
                    k = len(tups)-1
                    while k>=1 and letterdown[i]!= letterup[k] and i!=0:
                        k = k-1
        
                tk = tups[k]
        
        
                if timediff(t1,tk)>0 and timediff(t1,tj)>0 :
                    if abs(j-i)<abs(i-k):
                        t = j
                    else:
                        t = k
                            
                elif timediff(t1,tk)<0 :
                    t = j
                else:
                    t = k
    
            t2 = tups[t]
        
       

            if i!=len(tups)-1:
    
                t3 = tdowns[i+1]
                latency = timediff(t1,t3)
   
                lat =[ chr(int(letterdown[i]))+chr(int(letterdown[i+1])),latency]
                features.append(lat)

            hold_time = timediff(t1,t2)
            hold =[ chr(int(letterdown[i])),hold_time]
        except:
            pass
        features.append(hold)
      
	
###################################################################
        
def preprocessing(features):
    
    mean=[]
    for i in range (0,len(alp)):
        values=[]
        for j in features:
            if j[0]==alp[i] and j[1]<15:
                values.append(j[1])
        if(len(values)==0):
            mean.append(0)
        else:
            mean.append(sum(values)/len(values))
    for i in range(0,len(alp2)):
       values=[]
       for j in features:
           if j[0]==alp2[i] and j[1]<50:
               values.append(j[1])
       if(len(values)==0):
           mean.append(0)
       else:
           mean.append(sum(values)/len(values))
    return mean


###################################################################   
     
def accuracy(y_predict,y_actual):
    count=0;
    for i in range (0,len(y_predict)):
        if (y_predict[i] == y_actual[i]):
            count=count+1;
    accuracy=count*1.0/len(y_predict)
    return accuracy

#################################################################
##Trainning dataset feature vector
    
Mean_train = []
Label_train = []
for file in glob.glob(PATH+'/legal/*.txt'):
    feature=[]
    feature_extractor(file,feature)
    Mean_train.append(preprocessing(feature))
    Label_train.append('legal')
    
for file in glob.glob(PATH+'/intruder/*.txt'):
    feature=[]
    feature_extractor(file,feature)
    Mean_train.append(preprocessing(feature))
    Label_train.append('intruder')
    
    
######################################################################
##Visualising the holdtime and latencies of keystrokes
    
for i in range (0,4):
    plt.plot(alp[0:6],Mean_train[i][0:6],'g--',marker='^')
plt.xlabel('Key')
plt.ylabel('Hold time(sec)')
plt.title("Hold time of samples of a user")
plt.show()

for i in range (0,4):
    plt.plot(alp2[150:158],Mean_train[i][176:184],'g--',marker='^')
plt.xlabel('keystrokes')
plt.ylabel('Latencies(sec)')
plt.title("Latencies of samples of a user")
plt.show()

####################################################################
##NaiveBayesclassifier

from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import KFold, cross_val_score
k_fold = KFold(n_splits=5,shuffle=True)
gnb = GaussianNB()
gnb.fit(Mean_train,Label_train)
print("\n Cross validation score:")
cross_val_scores=cross_val_score(gnb, Mean_train, Label_train, cv=k_fold)
print(cross_val_scores)
print("Accuracy obtained is ",sum(cross_val_scores)/len(cross_val_scores))

####################################################################
##Test dataset feature vector
Mean_test=[]
Label_test=[]
for file in glob.glob(PATH+'/test/legal/*.txt'):
    feature=[]
    feature_extractor(file,feature)
    Mean_test.append(preprocessing(feature))
    Label_test.append('legal')
    
    
for file in glob.glob(PATH +'/test/intruder/*.txt'):
    feature=[]
    feature_extractor(file,feature)
    Mean_test.append(preprocessing(feature))
    Label_test.append('intruder')
    
    
#################################################################
##Predicting the labels for the test data
    
Label_predict=gnb.predict(Mean_test)
print("\n Predicted Labels for test data:")
print(Label_predict)


#Accuracy of the classifier over the test data
print("\n Accuracy obtained over test data: ",accuracy(Label_predict,Label_test))


