import numpy as np
import pandas as pd

channel = ['eeee','eeem','eemm','emmm','mmmm']
combine = ['even','odd']

for ch in combine:
	infile = ch + "_binary.h5"

	df = pd.read_hdf(infile)

	print(df)

	print(df.columns)
