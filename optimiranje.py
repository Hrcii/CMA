#racunanje i prikaz prosjecnog odstupanja filtera od
#stvarnih vrijednosti kroz vrijeme
import cvxpy as cp
import numpy as np
import matplotlib.pyplot as plt
import time
#PROMINITI ADRESU!!!
f=open("C:\\Users\\hrvoj\\OneDrive\\Radna površina\\LAFRA\\futures-active_adjusted_1min_qucz81\\BTC_continuous_adjusted_1min.txt")
f1=open("C:\\Users\\hrvoj\\OneDrive\\Radna površina\\LAFRA\\optimirani.txt","w")
n = 50
p=7200 #5 dana
lmbda = cp.Variable(100)
prices=np.array([])
c=np.array([])
C_matrix=np.array([])
C2=np.array([])
C1=np.array([])
C0=np.array([])
w=cp.Variable((n))
k=0

for i in range(n+p-1+k):
    if i>=k:
        prices=np.append(prices,float(f.readline().split(",")[4])) #.split(",")[4]
    else:
        f.readline()
for i in range(p):
    c=np.append(c,prices[n-1+i])
    C_matrix=np.append(C_matrix,prices[i:i+n])
    if i>=2 and i<=p-1:
        C2=np.append(C2,prices[i:i+n])
    if i>=1 and i<=p-2:
        C1=np.append(C1,prices[i:i+n])
    if i>=0 and i<=p-3:
        C0=np.append(C0,prices[i:i+n])
C_matrix=np.reshape(C_matrix,(p,n))
C2=np.reshape(C2,(p-2,n))
C1=np.reshape(C1,(p-2,n))
C0=np.reshape(C0,(p-2,n))
dC=(C2-2*C1+C0)
t1=time.time()
w=cp.Variable(n)
error=cp.norm((C_matrix @ w) - c,1)/p #conv
smoo=cp.norm(dC @ w,1)/(p-2) #conv
constr=[smoo<=1.485]
cost=error+lmbda*cp.abs(error-smoo) #neconv
prob=cp.Problem(cp.Minimize(error) , constr)
prob.solve()
print(time.time()-t1) #ISPISUJE SE VRIME OPT
plt.plot(np.linspace(0,n-1,n),w.value)
plt.title("BTC, smoo=1.485")
plt.xlabel("broj koeficijenta")
plt.ylabel("iznos")
w1=w.value
cma=np.matmul(C_matrix,w1)
#print(np.linalg.norm(cma-prices[n-1:],1)/p)
sma=np.matmul(C_matrix,np.ones(n)/n)
smoo=0
#for i in range(2,len(sma)):
#    smoo+=abs(sma[i]-2*sma[i-1]+sma[i-2])
#print(smoo/(p-2))
#print(np.linalg.norm(sma-prices[n-1:],1)/p)
for i in w1:
    f1.write(str(i)+"\n")
#print(sum(w1))
f1.close()
plt.show()