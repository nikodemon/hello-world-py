A=[[1,2,3],[4,5,6],[7,8,9]]
AD=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(A[1])):
  for j in range(len(A[1])):
    AD[i][j]=(-1)**(j+1+i+1)*A[j][i]
    print AD[i][j]
  