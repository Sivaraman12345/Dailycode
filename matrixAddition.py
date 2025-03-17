r,c=map(int,input().split())
m1=[list(map(int,input().split())) for i in range(r)]   
m2=[list(map(int,input().split())) for i in range(r)]
print([[m1[i][j]+m2[i][j] for j in range(len(m1[0]))] for i in range(len(m1))])