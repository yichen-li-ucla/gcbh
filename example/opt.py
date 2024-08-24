from ase.io import read, write
from ase.calculators.vasp import Vasp
import os, sys
import numpy as np

atoms = read('input.traj')

ldaul = [2, -1, -1]
ldauu = [3.5, 0.0, 0.0]
ldauj = [0.0, 0.0, 0.0]

calc = Vasp(
    ldau=True,
    lmaxmix=4,
    lasph=True,
    ldaul=ldaul,
    ldauu=ldauu,
    ldauj=ldauj,
    lwave=False,
    lcharg=False,
    gga='PE',
    encut=400,
    ismear=0,
    sigma=0.1,
    ediff=1e-5,
    nelm=200,
    npar=4,
    ivdw=4,
    lreal='Auto',
    isif=2,
    ibrion=2,
    nsw=1000,
    ediffg=-0.05,
    amix=0.2,
    amix_mag=0.8,
    bmix=0.0001,
    bmix_mag=0.0001,
    maxmix=50,
    ldipol=True,
    idipol=3,
    lnoncollinear=False,
    setups='recommended',
    kpts=[1, 1, 1]
)
atoms.calc = calc

try:
    atoms.get_potential_energy()
    write("optimized.traj", atoms)
except Exception as e:
    print("Optimization failed:", e)