import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

channel = ['eeee','eeem','eemm','emmm','mmmm']
combine = ['even','odd']
total = ['total']

def Load(cha):

	infile = cha+'_binary.h5'
	df = pd.read_hdf(infile)

	# Add necessary columns
	df['weight'] = (df['xsec'] * 3000000)/df['Event']
	sigY = df[df['y'] == 1]['weight'].sum(axis = 0, skipna = False)
	bkgY = df[df['y'] == 0]['weight'].sum(axis = 0, skipna = False)

	sf = sigY/bkgY

	data = []

	for i in df['y']:
	
		if i ==1:
			data.append(1)

		else:
			data.append(sf)

	
	df['SF'] = data
	
	signal_N = len(df['weight'][df['y'] == 1])
	bkg_N = df['weight'][df['y'] == 0].sum()
	SF = signal_N / bkg_N

	print("{0} signal : {1}, bkg : {2}, SF : {3}".format(cha, signal_N, bkg_N, SF))

	df['weight'][df['y'] == 1] = 1
	df['weight'][df['y'] == 0] = df['weight'][df['y'] == 0] * SF

	df_weight = df['weight']
	df = df.drop(['weight', 'SF'], axis=1)

	#pt1 = df['fstlep_pt']
	pt2 = df['sndlep_pt']
	pt3 = df['trdlep_pt']
	#pt4 = df['frtlep_pt']

	eta1 = df['fstlep_eta']
	eta2 = df['sndlep_eta']
	eta3 = df['trdlep_eta']
	eta4 = df['frtlep_eta']

	phi1 = df['fstlep_phi']
	phi2 = df['sndlep_phi']
	phi3 = df['trdlep_phi']
	phi4 = df['frtlep_phi']

	flep_mass = df['fourlep_mass']
	#flep_pt = df['fourlep_pt']

	#dimass = df['dilep_mass']
	#wmass = df['wleps_mass']

	#met = df['MET_MET']
	mphi = df['MET_phi']

	#mt2 = df['MT2']
	jetpt = df['jet_pt']
	#HT = df['HT']
	

	# Remove unnecessary columns
	df = df.drop(['sndlep_pt','trdlep_pt','fstlep_eta','sndlep_eta','trdlep_eta','frtlep_eta','fourlep_mass','fstlep_phi','sndlep_phi','trdlep_phi','frtlep_phi','MET_phi','jet_pt','jet_btag'], axis=1)#,'fourlep_pt','wleps_mass','HT'], axis=1)

	df['sndlep_pt'] = pt2
	df['trdlep_pt'] = pt3

	df['jet_pt'] = jetpt
	df['fourlep_mass'] = flep_mass
	df['fstlep_eta'] = eta1
	df['sndlep_eta'] = eta2
	df['trdlep_eta'] = eta3
	df['frtlep_eta'] = eta4

	df['fstlep_phi'] = phi1
	df['sndlep_phi'] = phi2
	df['trdlep_phi'] = phi3
	df['frtlep_phi'] = phi4
	df['MET_phi'] = mphi
	#df['fourlep_pt'] = flep_pt
	#df['wleps_mass'] = wleps_mass
	#df['HT'] = HT
	df['weight'] = df_weight

	print(df)

	df.to_hdf('{0}_binary.h5'.format(cha), key = 'df', mode = 'w')

	return df
Load(total[0])

'''
Load(channel[0])
Load(channel[1])
Load(channel[2])
Load(channel[3])
Load(channel[4])


'''
