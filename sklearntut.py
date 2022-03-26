from sklearn import datasets, linear_model
import numpy as np
import matplotlib as plt


diabetes = datasets.load_diabetes()
#dict_keys(['data', 'target', 'frame', 'DESCR', 'feature_names', 'data_filename', 'target_filename', 'data_module'])

diabetes_X = diabetes.data[: np.newaxis, 2]
print(diabetes_X)
diabetes_X_train = diabetes_X[: :20]
print(diabetes_X_train)