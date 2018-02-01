import numpy as np  # importing numpy package

## METHODS TO CREATE ARRAY
a = np.arange(1, 26)  # creates 1-d array from 1 to 15
print(a)

a2 = np.array(range(1, 28))
print(a2)

a3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
a3 = np.array(a3)  # creates 2-d array of list of lists
print(a3)

a4 = np.zeros((5, 5))
print(a4)  # creates zero matrix of 5X5

a5 = np.ones((5, 5))  # Return a new array of given shape and type, filled with ones
print(a5)

a6 = np.linspace(0, 10, 16)  # Return evenly spaced numbers over a specified interval
print(a6)

a7 = np.eye(5)  # Return a 2-D array with ones on the diagonal and zeros elsewhere
print(a7)

# # CONVERSION OF 1-D ARRAY TO HIGHER DIMENSIONS

a8 = a.reshape(5, 5)  # 1-D TO 2-D ARRAY RESHAPING
print(a8)

a9 = a2.reshape(3, 3, 3)  # 1-D TO 3-D ARRAY RESHAPING
print(a9)

## SLICING AND DICING

print(a)
print(a[1:6])  # slice array from 1 to 6 syntax-( array[ from : upto ] )
print(a[:6])  # slice array from beginning  to 6
print(a[3:])  # slice array from 3 upto last element
print(a[:-1])
print(a[-1:])
print(a[4:-1])
print('')
print(a8)
print('')
print(a8[:2, 1:])  # syntax( array[from row : upto row , from column: upto column] )
print(a8[2:4, :3])

# OPERATION ON ARRAY
arr1 = np.zeros((5,5))
print(arr1)
arr1=arr1+3
print(arr1)
arr1=arr1*7
print(arr1)
arr1=np.sqrt(arr1)
print(arr1)
arr1=np.log(arr1)
print(arr1)
