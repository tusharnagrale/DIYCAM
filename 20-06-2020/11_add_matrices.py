#Write a python program to add two matrix. Assume number of rows and columns of both matrix are same.
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

#loop for iterating Rows
for i in range(len(X)):

    #loop for iterating through Columns
   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]

for r in result:
   print(r)