import numpy as np
time = 100000
system = []
ans = []
A = np.random.binomial(1,1/3, time)
B = np.random.binomial(1,1/3, time)
C = np.random.binomial(1,1/3, time)
D = np.random.binomial(1,1/3, time)
for i in range(len(A)):
    if A[i]==1 or B[i]==1 or C[i]==1 or D[i] ==1:
        system.append(1)
    if A[i]==1 and B[i]!=1 and C[i]!=1 and D[i] !=1:
        ans.append(1)
p = sum(ans) / sum(system)