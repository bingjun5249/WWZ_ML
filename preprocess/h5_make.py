import numpy as np
import pandas as pd
#from IPython.display import display
import awkward as ak
import seaborn as sns
import matplotlib.pyplot as plt

# Data load
eeee_infile='/home/bjpark/WWZ/DRAW/baseline/npy/history/cut_final/4e_channel.npy'
eeem_infile='/home/bjpark/WWZ/DRAW/baseline/npy/history/cut_final/3e1m_channel.npy'
eemm_infile='/home/bjpark/WWZ/DRAW/baseline/npy/history/cut_final/2e2m_channel.npy'
emmm_infile='/home/bjpark/WWZ/DRAW/baseline/npy/history/cut_final/1e3m_channel.npy'
mmmm_infile='/home/bjpark/WWZ/DRaw/baseline/npy/gintory/cut_finel/4m_channel.npy'

eeee_data = np.load(eeee_infile,allow_pickle=True)[()]
eeem_data = np.load(eeem_infile,allow_pickle=True)[()]
eemm_data = np.load(eemm_infile,allow_pickle=True)[()]
emmm_data = np.load(emmm_infile,allow_pickle=True)[()]
mmmm_data = np.load(mmmm_infile,allow_pickle=True)[()]

# Arrange data by channel 

eeee = {
	'WWZ' : eeee_data['WWZ'],
	'Z' : eeee_data['Z'],
	'WZ' : eeee_data['WZ'],
	'ZZ' : eeee_data['ZZ'],
	'ZG' : eeee_data['ZG'],
	'WZZ' : eeee_data['WZ'],
	'ZZZ' : eeee_data['ZZZ'],
	'tWZ' : eeee_data['tWZ'],
	'ttbar' : eeee_data['ttbar'],
	'ttbarZ' : eeee_data['ttbarZ'],
}

eeem = {
	'WWZ' : eeem_data['WWZ'],
	'Z' : eeem_data['Z'],
	'WZ' : eeem_data['WZ'],
	'ZZ' : eeem_data['ZZ'],
	'ZG' : eeem_data['ZG'],
	'WZZ' : eeem_data['WZ'],
	'ZZZ' : eeem_data['ZZZ'],
	'tWZ' : eeem_data['tWZ'],
	'ttbar' : eeem_data['ttbar'],
	'ttbarZ' : eeem_data['ttbarZ'],
}

eemm = {
	'WWZ' : eemm_data['WWZ'],
	'Z' : eemm_data['Z'],
	'WZ' : eemm_data['WZ'],
	'ZZ' : eemm_data['ZZ'],
	'ZG' : eemm_data['ZG'],
	'WZZ' : eemm_data['WZ'],
	'ZZZ' : eemm_data['ZZZ'],
	'tWZ' : eemm_data['tWZ'],
	'ttbar' : eemm_data['ttbar'],
	'ttbarZ' : eemm_data['ttbarZ'],
}

emmm = {
	'WWZ' : emmm_data['WWZ'],
	'Z' : emmm_data['Z'],
	'WZ' : emmm_data['WZ'],
	'ZZ' : emmm_data['ZZ'],
	'ZG' : emmm_data['ZG'],
	'WZZ' : emmm_data['WZ'],
	'ZZZ' : emmm_data['ZZZ'],
	'tWZ' : emmm_data['tWZ'],
	'ttbar' : emmm_data['ttbar'],
	'ttbarZ' : emmm_data['ttbarZ'],
}

mmmm = {
	'WWZ' : mmmm_data['WWZ'],
	'Z' : mmmm_data['Z'],
	'WZ' : mmmm_data['WZ'],
	'ZZ' : mmmm_data['ZZ'],
	'ZG' : mmmm_data['ZG'],
	'WZZ' : mmmm_data['WZ'],
	'ZZZ' : mmmm_data['ZZZ'],
	'tWZ' : mmmm_data['tWZ'],
	'ttbar' : mmmm_data['ttbar'],
	'ttbarZ' : mmmm_data['ttbarZ'],
}


# Plotting
lumi = 3000000

EventDict = {
"WWZ" : 10000000,
"Z" : 10200000,
"WZ" : 10000000,
"ZZ" : 10000000,
"ZG" : 10100000,
"WZZ" : 10100000,
"ZZZ" : 10100000,
"tWZ" : 10100000,
"ttbar" : 10000000
"ttbarZ" : 10000000,
}

xsecDict = {
"WWZ" : 0.0003051,
"Z" : 44870,
"WZ" : 26.16,
"ZZ" : 0.04655,
"ZG" : 72.19,
"WZZ" : 0.02785,
"ZZZ" : 0.009669,
"tWZ" : 0.09813,
"ttbar" : 40.288,
"ttbarZ" : 0.002151,
}


pick_cols = []

for i in eem['WWZ'].fields:
	pick_cols.append(i)

def df_make(channel,sum_list):
	for process in channel:
#		process_columns = channel['{0}'.format(process)].fields
		process_columns = channel['{0}'.format(process)][pick_cols].fields
				
		if process == 'WWZ':
			y = np.ones(len(channel['{0}'.format(process)])) * 1
			evt = EventDict['WWZ']
			xsec = xsecDict['WWZ']			
		elif process == 'Z':
			y = np.ones(len(channel['{0}'.format(process)])) * 0
			evt = EventDict['Z']
			xsec = xsecDict['Z']
		elif process == 'ZG':
			y = np.ones(len(channel['{0}'.format(process)])) * 0
			evt = EventDict['ZG']
			xsec = xsecDict['ZG']
		elif process == 'WZ':
			y = np.ones(len(channel['{0}'.format(process)])) * 0
			evt = EventDict['WZ']
			xsec = xsecDict['WZ']
		elif process == 'ZZ':
			y = np.ones(len(channel['{0}'.format(process)])) * 0
			evt = EventDict['ZZ']
			xsec = xsecDict['ZZ']
		elif process == 'WZZ':
			y = np.ones(len(channel['{0}'.format(process)])) * 0
			evt = EventDict['WZZ']
			xsec = xsecDict['WZZ']
		elif process == 'ZZZ':
			y = np.ones(len(channel['{0}'.format(process)])) * 0
			evt = EventDict['ZZZ']
			xsec = xsecDict['ZZZ']
		elif process == 'tWZ':
			y = np.ones(len(channel['{0}'.format(process)])) * 0
			evt = EventDict['tWZ']
			xsec = xsecDict['tWZ']
		elif process == 'ttbar':
			y = np.ones(len(channel['{0}'.format(process)])) * 0
			evt = EventDict['ttbar']
			xsec = xsecDict['ttbar']
		else:
			y = np.ones(len(channel['{0}'.format(process)])) * 0
			evt = EventDict['ttbarZ']
			xsec = xsecDict['ttbarZ']

		data = {'y':y, 'Event':evt, 'xsec':xsec}	
		df = pd.DataFrame(data)	

		for column in process_columns:		
			df[column] = ak.to_pandas(channel['{0}'.format(process)][column])

		lista = df.values.tolist()
		sum_list += lista
		
	return sum_list

sum_list=[]
sum_list = df_make(eeee,sum_list)
sum_list = df_make(eeem,sum_list)
sum_list = df_make(eemm,sum_list)
sum_list = df_make(emmm,sum_list)
sum_list = df_make(mmmm,sum_list

col = ['y', 'Event', 'xsec']

cols = col + eem['WWZ'][pick_cols].fields

df = pd.DataFrame(sum_list, columns=cols)

pd.set_option("display.max_colwidth", 200)

df.to_hdf('tenet.h5', key='df', mode='w')
