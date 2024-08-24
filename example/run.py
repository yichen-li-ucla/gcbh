import os,sys
from ase.io import read
from run_gcbh import GrandCanonicalBasinHopping
from pygcga import mutation_atoms

path = os.path.realpath("../gcbh/")
sys.path.insert(0, path)
atoms = read('Current_atoms.traj')
bh_run = GrandCanonicalBasinHopping(
    atoms=atoms,
    bash_script="optimize.sh",
    files_to_copied=["opt.py"],
    restart=True,
    chemical_potential="chemical_potentials.dat"
)
bh_run.add_modifier(mutation_atoms, name='mutation', weight=3.0)
bh_run.run(1000)