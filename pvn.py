#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 16:26:10 2018

@author: Bin Wang
"""

import numpy as np
from docopt import docopt
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def load_vocabulary(path):
    '''
    Load vocabulary and index for existing method
    '''
    with open(path) as f:
        vocab = [line.strip().split()[0] for line in f if len(line) > 200]
    return dict([(a, i) for i, a in enumerate(vocab)]), vocab

def load_vectors(path):
    '''
    Load vector for existing method
    '''
    vector = []
    with open(path) as f:
        for line in f:
            if len(line) > 200:
                single_line = line.strip().split()
                single_line = single_line[1:]
                vector.append(single_line)
    np_vector = np.asarray(vector)
    return np_vector

def PNV():
    '''
    Load and save file
    '''
    args = docopt("""
    Usage:
        pvn.py <baseline_path> <result_txt> <PVN_dims>
    
    """)
    
    baseline_path = args['<baseline_path>']
    result_txt = args['<result_txt>']

    PVN_dims = int(args['<PVN_dims>'])
    print("PVN_dims: ", PVN_dims)


    print("Load vocabualary and vectors...")
    print("This might take some time...")
    _, vocab = load_vocabulary(baseline_path)
    np_vector = load_vectors(baseline_path).astype(np.float)


    # PNV processing
    print("PNV processing...")
    #import pdb; pdb.set_trace()
    np_vector = np_vector - np.mean(np_vector,0)
    pca = PCA(n_components=300)
    pca.fit(np_vector)
    U1 = pca.components_
    explained_variance = pca.explained_variance_
    # Removing Projections on Top Components
    z = []
    for i, x in enumerate(np_vector):
        for j,u in enumerate(U1[0:PVN_dims]):
            ratio = (explained_variance[j]-explained_variance[PVN_dims]) / explained_variance[j]
            x = x - ratio*np.dot(u.transpose(),x)*u
        z.append(x)
    np_vector = np.asarray(z)
   
    # Plot processed variance graph
    pca2 = PCA(n_components=300)
    pca2.fit(np_vector)
    explained_variance2 = pca2.explained_variance_

    line1, = plt.plot(explained_variance[:30], marker='o', linestyle='--',label='Original SGNS')
    line2, = plt.plot(explained_variance2[:30], marker='*', label='After PNA')
    plt.xlabel('Principal Components')
    plt.ylabel('Variance Explained')
    
    plt.legend([line1, line2], ["Original SGNS", "After PVN"])
    print('Close figure to continue.')
    plt.show()
    print('Continue computing...')

    # Save result file
    with open(result_txt, 'w') as f:
         f.write(str(np_vector.shape[0]))
         f.write(' ')
         f.write(str(np_vector.shape[1]))
         f.write('\n')
         for i, items in enumerate(vocab):
             f.write("%s" % items)
             current_vector = np_vector[i,:]
             for _, value in enumerate(current_vector):
                 f.write(' ')
                 f.write(str(np.float32(value)))
             f.write('\n')
         f.close()
    print("Processed vector file Saved.")
    
if __name__ == "__main__":
    PNV()