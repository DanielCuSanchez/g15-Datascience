import numpy as np
import matplotlib.pyplot as plt


a = np.array([1, 2, 3,4,5,6,7,8,9,10,0.1,3,1.5])
b = np.array([1, 2, 3,4,5,6,7,8,9,10,0.1,3,45.5])

print(a)
#print(type(a))

a.sort()
print(a)

mean = a.mean()
print(mean)

max = a.max()
print(max)

min = a.min()
print(min)


c = np.concatenate((a,b))
c.sort()
print(c)

print("Dimensiones")
print("a = ",a.ndim)
print("b = ",b.ndim)
print("c = ",c.ndim)

print("Tamaño")
print("a = ",a.size)
print("b = ",b.size)
print("c = ",c.size)

d = np.array([[[1,2,4,6],[1,3,4,5]],[[1,2,4,6],[1,3,4,5]],[[1,2,4,6],[1,3,4,5]]])
print("Forma")
print("a = ",a.shape)
print("b = ",b.shape)
print("c = ",c.shape)
print("d = ",d.shape)

e = np.array([[[1,2,4,6],[1,3,45,5]]])
# f[1,3,4,5] = f[3]
print(e[0][1][2])
print(e)

#for x in np.nditer(e):
  #print(x)


print("Traditional")
for i in range(1):
  for j in range(2):
    if (j != 0):
        for k in range(4):
          print(e[i][j][k])


print(e)

print("nditer Numpy")
for x in np.nditer(e[:,1::,::2]):
  print(x)

print(e)
for idx, x in np.ndenumerate(e):
  print("idx = ",idx, "x =", x)


print("a = ", a)
plt.plot(a)
plt.show()