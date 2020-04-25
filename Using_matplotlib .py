
import matplotlib.pyplot as plt
import seaborn as sns


x=list(range(0,10))
y=list(range(-10,0))
plt.plot(x,y)
plt.show()

a=[0,-100,25,67,-323]
b=[0,3,7,3,9]
plt.plot(a,b)
plt.show()


c=[-100,0,100,120]
d=[1,3,5,9]
plt.plot(c,d,'ro') #red dots
plt.show()

plt.plot([1,3,5,6],[4,5,6,8],'g^') #green triangle
plt.show()


