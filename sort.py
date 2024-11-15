### Purpose: This script can customize and sort large dump files ###
## specifically for orientation.py ##
### Syntax: python sort.py ###
### Author: Janani Sampath ###
### Date:  February 2015 ###
 

import sys,string
from numpy import *
from math import *
import fileinput

linelist=[]
infiles=['PSnpt.lammpstrj']
IN=fileinput.input(infiles)
tframes = 1280
tatoms = 3200

for step in range(tframes):
    linelist=[]
    l1=IN.readline()
    l2=IN.readline() 
    l3=IN.readline()
    l4=IN.readline()
    l5=IN.readline()
    l6=IN.readline()
    l7=IN.readline()
    l8=IN.readline()
    l9=IN.readline()

    
    for j in range(1,tatoms+1):
        line = IN.readline()
        [ii,molj,typej,qi,x1,x2,x3,n1,n2,n3] = string.split(line)
        k=int(ii)
        mol=int(molj)
        typek=int(typej)
        q = float(qi)
        x=float(x1)
        y=float(x2)
        z=float(x3)
        m1=int(n1)
        m2=int(n2)
        m3=int(n3)
        if typek == 12:
            line=[k,mol,1,q,x,y,z,m1,m2,m3]
            linelist.append(line)
        elif typek == 20:
            line=[k,mol,2,q,x,y,z,m1,m2,m3]
            linelist.append(line)
        elif typek == 63:
            line=[k,mol,3,q,x,y,z,m1,m2,m3]
            linelist.append(line)
        elif typek == 70:
            line=[k,mol,4,q,x,y,z,m1,m2,m3]
            linelist.append(line)
        elif typek == 71:
            line=[k,mol,5,q,x,y,z,m1,m2,m3]
            linelist.append(line)
        elif typek == 72:
            line=[k,mol,6,q,x,y,z,m1,m2,m3]
        #if typek in range(1,3):# and ((k%40) != 0) and ((k-39)%40 != 0):
            linelist.append(line)
            
            
    linelist.sort()
            
    ## for i in range(len(linelist)-2):
    ##     if ((linelist[i][2]==4) and (linelist[i+1][2]==5) and (linelist[i+2][2]==5)):
    ##         linelist[i][2] = 1
    ##         linelist[i+1][2] = 2
    ##         linelist[i+2][2] = 3
            
            
      #print("new time step")


    print l1,
    print l2,
    print l3,
    print 3200
    print l5,
    print l6,
    print l7,
    print l8,
    print l9, 
    for line in linelist:
        print ' '.join(map(str, line))    


        
    
    
