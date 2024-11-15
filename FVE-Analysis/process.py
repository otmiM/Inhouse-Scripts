#Author: Mohammed Al Otmi
#Description: This code prepares files for VACUUMMS

import itertools

data = open('../after_21step.lmps','r')

list_of_atoms=[]
append = False
for line in data:
    stripped_line = line.strip()
    if stripped_line =="Atoms # full":
        append=True
        continue
    elif stripped_line =="Velocities":
        append=False
        continue
    elif append:
        list_of_atoms.append(stripped_line.split())
list_of_atoms = [ele for ele in list_of_atoms if ele != []]
list_of_atoms = [[float(float(j)) for j in i] for i in list_of_atoms]







data = open('../after_21step.lmps','r')
pair = open('pair.dat', 'w')
list_of_pairs=[]
append = False
for line in data:
    stripped_line = line.strip()
    if stripped_line =="Pair Coeffs # lj/cut/coul/long":
        append=True
        continue
    elif stripped_line =="Bond Coeffs # harmonic":
        append=False
        continue
    elif append:
        list_of_pairs.append(stripped_line.split())
list_of_pairs = [ele for ele in list_of_pairs if ele != []]
list_of_pairs = [[float(j) for j in i] for i in list_of_pairs]
for i in list_of_pairs:
    pair.write(str(int(i[0]))+" "+str(i[1])+" "+ str(i[2])+'\n')
print(list_of_pairs)   
    
   





corrected = open('Corrected.gfg', 'w')
for i,j in itertools.product(list_of_atoms, list_of_pairs):
    if int(j[0])==int(i[2]):
        print(i[4]," ",i[5]," ",i[6], " ", float(j[1])," ", float(j[2]))
        corrected.write(str(i[4])+"    "+ str(i[5])+"    "+ str(i[6])+ "    "+ str(float(j[2]))+"    "+ str(float(j[1]))+'\n')
    else:
        pass





