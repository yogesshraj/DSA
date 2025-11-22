import numpy as np

v = [1,2]
a = [[1,2],
     [4,5]]

#this is how we find eigen values and eigen vectors
eigen_v, eigen_vec = np.linalg.eig(a)
print(eigen_v, eigen_vec)

