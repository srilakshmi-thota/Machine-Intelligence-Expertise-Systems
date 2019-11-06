__Libraries used:__\
->numpy to calculate squareroot\
->pandas to read the train and test input csv files\
->matplotlib for plotting the plots\
->sklearn for KneighborClassifier \
->seaborn for visualising the Bivariate Pairwise relationships between features

__Inputs:__\
->train_data_banknote_auth.csv containning the trainning dataset\
->test_data_banknote_auth.csv containning the test dataset

__Outputs:__\
->Plot display the Bivariate Pairwise relationships between features of dataset\
->Plot to visualise the input values before and after normalisation\
->Training Accuracy and Testing Accuracy with the k-NN classifier developed for k=1,3,5,7,9\
->Training Accuracy and Testing Accuracy with the sklearn classifier developed for k=1,3,5,7,9

->Normalized the features by removing the mean and scaling to unit variance using the StandardScaler module from numpy.preprocessing library\
->Test data inputs are normalised accordingly using the same

__User Defined functions:__\
__1.accuracy(y_true,y_target)__\
Inputs : y_true , y_predict\
Output : accuracy\
Counted the number of correctly classified examples and divided it with the total number of samples to get the accuracy.

__2.euclidean_distance(x1 , x2)__\
Inputs : x1 , x2\
Outputs : disatnce between the input points\
Calculates and returns the euclidean distance between the inputs points x1 , x2

__3.get_k_neighbors(x_train,test,k)__\
Inputs : x_train , test , k\
Output : K-nearest neighbors of the test instance\
Finds the distance between the test instance and the instances of x_train\
Returns the first k-nearest points to the test instance by considering the first k minimum distances

__4.predict_class(neighbors,y_train,test)__\
Inputs : neighbors , y_train , test\
Output :Predicted class of the test instance\
Predicts the output class of the test instance by  finding the majority vote of class labels among the k-nearest neighbors.

__5.knn(x_train,y_train,x_test,k)__\
Inputs : x_train , y_train , x_test , k\
Output : Predicted classes of the x_test samples\
Fits the model and predicts the class by calling the functions get_k_neighbors and then the predict_class function.

Accuracy values for both training and test data are obtained using the above knn model developed for k=1,3,5,7,9

The accuracy values for both training and test data are obtained using the sklearn KNeighborsClassifier for k=1,3,5,7,9
