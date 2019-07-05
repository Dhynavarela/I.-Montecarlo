#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random
import matplotlib.pyplot as plt

#b) 
#Integración por Método de montecarlo. 

#seed=int(input('Ingresar semilla: '))
G = 6.67*10**(-11)#m³7kg*seg²
D = 10000 #10 Tm =10000kg
L = 10#m
seed = 12345
ax = random.seed(seed)
sum = float()
    
M = 100
aa1 = -5.0
bb1 = 5.0
aa2 = -5.0
bb2 = 5.0

def f(x,y,z):
    return (D*G*z)/((x**2+y**2+z**2)**(3/2))
   
def fuerza(z):
    ss = 0
    for i in range (1,M):
        ax = random.random()
        ay = random.random()
        ss = ss + f(aa1+(bb1-aa1)*ax, aa2+(bb2-aa2)*ay,z)
        
    return ((bb1-aa1)*(bb2-aa2)*ss)/M


Z = [0]
fz = [fuerza(0)]
dz = 0.01
for i in range(10001):
    Z.append(Z[i]+dz)
    fz.append(fuerza(Z[i]))
    #print("Aprox de la fuerza para z = %s por Montecarlo con = %s" % (i*0.001,fuerza(i*0.001)))
         
#c) Curva graficada

plt.figure()
plt.title("")
plt.plot(Z,fz)
plt.grid(color='B', linestyle='-', linewidth=0.1)
plt.xlabel('Eje Z')
plt.ylabel('Eje Fz')


# In[ ]:




