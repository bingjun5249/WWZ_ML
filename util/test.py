import pandas as pd
from sklearn.metrics import roc_curve, roc_auc_score, confusion_matrix
import matplotlib.pyplot as plt
import numpy as np
from torch import from_numpy

eee_infile = '/x4/cms/dylee/Delphes/ML/Node06_Machine_Learning/mix_ML/storage/128neuron/more/eee/prediction.csv'
eem_infile = '/x4/cms/dylee/Delphes/ML/Node06_Machine_Learning/mix_ML/storage/256neuron/much/eem/prediction.csv'
emm_infile = '/x4/cms/dylee/Delphes/ML/Node06_Machine_Learning/mix_ML/storage/256neuron/much/emm/prediction.csv'
mmm_infile = '/x4/cms/dylee/Delphes/ML/Node06_Machine_Learning/mix_ML/storage/256neuron/much/mmm/prediction.csv'

eee_df = pd.read_csv(eee_infile)
eem_df = pd.read_csv(eem_infile)
emm_df = pd.read_csv(emm_infile)
mmm_df = pd.read_csv(mmm_infile)

eee_cut_df = eee_df[eee_df['prediction'] >= 0.6]
eem_cut_df = eem_df[eem_df['prediction'] >= 0.56]
emm_cut_df = emm_df[emm_df['prediction'] >= 0.7]
mmm_cut_df = mmm_df[mmm_df['prediction'] >= 0.42]

eee_idx = eee_cut_df.iloc[:,[0]].values.flatten()
eee_testset = '/x4/cms/dylee/Delphes/ML/Node06_Machine_Learning/mix_ML/storage/128neuron/more/eee/eee_testset.h5'

eee_test_df = pd.read_hdf(eee_testset)


'''
#emm_idx = emm_cut_df.index
#mmm_idx = mmm_cut_df.index

eee_testset = '/x4/cms/dylee/Delphes/ML/Node06_Machine_Learning/mix_ML/storage/128neuron/more/eee/eee_testset.h5'
#eem_testset = '/x4/cms/dylee/Delphes/ML/Node06_Machine_Learning/mix_ML/storage/256neuron/much/eem/eem_testset.h5'
#emm_testset = '/x4/cms/dylee/Delphes/ML/Node06_Machine_Learning/mix_ML/storage/256neuron/much/emm/emm_testset.h5'
#mmm_testset = '/x4/cms/dylee/Delphes/ML/Node06_Machine_Learning/mix_ML/storage/256neuron/much/mmm/mmm_testset.h5'

eee_test_df = pd.read_hdf(eee_testset)
#eem_test_df = pd.read_hdf(eem_testset)
#emm_test_df = pd.read_hdf(emm_testset)
#mmm_test_df = pd.read_hdf(mmm_testset)

#eee_after = eee_test_df[eee_test_df.index == eee_idx]

#print(eee_test_df)
#print(eee_after)
'''

