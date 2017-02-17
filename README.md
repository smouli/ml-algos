The project contains implementation of a few common Machine Learning algorithms in Python, done from scratch, as part of the Statistical
Machine Learning course in Purdue

The algorithms covered are

1. A linear perceptron algorithm, implemented in linperceptron.py outputting the weight vector, and a predictor for unknown test values using the trained 
   perceptron model in linpred.py

2. A kernel perceptron algorithm, implemented in kerperceptron.py outputting the weight vector, and a predictor for unknown test values using the trained 
   perceptron model in kerpred.py  
    More description on the algorithm used is provided in hw1.pdf

   To train and test the perceptrons, use  
   `python linpredtest.py/kerpredtest.py  <num_iterations_of_perceptron> <num_training_pts> <num_dimensions>`
   
   A test label will be randomly generated and tested, and a visual representation of the train and test points will be shown.   
   The linear separable data is generated for these algorithms via createsepdata.py   

3. A PRank algorithm, implemented in prank.py outputting the weight vector and cutoffs for labels, and and a predictor for unknown test values using the trained 
   perceptron model in rankpred.py. More description on the algorithms used is provided in hw2.pdf
   
   To train and test PRank, use  
   `python rankpredtest.py  <num_iterations_of_perceptron> <num_training_pts> <num_dimensions> <num_labels>`  
   
   A test label will be randomly generated and tested, and a visual representation of the train and test points will be shown.  
   The label separable data is generated for these algorithms via createseprankdata.py   
   
4. K-fold cross validation and bootstrap algorithms, implemented in kfoldcv.py and bootstrapping.py respectively, outputting the mean square error
   vector of size num_folds of num_bootstraps.  More description on the algorithm used is provided in hw3.pdf
   
   To test the implementations, use  
   `python kfoldcv.py <num_folds> <num_training_pts> <num_dimensions>`  
  `python bootstrapping.py <num_bootstraps> <num_folds> <num_dimensions>`  
  The linear regression data is generated for these algorithms via createlinregdata.py