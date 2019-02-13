import numpy as np
import matplotlib.pyplot as plt
t=np.arange(0,10,0.1)
x1=np.sin(2*np.pi*t)
x2=np.cos(2*np.pi*t)
plt.figure(1)
plt.title("sin wave")
plt.xlabel("time")
plt.ylabel("amplitude")
plt.plot(t,x1,'b')
plt.figure(2)
plt.title("cos wave")
plt.xlabel("time")
plt.ylabel("amplitude")
plt.plot(t,x2,'r')
plt.show()
