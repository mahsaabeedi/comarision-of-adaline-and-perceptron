# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 19:39:54 2020

@author: Mahsa Abedi
"""
import numpy as np 
import matplotlib.pyplot as plt
from pylab import *
import time

start =time.time()
##first set
x1_firstclass=np.random.normal(0,1,100)
x_11=(x1_firstclass*0.5)+1
x_11=x_11.reshape(100,1)

x2_firstclass=np.random.normal(0,1,100)
x_21=(x2_firstclass*0.5)+1
x_21=x_21.reshape(100,1)
#print( x_11)



x1_secondclass=np.random.normal(0,1,10)
x_12=(x1_secondclass*0.5)-1
x_12=x_12.reshape(10,1)

x2_secondclass=np.random.normal(0,1,10)
x_22=(x2_secondclass*0.5)-1
x_22=x_22.reshape(10,1)


Q_1 = np.concatenate((x_11,x_21),axis=1) 
##Q_1=Q_1.reshape(100,2)

#print(Q_1)
c=np.ones((100,1))
#print(c)
new_Q_1=np.append(Q_1,c,axis=1)
new_Q_1=new_Q_1.reshape(100,3)
#print(new_Q_1)

Q_2 = np.concatenate((x_12,x_22),axis=1) 
##Q_2=Q_2.reshape(100,2)
##print(Q_2.size)
c=np.array([[-1],[-1],[-1],[-1],[-1],[-1],[-1],[-1],[-1],[-1],
            ])

print(c.size)
new_Q_2=np.append(Q_2,c,axis=1)
new_Q_2=new_Q_2.reshape(10,3)
##print(new_Q_2)

Q = np.concatenate((new_Q_1,new_Q_2),axis=0)



w1=0 
w2=0 
alpha=0.02
tresh=0.4 
finish=0 
b=0
cost_function_list=np.zeros((110,1))
for k in range(100):
    j1=0
    x=0
    if finish!=1: 
        for i in range(110): 
            net=Q[(i,0)]*w1+Q[(i,1)]*w2+b 
            #print(net) #print(net) 
            if net>=0: 
                h=1 
            else:
                h=-1 
                #print(h)
            if i<100: 
                w1=w1+(alpha*(1-net)*Q[(i,0)]) 
                w2=w2+(alpha*(1-net)*Q[(i,1)]) 
                b=b+alpha*(1-net) 
                j=((1-h)**2) 
            else: 
                w1=w1+alpha*((-1-net)*Q[(i,0)])
                w2=w2+alpha*((-1-net)*Q[(i,1)]) 
                b=b+alpha*(-1-net) 
                j=((-1-h)**2)
            #print(j)
            #net = np.linspace(-10,10) 
            cost_function_list[i]=j 
            j1=j+j1 
            #print(j1)
            if i==109: 
                print(j1) 
            if j<tresh: 
                x=x+1 
                if x==109: 
                    finish=1 
                    print("finish") 
                    print("epoch:",k+1) 
                    print("w1:",w1) 
                    print("w2:",w2) 
                    print("b:",b) 
                    print("alpha",alpha)
                    plt.figure() 
                    ax1=plt.subplot(2,1,1) 
                    x = np.linspace(-1,3) 
                    plt.plot(x,((-w1*x-b)/w2)) 
                    plt.scatter(x_11,x_21,s=100,marker='.',color='blue') 
                    plt.scatter(x_12,x_22,s=100,marker='.',color='red') 
                    ax1.plot() 
                    plt.show()

end = time.time()
elapsed = end - start
print("elapsed time: " + str(elapsed))
            