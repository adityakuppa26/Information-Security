import numpy as np 

plain="ACT"
key="GYBNQKURP"

k=0

pmat=np.zeros((3,1))
mat=np.zeros((3,3))

# key to matrix

for i in range(3):
    for j in range(3):
        mat[i][j]=ord(key[k])-65
        k=k+1 

# plain text to matrix

for i in range(3):
    pmat[i][0]=ord(plain[i])-65

# multiplying key and plain text   

res=np.dot(mat,pmat)
temp=res
res=res%26

# printing encrypted message 

result=""
for i in range(3):
    result+=(chr(int(res[i][0])+65))

print(result)                # Output : POH

# calculating inverse
        
invmat=np.linalg.inv(mat)

# multiply inverse and encrypted message

conv=np.dot(invmat,temp)
conv=conv%26

# print decrypted text

plain=""
for i in range(3):
    plain+=(chr(int(conv[i][0])+65))

print(plain)
