__Libraries used:__\
sklearn  for DecisionTreeClassifier\
pandas for reading the train_data and test_data

__Inputs:__\
iris_train_data\
iris_test_data

__Outputs:__\
Depth of learnt tree\
Number of leaf nodes of learnt tree\
Training accuracy of classifier\
Test accuracy using classifier\

__Pruning results for :__\
__case1:__ reducing max_depth\
 Test Accuracy for Max_depth =  4\
 Test Accuracy for Max_depth =  3\
 Test Accuracy for Max_depth =  2\
 Test Accuracy for Max_depth =  1

__Pruning results for __\
__case2:__ reducing max_leaf_nodes\
 Test Accuracy for Max_leaf_nodes=8\
 Test Accuracy for Max_leaf_nodes=7\
 Test Accuracy for Max_leaf_nodes=6\
 Test Accuracy for Max_leaf_nodes=5\
 Test Accuracy for Max_leaf_nodes=4\
 Test Accuracy for Max_leaf_nodes=3\
 Test Accuracy for Max_leaf_nodes=2
 
__Functions used:__\
__1.accuracy:__\
   inputs: y_true    y_predict\
   counted the number of correctly classified examples and divided it with the total number of examples and multiplied it with 100 to get the accuracy percentage.

__2.pruning_by_max_leaf_nodes__\
  input:number of leaf nodes of the classifier without pruning\
  Reduced the number of leaf nodes by 1 in each step by giving the max_leaf_nodes parameter to DecisionTreeClassifier and calculated the accuracy in each case and printed it accordingly

__3.pruning_by_max_depth__\
  input:depth of the classifier without pruning\
  Reduced the max_depth by 1 in each step by giving the max_depth parameter to DecisionTreeClassifier and calculated the accuracy in each case and printed it accordingly
