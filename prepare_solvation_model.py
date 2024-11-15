from pysimm import system, lmps, forcefield
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', required=True, help='Input solvent LAMMPS File')
parser.add_argument('-n', '--number', required=True, help='Number of solvents')
parser.add_argument('-o', '--output', required=True, help='Output LAMMPS data file')
parser.add_argument('-r', '--reference', required=True, help='Input reference LAMMPS data file')
args = parser.parse_args()

s = system.read_lammps(args.reference)
s.forcefield = 'gaff2'

s3 = system.read_lammps('ho_opt.lmps')
s3.ff_class = 2
s3.forcefield = 'gaff2'
s3.pair_style = 'lj'
s3.bond_style = 'harmonic'
s3.angle_style = 'harmonic'
s3.dihedral_style = 'fourier'
s4 = system.read_lammps(args.input)

n_solvent = 100 * int(args.number)
s_ = system.replicate([s3, s4], [100, n_solvent)], s_=s, density=None)
s_.write_lammps(args.output)

