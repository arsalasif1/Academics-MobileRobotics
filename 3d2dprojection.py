## Copyright (c) Mohmmad Arsal Asif. All rights reserved.

import matplotlib.pyplot as plt
import numpy as np
import math as m
###############################################
##plane unit A 
zoom=5
P_A=zoom*np.array([[1,0,0],[0,1,0],[0,0,1]])

###############################################

## Rotations axis and angles
theta= 50 #Choose Rotation angle 


R_X= np.array([[1,0,0],[0,m.cos(m.radians(theta)),-m.sin(m.radians(theta))],[0,m.sin(m.radians(theta)),m.cos(m.radians(theta))]])
R_Z= np.array([[m.cos(m.radians(theta)),-m.sin(m.radians(theta)),0],[m.sin(m.radians(theta)),m.cos(m.radians(theta)),0],[0,0,1]])
R_Y= np.array([[m.cos(m.radians(theta)),0,m.sin(m.radians(theta))],[0,1,0],[-m.sin(m.radians(theta)),0,m.cos(m.radians(theta))]])

R_T= np.dot(P_A,R_Z) #Choose R_X, R_Y, or R_Z change in for loop too

print('Rotated Matrix:\n')
print(R_T)
fig, ax = plt.subplots()


###############################################
## i=0 draws original plane and i=1 in black draws rotated plane in red
for i in range (0,2):
        R_T=(i==1)*np.dot(P_A,R_Z)+(i==0)*P_A #Choose R_X, R_Y, or R_Z
        ###############################################
        ## Applying Cabnit projection transfrom for visualization

        T_C=np.array([[1, 0, -0.5*m.cos(m.radians(m.atan(2)))],[0, 1, -0.5*m.sin(m.atan(2))],[0,0,0]])

        res=np.dot(T_C,R_T)

        print('\n3d to 2d plane projection:\n')
        print (res)

        ###############################################

        ## Plotting the matrix
        # X-axis
        x_pos = 0
        y_pos = 0
        x_direct = res[0][0]
        y_direct = res[1][0]
        print (y_direct)
        ax.quiver(x_pos,y_pos,x_direct,y_direct,color=(i==0)*'k'+(i==1)*'r',angles='xy',scale_units='xy',scale=1)
        ax.text(res[0][0],res[1][0],"X-axis",color=(i==0)*'k'+(i==1)*'r');


        # Y-Axis
        x_pos = 0
        y_pos = 0
        x_direct = res[0][1]
        y_direct = res[1][1]

        ax.quiver(x_pos,y_pos,x_direct,y_direct,color=(i==0)*'k'+(i==1)*'r',angles='xy',scale_units='xy',scale=1)
        ax.text(res[0][1],res[1][1],"Y-axis",color=(i==0)*'k'+(i==1)*'r');

        # Z-axis

        x_pos = 0
        y_pos = 0
        x_direct =res[0][2]
        y_direct =res[1][2]
        ax.quiver(x_pos,y_pos,x_direct,y_direct,color=(i==0)*'k'+(i==1)*'r',angles='xy',scale_units='xy',scale=1)
        ax.text(res[0][2]-0.1,res[1][2]-0.1,"Z-axis",color=(i==0)*'k'+(i==1)*'r');

        #############################################
        ## Setting zoom relative to the plot

        #alim=2.5*max(m.sqrt(pow(res[0][0],2)+pow(res[1][0],2)),m.sqrt(pow(res[0][1],2)+pow(res[1][1],2)),m.sqrt(pow(res[0][2],2)+pow(res[1][2],2))) 
        plt.axis([zoom*-1.25, zoom*1.25,zoom*-1.25 , zoom*1.25])
        
        ###############################################
        ##Point ploting valid for rotation in z-axis only... cabint transform needs to be implimented
        ## Ploting a point in local referece frame
        PointL=np.array([1,1,1])
        P_T= np.dot(PointL,np.transpose(R_Z))
        ax.plot(P_T[0],P_T[1],marker="X", color="red");
        
        ###############################################
        ## Ploting a point in global referece frame
        PointG=np.array([1,1,1])
        ax.plot(PointG[0],PointG[1],marker="X", color="black");
        
        ###############################################
        
        
plt.show()

    #############################################

