import numpy as np
import pandas as pd
import pytraj as pt
import os

def getFrameInfo(timeframe):
    filepathDCD1 = '/home/mhanowar/Downloads/traj1.dcd'
    filepathDCD2 = '/home/mhanowar/Downloads/traj2.dcd'
    filepathDCD3 = '/home/mhanowar/Downloads/traj3.dcd'
    filepathDCD4 = '/home/mhanowar/Downloads/traj4.dcd'

    filepathPRM = '/home/mhanowar/Downloads/4csp_no_sol.prmtop'

    if timeframe < 200000:
        fname = filepathDCD1
    elif timeframe >= 200000 and timeframe < 400000:
        timeframe = timeframe - 200000
        fname = filepathDCD2
    elif timeframe >= 400000 and timeframe < 600000:
        timeframe = timeframe - 400000
        fname = filepathDCD3
    elif timeframe >= 600000 and timeframe < 800000:
        timeframe = timeframe - 600000
        fname = filepathDCD4



    return pt.load(fname, filepathPRM, frame_indices=[timeframe])


def giveDF(frameNumber):
    traj = getFrameInfo(10)


    # Extract topology information
    topology = traj.topology

    # Extract atom names, residue names, residue IDs, and atom types
    atom_names = []
    residue_names = []
    residue_ids = []
    atom_types = []
    for atom in topology.atoms:
        atom_names.append(atom.name)
        residue = topology.residue(atom.resid)
        residue_names.append(residue.name)
        residue_ids.append(residue.index + 1)
        atom_types.append(atom.type)

    # Extract coordinates for the specified frame
    xyz = traj.xyz

    # Flatten the xyz coordinates
    xyz_flat = xyz.reshape(-1, 3)

    # Create a DataFrame
    df = pd.DataFrame(xyz_flat, columns=['X', 'Y', 'Z'])
    df['Atom_Name'] = atom_names
    df['Molecule_Name'] = residue_names
    df['Molecule_ID'] = residue_ids
    df['Atom_Type'] = atom_types

    return df

display(giveDF(10))