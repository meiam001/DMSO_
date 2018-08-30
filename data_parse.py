import pandas as pd
import os
import numpy as np
from rdkit import Chem
from rdkit.Chem import AllChem
import pickle
# import pubchempy

PATH = os.getcwd()
data_csv = 'Information_Files\\enamine.csv' 

class dmso:
    """
    Class used to easily parse dmso data set into fingerprints and one-hot encoded
    categorical labels
    """
    def __init__(self):
        self.mapping = None
        self.data = None

    def obtain_data(self, morgan=False, maccs=False, pubchem=False,
                    categorical_to_onehot=True, nbits = 1024):
        """
        The meat and cheese!
        Opens the data set and transforms it as desired.
        :param fingerprint: Set to False to prevent smiles -> fingerprint conversion
        :param categorical_to_onehot: Set to False to prevent label strings -> one hot conversion
        :return: Stores
        """
        self.nbits = nbits
        self.data = pd.read_csv(data_csv)
        if categorical_to_onehot:
            self.mapping = self.one_hot(self.data['Solubility'])
            self.data['Solubility'] = self.data['Solubility'].map(self.mapping)
        if morgan:
            self.data['fingerprints'] = self.data['SMILES'].apply(self.morgan)
        elif maccs:
            self.data['fingerprints'] = self.data['SMILES'].apply(self.maccs)
        # elif pubchem:
        #     self.data['fingerprints'] = self.data['SMILES'].apply(self.pubchem)

    def one_hot(self, column):
        """
        One hot encodes a column of arbitrary categories
        :param column: a pandas dataframe
        :return: a dict mapping each category to its respective list
        ex: for the two categories ['Soluble', 'Insoluble'] this function will return
        {'Soluble':array([0,1]), 'Insoluble': array([1,0])}
        """
        values = set(column)
        values = sorted(list(values))
        ints = [c for c, _ in enumerate(values)]
        number_values = len(values)
        int_map = {a: ints[c] for c, a in enumerate(values)}
        for thingy in int_map:
            zeroes = np.zeros(number_values, dtype='int32')
            zeroes[int_map[thingy]] = 1
            int_map[thingy] = zeroes
        return int_map

    def morgan(self, column):
        x = Chem.MolFromSmiles(column)
        y = list(AllChem.GetMorganFingerprintAsBitVect(x, 2, self.nbits))
        return y

    def maccs(self, column):
        x = Chem.MolFromSmiles(column)
        y = list(AllChem.GetMACCSKeysFingerprint(x))
        return y

    # def pubchem(self, column):
    #     try:
    #         x = pubchempy.get_compounds(column, namespace='smiles')[0].cactvs_fingerprint
    #         y = list(x)
    #     except:
    #         print('lol')
    #         return None
    #     return y

if __name__== '__main__':
    nbits = 1024
    if 'morgan_df_{}.p'.format(nbits) not in os.listdir(os.getcwd()):
        x = dmso()
        x.obtain_data(morgan=True, nbits=nbits)
        print('done yo')
        pickle.dump(x.data, open('Fingerprints\\morgan_df_{}.p'.format(nbits), 'wb+'))

    if 'maccs_df.p' not in os.listdir(os.getcwd()):
        x = dmso()
        x.obtain_data(maccs=True)
        pickle.dump(x.data, open('Fingerprints\\maccs_df.p', 'wb+'))
#
#
    # del x
    # if 'pubchem_df.p' not in os.listdir(os.getcwd()):
    #     x = dmso()
    #     x.obtain_data(pubchem=True)
    #     pickle.dump(x, open('pubchem_df.p', 'wb+'))
