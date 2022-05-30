import numpy as np
import opt
import matplotlib.pyplot as plt

path1 = "C:\\Users\\hrvoj\\OneDrive\\Radna površina\\LAFRA\\" \
      "futures-active_adjusted_1min_qucz81\\BTC_continuous_adjusted_1min.txt"
path2 = "C:\\Users\\hrvoj\\OneDrive\\Radna površina\\" \
        "LAFRA\\futures-active_adjusted_1min_qucz81\\MBT_continuous_adjusted_1min.txt"

n = 50
p = 7200
prices = open(path2).readlines()

for i in range(len(prices)):
    prices[i] = float(prices[i].split(",")[4])

w=opt.opt(path1,n,p)
w1 = np.ones(n)/n
error=np.array([])
error1=np.array([])
for i in range(len(prices)//(n+p-1)):
    c=prices[i*(n+p-1):(i+1)*(n-1+p)]
    cma=np.array([])
    sma=np.array([])
    for j in range(n,n+p):
        cma=np.append(cma,np.dot(c[j-n:j],w))
        sma=np.append(sma,np.dot(c[j-n:j],w1))
    error=np.append(error,np.linalg.norm(cma-c[n-1:],1)/p)
    error1=np.append(error1,np.linalg.norm(sma-c[n-1:],1)/p)
plt.plot(np.linspace(0,len(prices)//(n+p-1)-1,len(prices)//(n+p-1)),error,label="CMA(50)")
plt.plot(np.linspace(0,len(prices)//(n+p-1)-1,len(prices)//(n+p-1)),error1,label="SMA(50)")


plt.legend()
plt.title("MBT, 2049 uzoraka po otvoru, optimirano na BTC")
plt.xlabel("vremenski otvor")
plt.ylabel("acc")
plt.show()