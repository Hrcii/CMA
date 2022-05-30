import matplotlib.pyplot as plt
import numpy as np

w=open("C:\\Users\\hrvoj\\OneDrive\\Radna površina\\"
       "LAFRA\\optimirani koef.txt").readlines() #KOEF NA GITU!
for i in range(len(w)):
    w[i]=float(w[i])
w=w[::-1]
omega=np.linspace(-np.pi,np.pi,200)
H=np.array([])
for i in omega:
    s=0
    for k in range(len(w)):
        s += w[k]*(np.cos(k*i)-1j*np.sin(k*i))
    H=np.append(H,s)

plt.subplot(3,1,1)
plt.plot(omega,abs(H))
plt.title("Amplitudno-frekvencijska karakteristika filtera")
plt.xlabel("w [rad/s]")
plt.ylabel("|H(jw)|")

plt.subplot(3,1,3)
plt.plot(omega,np.angle(H))
plt.title("Fazno-frekvencijska karakteristika filtera")
plt.xlabel("w [rad/s]")
plt.ylabel("∠H(jw)")
plt.show()
