#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np

k_points =  np.loadtxt("lead_kband.dat",  dtype = float, usecols = (0,1,2))
a_points =  np.loadtxt("a_points_tb.dat", dtype = float, usecols = (0,1,2))
t        =  np.array([0.654068,0.262586, 0.400446, 0.426529, 0.353707])
N        =  np.array([1,1,1,3,3])


E0       = 7.844960
wght     = 1 / N
a        = a_points
k        = 2*np.pi*k_points
print(np.size(k[:,0]))
print(a[20])
E_points = []

for i in np.arange(0,np.size(k[:,0])):
    E1_k = 2*wght[0]*t[0]*(np.cos(np.dot(k[i],a[0]))+ np.cos(np.dot(k[i],a[1]))+np.cos(np.dot(k[i],a[2])))

    E2_k = 2*wght[1]*t[1]*(np.cos(np.dot(k[i],a[3]))+ np.cos(np.dot(k[i],a[4]))+np.cos(np.dot(k[i],a[5])))

    E3_k = 2*wght[2]*t[2]*(np.cos(np.dot(k[i],a[6]))+ np.cos(np.dot(k[i],a[7]))+np.cos(np.dot(k[i],a[8])))

    E4_k = 2*wght[3]*t[3]*(np.cos(np.dot(k[i],a[9]))+ np.cos(np.dot(k[i],a[10]))+np.cos(np.dot(k[i],a[11])) +                np.cos(np.dot(k[i],a[12]))+ np.cos(np.dot(k[i],a[13]))+np.cos(np.dot(k[i],a[14])) +                np.cos(np.dot(k[i],a[15]))+ np.cos(np.dot(k[i],a[16]))+np.cos(np.dot(k[i],a[17])))

    E5_k = 2*wght[4]*t[4]*(np.cos(np.dot(k[i],a[18]))+ np.cos(np.dot(k[i],a[19]))+np.cos(np.dot(k[i],a[20])))
    
    E = E0 + E1_k + E2_k + E3_k + E4_k + E5_k
    
    E_points.append(E)
    
k_plot   =  np.loadtxt("lead_band.dat", dtype = float, usecols = 0)

E_band = np.column_stack((k_plot,E_points))
    
#print(E_points)
np.savetxt("Eband_tb.dat", E_band, fmt = ("%10.6f", "%10.6f"))

