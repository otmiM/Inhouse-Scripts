## This is a code that can take a list of bonded pairs and convert it into all possible dihedrals
## FIXME: impropers are listed separately, but need to figure out how to print out in the right sequence
## FIXME: this can be modified easily to add angles
## FIXME: Duplicate entries need to be removed
## Convert bond.txt to bond.csv and place it in the same folder as code
## Execute code as '$ python getdihedrals.py'
## Author: Janani Sampath
##Edited: Mohammed Al Otmi
## Date: 5/25/21

from os import close, closerange
import numpy as np
import pandas as pd
import string as string
from ordered_set import OrderedSet

bond_info = pd.read_csv("PE3_bonds.csv")
bondlist = bond_info.loc[:,['b1','b2']]
a1 = bond_info.iloc[len(bond_info)-1,2]
a2 = bond_info.iloc[len(bond_info)-1,3]# a1,a2 will be used to identify new angles,dihedrals, and impropers
x = []
y = []
z = []
dix = []
diy = []
diz = []
imx = []
imy = []
imz = []
anx= []
any=[]
anz=[]
indexlist = []

#using pandas to prepare the bonds file, convert everything to a list of bond pairs and arrange each par in ascending order 
for i in range(len(bondlist)):
    if (bondlist.iloc[i,0] > bondlist.iloc[i,1]):
        tmp = bondlist.iloc[i,0]
        bondlist.iloc[i,0]=bondlist.iloc[i,1]
        bondlist.iloc[i,1]=tmp
bonds = bondlist.values.tolist()

#group bond pairs that forms a dihedral or an improper. This means you will get groups of 3.
#For each bond pair [a,b] go over the entire list of bonds till you find a bond that contains one similar element, e.g [a,c] or [b,c]
#Using the second bond pair, go over the entire list of bonds again till you find a third bond pair that contains at least one an element that is 'a' or 'b' and another element 'd, such as [a,d] or [b,d] or the element 'c' and a different element 'd' [c,d]
#now, [a,b] [b,c] [c,d] form the dihedral a-b-c-d OR you end up with [a,b] [b,c] [b,d] that forms an improper a-b-d-c

for i in range(len(bond_info)): ## this should go up to range len(bonds) to include all bonds in the list, but keeping this short helps in debugging
    for j in range(len(bond_info)):
        for k in range(len(bond_info)):
            if ((bonds[i][0] == bonds[j][0] or bonds[i][0] == bonds[j][1] or bonds[i][1] == bonds[j][0] or bonds[i][1] == bonds[j][1]) and (bonds[j][0] == bonds[k][0] or bonds[j][0] == bonds[k][1] or bonds[j][1] == bonds[k][0] or bonds[j][1] == bonds[k][1])):
                if ((bonds[i] != bonds[j]) and (bonds[i] != bonds[k]) and (bonds[j] != bonds[k])):
                    x.append(bonds[i])
                    y.append(bonds[j])
                    z.append(bonds[k])
                    
                    
#################Angles##############################
for i in range(len(x)):
    if x[i][0] == y[i][0] or x[i][0] == y[i][1] or x[i][1] == y[i][0] or x[i][1] == y[i][1] or x[i][0] == z[i][0] or x[i][0] == z[i][1] or x[i][1] == z[i][0] or x[i][1] == z[i][1] or z[i][0] == y[i][0] or z[i][0] == y[i][1] or z[i][1] == y[i][0] or z[i][1] == y[i][1]:
        anx.append(x[i])
        any.append(y[i])
        anz.append(z[i])

ANG = []
for i in range(len(anx)):
    angles=[]
    ANG.append(angles)
    if (anx[i][0]==any[i][0]):
        angles.insert(0,anx[i][1])
        angles.insert(1,anx[i][0])
        angles.insert(2,any[i][1])
    if (anx[i][0]==any[i][1]):
        angles.insert(0,anx[i][1])
        angles.insert(1,anx[i][0])
        angles.insert(2,any[i][0])
    if (anx[i][1]==any[i][0]):
        angles.insert(0,anx[i][0])
        angles.insert(1,anx[i][1])
        angles.insert(2,any[i][1])
    if (anx[i][1]==any[i][1]):
        angles.insert(0,anx[i][0])
        angles.insert(1,anx[i][1])
        angles.insert(2,any[i][0])
  
unique_angles=[]
for angle in ANG:
    if angle not in unique_angles:
        unique_angles.append(angle)
#print(unique_angles)
new_file_ang = open('angles_g.txt','w')
for item in unique_angles:
    value_set = str(item[0:])
    new_file_ang.write(value_set[1:-1]+'\n')
