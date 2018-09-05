import pubchempy
import csv
import os
import datetime
import pandas as pd
PATH = '.'
info = os.path.join(PATH, 'Information_Files')
smiles_csv = os.path.join(info, 'enamine - Copy.csv')

# x = open(smiles_csv, 'r')
# csv_ = csv.reader(x)
# smiles = []
# for item in csv_:
#     smiles.append(item[0])

# needs to change if program breaks again
# del smiles[:10359]

# debugging + me being lazy. Change to false to turn it off.
# do_it = False
# if do_it:
#     count = 0
#     for item in smiles:
#         count += 1
#         try:
#             x = pubchempy.get_compounds(item, namespace='smiles')[0].cactvs_fingerprint
#             y = list(x)
#             with open('pubchem_fp.csv', 'a') as f:
#                 writer = csv.writer(f)
#                 writer.writerow((item, y))
#         except:
#             with open('pubchem_fp.csv', 'a') as f:
#                 writer = csv.writer(f)
#                 writer.writerow((item, 'QUERY FAILED'))
#         if count%1000 == 0:
#             print(datetime.datetime.now())
#     x.close()

df = pd.read_csv('pubchem_fp.csv')


stuff = {'1','0',1,0}

def remove_puncuation(column):
    new_column = []
    for item in column:
        if item in stuff:
            new_column.append(int(item))
    if not new_column:
        return None
    return new_column

df['fingerprints'] = df['fingerprints'].apply(remove_puncuation)

