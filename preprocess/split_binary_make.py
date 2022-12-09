import numpy as np
import pandas as pd
#from IPython.display import display
import awkward as ak
import seaborn as sns
import matplotlib.pyplot as plt

channel = ['eeee','eeem','eemm','emmm','mmmm']
combine = ['even','odd']

# Plotting
lumi = 3000000

EventDict = {
"WWZ" : 10000000,
"Z" : 10200000,
"ZG" : 10100000,
"WZ" : 10000000,
"ZZ" : 10000000,
"WZZ" : 10100000,
"ZZZ" : 10100000,
"tWZ" : 10100000,
"ttbar" : 10000000,
"ttbarZ" : 10000000
}

xsecDict = {
"WWZ" : 0.0003051,
"Z" : 44870,
"ZG" : 72.19,
"WZ" : 26.16,
"ZZ" : 0.04655,
"WZZ" : 0.02785,
"ZZZ" : 0.009669,
"tWZ" : 0.09813,
"ttbar" : 40.288,
"ttbarZ" : 0.002151,
}

def df_make(channel,sum_list):
	for process in channel:
#		process_columns = channel['{0}'.format(process)].fields
#		process_columns = channel['{0}'.format(process)][pick_cols].fields
		process_columns = pick_cols
				
		if process == 'WWZ':
			y = np.ones(len(channel['{0}'.format(process)]['dilep_mass'])) * 1
			evt = EventDict['WWZ']
			xsec = xsecDict['WWZ']
		elif process == 'Z':
			if len(channel['{0}'.format(process)]) == 0: continue
			y = np.ones(len(channel['{0}'.format(process)]['dilep_mass'])) * 0
			evt = EventDict['Z']
			xsec = xsecDict['Z']
		elif process == 'ZG':
			if len(channel['{0}'.format(process)]) == 0: continue
			y = np.ones(len(channel['{0}'.format(process)]['dilep_mass'])) * 0
			evt = EventDict['ZG']
			xsec = xsecDict['ZG']
		elif process == 'WZ':
			if len(channel['{0}'.format(process)]) == 0: continue
			y = np.ones(len(channel['{0}'.format(process)]['dilep_mass'])) * 0
			evt = EventDict['WZ']
			xsec = xsecDict['WZ']
		elif process == 'ZZ':
			if len(channel['{0}'.format(process)]) == 0: continue
			y = np.ones(len(channel['{0}'.format(process)]['dilep_mass'])) * 0
			evt = EventDict['ZZ']
			xsec = xsecDict['ZZ']
		elif process == 'WZZ':
			if len(channel['{0}'.format(process)]) == 0: continue
			y = np.ones(len(channel['{0}'.format(process)]['dilep_mass'])) * 0
			evt = EventDict['WZZ']
			xsec = xsecDict['WZZ']
		elif process == 'ZZZ':
			if len(channel['{0}'.format(process)]) == 0: continue
			y = np.ones(len(channel['{0}'.format(process)]['dilep_mass'])) * 0
			evt = EventDict['ZZZ']
			xsec = xsecDict['ZZZ']
		elif process == 'tWZ':
			if len(channel['{0}'.format(process)]) == 0: continue
			y = np.ones(len(channel['{0}'.format(process)]['dilep_mass'])) * 0
			evt = EventDict['tWZ']
			xsec = xsecDict['tWZ']
		elif process == 'ttbar':
			if len(channel['{0}'.format(process)]) == 0: continue
			y = np.ones(len(channel['{0}'.format(process)]['dilep_mass'])) * 0
			evt = EventDict['ttbar']
			xsec = xsecDict['ttbar']
		else:
			y = np.ones(len(channel['{0}'.format(process)]['dilep_mass'])) * 0
			evt = EventDict['ttbarZ']
			xsec = xsecDict['ttbarZ']

		data = {'y':y, 'Event':evt, 'xsec':xsec}	
		df = pd.DataFrame(data)	

		for column in process_columns:		
			df[column] = ak.to_pandas(channel['{0}'.format(process)][column])

		lista = df.values.tolist()
		sum_list += lista
		
	return sum_list


for ch in combine:


	# Data load
	infile='/home/bjpark/WWZ/ML/npy/MLnpy/combine/'+ch+'_channel.npy'

	data = np.load(infile,allow_pickle=True)[()]

	# Arrange data by channel 

	ch_name = {
		'WWZ' : data['WWZ'],
		'Z' : data['Z'],
		'ZG' : data['ZG'],
		'WZ' : data['WZ'],
		'ZZ' : data['ZZ'],
		'WZZ' : data['WZZ'],
		'ZZZ' : data['ZZZ'],
		'tWZ' : data['tWZ'],
		'ttbar' : data['ttbar'],
		'ttbarZ' : data['ttbarZ'],
	}





	pick_cols = []

	for i in ch_name['WWZ'].keys():
		if 'lep' in i:
			pick_cols.append(i)
		if 'MET' in i:
			pick_cols.append(i)
		if 'MT' in i:
			pick_cols.append(i)
		if 'jet' in i:
			pick_cols.append(i)
		if 'HT' in i:
			pick_cols.append(i)

	print(pick_cols)


	ch_list = []
	ch_list = df_make(ch_name,ch_list)

	col = ['y', 'Event', 'xsec']

	cols = col + pick_cols

	ch_df = pd.DataFrame(ch_list, columns=cols)

	pd.set_option("display.max_colwidth", 200)

	ch_df.to_hdf(ch+'_binary.h5', key='df', mode='w')

	print(ch_df)

