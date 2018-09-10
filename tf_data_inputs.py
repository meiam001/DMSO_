import pandas as pd
import numpy as np
import pickle

def undersampled_data(df_i,df_s, descriptor='fingerprints', n=150):
    """
    Feed function for model. Undersampled, randomly pickes 100 insoluble and 100 soluble compounds
    """
    insol = df_i.sample(n=n)
    sol = df_s.sample(n=n)
    
    df = pd.concat([insol, sol])
    df = df.sample(frac=1)
    
    fprints = np.array(list(df[descriptor]), dtype='int32')
    labels = np.array(list(df['Solubility']), dtype='int32')
    return fprints, labels

def entire_df_input_fprint(valid_set, descriptor='fingerprints'):
    features = np.array(list(valid_set[descriptor]))
    labels = np.array(list(valid_set['Solubility']))
    return features, labels
	
def random_sample(df, descriptor='fingerprints', n=150):
    random_sample = df.sample(n=n*2)
    fprints = np.array(list(random_sample[descriptor]), dtype='int32')
    labels = np.array(list(random_sample['Solubility']), dtype='int32')
    return fprints, labels