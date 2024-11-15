from pysimm import system, lmps, forcefield
from subprocess import call, Popen, PIPE
import argparse

template = """
#
# A mixture of four different molecular fragments
#

# All the atoms from diferent molecules will be separated at least 2.0
# Anstroms at the solution.

tolerance 2.0

# The file type of input and output files is XYZ

filetype xyz

# The name of the output file

output OUTPUT_XYZ

# 100 mol1 and mol2 and 200 mol3 molecules will be put in a box
# defined by the minimum coordinates x, y and z = 0. 0. 0. and maximum
# coordinates 40. 40. 40. That is, they will be put in a cube of side
# 40. (the keyword "inside cube 0. 0. 0. 40.") could be used as well.

structure SOLUTE_XYZ 
  number 1
  # center
  fixed 0. 0. 0. 0. 0. 0.
end structure

structure ION_XYZ   
  number N_ION
  inside box -BOX_SIZE -BOX_SIZE -BOX_SIZE BOX_SIZE BOX_SIZE BOX_SIZE 
end structure

structure SOLVENT_XYZ 
  number N_SOLVENT
  inside box -BOX_SIZE -BOX_SIZE -BOX_SIZE BOX_SIZE BOX_SIZE BOX_SIZE
end structure

"""

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', default='H2O_spce_flex.xyz', help='Input Solvent XYZ File')
parser.add_argument('-c', '--counterion', default='ho_opt.xyz', help='Input Ion XYZ File')
parser.add_argument('-x', '--xions', default=100, help='Number of Counter ions')
parser.add_argument('-b', '--boxsize', default=100., help='Box length from center')
parser.add_argument('-n', '--number', required=True, help='Number of solvents')
parser.add_argument('-o', '--output', required=True, help='Output XYZ file')
parser.add_argument('-s', '--solute', required=True, help='Input Solute XYZ file')
args = parser.parse_args()

fname_ion = args.counterion
n_ion = args.xions
fname_solute = args.solute
fname_solvent = args.input
n_solvent = args.number
fname_output = args.output
boxsize = args.boxsize

packmol_inp = template.replace('OUTPUT_XYZ', fname_output).replace('SOLUTE_XYZ', fname_solute).replace('ION_XYZ', \
                  fname_ion).replace('N_ION', str(n_ion)).replace('SOLVENT_XYZ', fname_solvent).replace('N_SOLVENT', \
                  n_solvent).replace('BOX_SIZE', boxsize)

f_temp = 'packmol_temp.inp'
with open(f_temp, 'w') as f:
    f.write(packmol_inp)

import subprocess

command = "packmol < packmol_temp.inp"

# Run the command
process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

# Get the output and errors
output, error = process.communicate()

# Print the output and errors
print("Output:", output.decode())


