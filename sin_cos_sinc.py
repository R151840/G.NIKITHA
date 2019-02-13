import numpy as np
import matplotlib.pyplot as plt
t=np.arange(-10,10,0.1)
x1=np.sin(2*np.pi*t)
x2=np.cos(2*np.pi*t)
x3=np.sinc(2*np.pi*t)
plt.subplot(1,3,1)
plt.title("sin wave")
plt.xlabel("time")
plt.ylabel("amplitude")
plt.plot(t,x1,'b')
plt.subplot(1,3,2)
plt.title("cos wave")
plt.xlabel("time")
plt.ylabel("amplitude")
plt.plot(t,x2,'r')
plt.subplot(1,3,3)
plt.title("sinc wave")
plt.xlabel("time")
plt.ylabel("amplitude")
plt.plot(t,x3,'b')
plt.show()
