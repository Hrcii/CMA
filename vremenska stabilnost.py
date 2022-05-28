import numpy as np
import matplotlib.pyplot as plt

##PROMINITI ADRESU!!!
f=open("C:\\Users\\hrvoj\\OneDrive\\Radna površina\\LAFRA\\futures-active_adjusted_1min_qucz81\\BTC_continuous_adjusted_1min.txt")
f1=open("C:\\Users\\hrvoj\\OneDrive\\Radna površina\\LAFRA\\optimirani.txt")

n=50
p=7200
w=np.array([])
w1=np.ones(n)/n
prices=f.readlines()
error=np.array([])
error1=np.array([])
#price_matrix=np.array([])

w1=f1.readlines()
for i in range(len(w1)):
    w1[i]=float(w1[i])

for i in range(len(prices)):
    prices[i]=float(prices[i].split(",")[4])

for i in range(len(prices)//(n+p-1)):
    c=prices[i*(n+p-1):(i+1)*(n-1+p)]
    cma=np.array([])
    sma=np.array([])
    for j in range(n,n+p):
        cma=np.append(cma,np.dot(c[j-n:j],w1))
        sma=np.append(sma,np.dot(c[j-n:j],np.ones(n)/n))
    error=np.append(error,np.linalg.norm(cma-c[n-1:],1)/p)
    error1=np.append(error1,np.linalg.norm(sma-c[n-1:],1)/p)
plt.plot(np.linspace(0,len(prices)//(n+p-1)-1,len(prices)//(n+p-1)),error,label="CMA(50)")
plt.plot(np.linspace(0,len(prices)//(n+p-1)-1,len(prices)//(n+p-1)),error1,label="SMA(50)")
plt.legend()
plt.title("BTC, 2049 uzoraka po otvoru")
plt.xlabel("vremenski otvor")
plt.ylabel("acc")
plt.show()


