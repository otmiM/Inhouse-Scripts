
#TypeGenerate
#Generate Type.txt file for polymerization in Polymatic:
#Author: Mohammed Al Otmi
#Description: This code takes datafile and generate Type.txt file
#datafile  should be devided into atoms.txt , bonds.txt , Angles.txt, dihedrals.txt ...

import sys
import os
import numpy as np
import pandas as pd
from ordered_set import OrderedSet


file_atom=np.loadtxt('atoms.txt')
file_bond= np.loadtxt('bonds.txt')
file_angle= np.loadtxt('angles.txt')
file_dihedral= np.loadtxt('dihedrals.txt')
file_improper= np.loadtxt('impropers.txt')



dict = {}
Type={1:'cp', 2:'hc', 3:'Lc2', 71:'Lc1'}
output =open("Types_Generated.txt","w")
for i in range (len(file_atom)):
    dict[int(file_atom[i,0])]=int(file_atom[i,2]) #replacing column 1 with column 3 type column
    
# for indx,type_number in dict.items():
#     print(indx, Type[type_number])




#Bonds Type
Bondlist = []
for i in range(len(file_bond)):
    mystr = (str(int(file_bond[i,1])) + ' ' + str(Type[dict[file_bond[i,2]]]) + ',' + str(Type[dict[file_bond[i,3]]]))
    Bondlist.append(mystr)
myset = OrderedSet(Bondlist)     #converts the list into a set set does not allow repetition 

output.write("\n"+ "bond types\n")
print("Bond Types \n")
for line in myset:
    print(line+'\n')
    output.write(line+'\n')




# #Angle types: 
print('#', '\n', 'angle types\n')
output.write('#'+'\n'+ 'angle types'+'\n')
file_angle=np.delete(file_angle, 0, axis=1)
file_angle1=file_angle[np.argsort(file_angle[:,0])]
mylist1=[]
for i in range(len(file_angle1)):
    mystr1 = (str(int(file_angle1[i,0]))+ " "+ str(Type[dict[file_angle1[i,1]]])+','+str(Type[dict[file_angle1[i,2]]])+','+str(Type[dict[file_angle1[i,3]]]))
    mylist1.append(mystr1)
myset1=OrderedSet(mylist1)
for line in myset1:
    print(line+'\n')
    output.write(line+'\n') 




#Dihedral Types 
print('#','\n','Dihedral Types')
output.write('#'+'\n'+ 'dihedral types\n')
file_dihedral=np.delete(file_dihedral, 0, axis=1)
file_dihedral1=file_dihedral[np.argsort(file_dihedral[:,0])]
mylist2=[]
for i in range(len(file_dihedral1)):
    mystr2 = (str(int(file_dihedral1[i,0]))+ " "+ str(Type[dict[file_dihedral1[i,1]]])+','+str(Type[dict[file_dihedral1[i,2]]])+','+str(Type[dict[file_dihedral1[i,3]]])+"," +str(Type[dict[file_dihedral1[i,4]]]))
    mylist2.append(mystr2)
myset2=OrderedSet(mylist2)
for line in myset2:
    print(line+'\n')
    output.write(line+'\n')

 
#Improper Types 
print('#','\n','impropers types')
output.write('#'+'\n'+ 'impropers types\n')
file_improper=np.delete(file_improper, 0, axis=1)
file_improper1=file_improper[np.argsort(file_improper[:,0])]
mylist3=[]
for i in range(len(file_improper1)):
    mystr3 = (str(int(file_improper1[i,0]))+ " "+ str(Type[dict[file_improper1[i,1]]])+','+str(Type[dict[file_improper1[i,2]]])+','+str(Type[dict[file_improper1[i,3]]])+"," +str(Type[dict[file_improper1[i,4]]]))
    mylist3.append(mystr3)
myset3=OrderedSet(mylist3)
for line in myset3:
    print(line+'\n')
    output.write(line+'\n')  