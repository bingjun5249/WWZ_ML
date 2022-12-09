import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import sklearn

channel = ['eeee','eeem','eemm','emmm','mmmm']
combine = ['even','odd']

for ch in combine:
	# Data Load
	infile = ch + "_binary.h5" 

	df = pd.read_hdf(infile)

	'''
	# use pandas 
	df_shuffled_pd = df.sample(frac=1).reset_index(drop=True)

	# use numpy 
	df_shuffled_np = df.iloc[np.random.permutation(df.index)].reset_index(drop=True)
	'''
	# use sklearn
	df_shuffled_sk = sklearn.utils.shuffle(df)

	print(df_shuffled_sk)

	df_shuffled_sk.to_hdf(ch + '_binary.h5', key = 'df', mode = 'w')

