# Handwritten Chinese Numeral Recognition Using Convolutional Neural Network

The repository is used for  a project about handwritten Chinese numeral recognition using convolutional neural network. This is not an original project since some of the codes are copied from Andrew Wu’s course from Coursera. In other words, it can be viewed as a solution to Wu’s project homework.

The project builds a CNN model with the aid of Google’s tensorflow frame. It uses the data from MNIST for traning and achieve a 95.5% accuracy rate on the test set.

The repository consists of the following parts:

* `MNIST.zip` contains a small dataset of handwritten Chinese numbers from MNIST. 
* The directory `rawdata` contains images extracted from `MINST.zip`. It contains two directories: `train` with 8000 images inside and `test` with 2000 images inside.
* `h5.py` is used for generating labeled data file `train.h5` and `test.h5`.
* `train.h5` and `test.h5` are labeled data files for CNN to learn
* `tensorflow-cnn.ipynb` contains the code of the convolutional neural network. It uses Google’s tensorflow frame to train the model.
* `params.ckpt` contains the parameters learned by CNN. After loading the parameters, the predictor can immediately work
* `cnn_utils.py` is provided by Andrew Wu’s course and it contains some utilities for the project, such as the function for reading the data and making minibatches.

Please feel free to use the codes and dataset in this repository.