Unique_line_angle = open("angles.txt").readlines()
un_angle = open("unique_angles.txt", 'w').writelines(set(Unique_line_angle))
new_angles = []
for i in unique_angles:
    if (a1 in i and a2 in i):
        new_angles.append(i)
News = open('news.txt','w')
News.write("New angles are :\n")
for i in new_angles:
    value_set = str(i[0:])
    News.write(value_set[1:-1]+'\n')
    
    


#list y always contains the bond pair in the middle of the dihedral 
#Now,we remove impropers from the list and move it to another list, so we have an improper list and a dihedral list
for i in range(len(x)):
    if ((x[i][0] == y[i][0] or x[i][0] == y[i][1] or x[i][1] == y[i][0] or x[i][1] == y[i][1]) and (x[i][0] == z[i][0] or x[i][0] == z[i][1] or x[i][1] == z[i][0] or x[i][1] == z[i][1])):
        imx.append(x[i])
        imy.append(y[i])
        imz.append(z[i])
        indexlist.append(i) # List of indices that have improper triplets

newlist = np.arange(len(x))
newlist = newlist.tolist()
newlist = [x for x in newlist if x not in indexlist] # List of indices that have dihedral triplets

for ii in newlist:
    dix.append(x[ii])
    diy.append(y[ii])
    diz.append(z[ii])


#############Impropers##############################################
IMP=[]
IMPset=[]
for i in range(len(imx)):
    impropers=[]
    IMP.append(impropers)
    impropers.insert(0,imy[i][0])
    impropers.insert(2, imy[i][1])
    if (imx[i][0]==imy[i][0]):
        impropers.insert(1,imx[i][1])
    if (imx[i][1]==imy[i][0]):
        impropers.insert(1,imx[i][0])
    if (imz[i][0]==imy[i][0]):
        impropers.insert(3,imz[i][1])
    if (imz[i][1]==imy[i][0]):
        impropers.insert(3,imz[i][0])

sizeIMP = []                  #keeping only items with 4 values 
for j in IMP:
    if len(j)==4:
        sizeIMP.append(j)
Unique_impropers = []
for k in sizeIMP:
    if k not in Unique_impropers:
        Unique_impropers.append(k)
new_file_im = open('impropers_g.txt','w')
#data_Impropers = set(map(lambda x: tuple(sorted(x)),Unique_impropers))
for item in Unique_impropers:
    value_set = str(item[0:])
    new_file_im.write(value_set[1:-1]+ '\n')
new_impropers = []
for i in Unique_impropers:
    if (a1 in i and a2 in i):
        new_impropers.append(i)
News.write("New Impropers are :\n")
for i in new_impropers:
    value_set = str(i[0:])
    News.write(value_set[1:-1]+'\n')




    
##############Dihedrals############################################
#This impropper Order with ATB FF. First atom is the middle
DIH = []
for i in range(len(dix)):
    dihedrals = []
    DIH.append(dihedrals)
    dihedrals.insert(1,diy[i][0])
    dihedrals.insert(2,diy[i][1])
    if (dix[i][0] == diy[i][0]):
        dihedrals.insert(0,dix[i][1])
    if (dix[i][0] == diy[i][1]):
        dihedrals.insert(3,dix[i][1])
    if (dix[i][1] == diy[i][0]):
        dihedrals.insert(0,dix[i][0])
    if (dix[i][1] == diy[i][1]):
        dihedrals.insert(3,dix[i][0])
    if (diz[i][0] == diy[i][0]):
        dihedrals.insert(0,diz[i][1])
    if (diz[i][0] == diy[i][1]):
        dihedrals.insert(3,diz[i][1])
    if (diz[i][1] == diy[i][0]):
        dihedrals.insert(0,diz[i][0])
    if (diz[i][1] == diy[i][1]):
        dihedrals.insert(3,diz[i][0])

unique_dihedrals = []
for element in DIH:
    if element not in unique_dihedrals:
        unique_dihedrals.append(element)
newfile = open('dihedrals_g.txt', 'w')
for item in unique_dihedrals:
    value_set = str(item[0:])
    newfile.write(value_set[1:-1]+'\n')
new_dihedrals = []
for i in unique_dihedrals:
    if (a1 in i and a2 in i ):
        new_dihedrals.append(i)
News.write("New Dihedrals are :\n")
for i in new_dihedrals:
    value_set = str(i[0:])
    News.write(value_set[1:-1]+'\n')
























        
        
        


