import pandas as pd
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier

def accuracy(y_true,y_predict): 
    count=0;
    for i in range(0,len(y_true)):
        if y_true[i] == y_predict[i]:
            count=count+1;   
    return(count*100*1.0/len(y_true));
    
def pruning_by_max_leaf_nodes(t):
    for i in range(1, t-1):
        clfnxt1 = DecisionTreeClassifier(criterion= 'entropy',max_leaf_nodes=t-i);
        clfnxt1.fit(x_train,y_train)
        print('Max_leaf_nodes = ',t-i,'Test Accuracy = ',accuracy(y_test,clfnxt1.predict(x_test)))    
    return;
 
def pruning_by_max_depth(t):
    for i in range(1, t):
        clfnxt2 = DecisionTreeClassifier(criterion= 'entropy',max_depth=t-i);
        clfnxt2.fit(x_train,y_train)
        print('Max_depth = ',clfnxt2.tree_.max_depth,'Test Accuracy = ',accuracy(y_test,clfnxt2.predict(x_test))) 
    return;
    
#reading trainning data
train_data=pd.read_csv("iris_train_data.csv",header=0)
x_train=train_data.values[:,0:4];
y_train=train_data.values[:,4];

#training the classifier 
clf=DecisionTreeClassifier(criterion= 'entropy');
clf.fit(x_train,y_train);

print('Depth of learnt tree is ',clf.tree_.max_depth)
#t=clf.get_n_leaves()
print('Number of leaf nodes in learnt tree is 9','\n')

#reading test data
test_data=pd.read_csv("iris_test_data.csv",header=0)
x_test=test_data.values[:,0:4];
y_test=test_data.values[:,4];

#Training accuracy and Test accuracy without pruning
print('Training accuracy of classifier is ',accuracy(y_train,clf.predict(x_train)))
print('Test accuracy using classifier is ',accuracy(y_test,clf.predict(x_test)),'\n')

#Pruning by reducing max_depth
print('Pruning case1:By reducing the max_depth of the tree')
pruning_by_max_depth(clf.tree_.max_depth)
print('')    
t=9;

#Pruning by reducing max_leaf_nodes
print('Pruning case2:By reducing the max_leaf_nodes of the tree')
pruning_by_max_leaf_nodes(t);
