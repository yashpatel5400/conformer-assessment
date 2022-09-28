from rdkit import Chem
from rdkit.Chem import AllChem

import os
import numpy as np
import copy
import pickle
import pandas as pd

data = pd.read_csv("data/test_smiles.csv").values

smiles_to_mols = {}
for data_row in data:
    smiles, true_num_confs, _ = data_row
    num_confs = 2 * true_num_confs
    mol = Chem.MolFromSmiles(smiles)
    if mol:
        mol = Chem.AddHs(mol)
    
    etkdg_mol = copy.deepcopy(mol)
    etkdg_mol.RemoveAllConformers()
    AllChem.EmbedMultipleConfs(etkdg_mol, numConfs=num_confs)
    AllChem.MMFFOptimizeMoleculeConfs(etkdg_mol, nonBondedThresh=10., maxIters=500)
    
    confs = []
    for i in range(num_confs):
        conf = copy.deepcopy(etkdg_mol)
        [conf.RemoveConformer(j) for j in range(num_confs) if j != i]
        confs.append(conf)
    smiles_to_mols[smiles] = confs
    print(f"Completed: {smiles}")

with open("etkdg.pkl", "wb") as f:
    pickle.dump(smiles_to_mols, f)