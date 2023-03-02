import pandas as pd
from sklearn.metrics import roc_curve, roc_auc_score, confusion_matrix
import matplotlib.pyplot as plt
import numpy as np
from torch import from_numpy
import math

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--trial', type=str, default='0', help='--trial TRIAL NUMBER')
args = parser.parse_args()

trial = args.trial

channel = ['eeee','eeem','eemm','emmm','mmmm']
combine = ['even','odd']
total = ['total']

for ch in total:

	infile = '/home/bjpark/WWZ/ML/DNN/storage/run_files/'+ch+'/trial'+trial+'/'+ch+'_prediction.csv'

	df = pd.read_csv(infile)

	tpr, fpr, thr = roc_curve(df['label'], df['prediction'], sample_weight=df['weight'], pos_label=0)

	auc = roc_auc_score(df['label'], df['prediction'], sample_weight=df['weight'])

	df_bkg = df[df.label == 0]
	df_sig = df[df.label == 1]

	#eee_SF = 10.458301622766731
	#eem_SF = 20.366929671269794
	#emm_SF = 18.407198288188823
	#mmm_SF = 13.76974571541884
	lumi = 3000000 
	genevt = 10000000
	xsex = 0.0003051

	plt.rcParams['figure.figsize'] = (8,6)
	plt.ylim(0,105000)

	hbkg = plt.hist(df_bkg['prediction'], histtype='step', weights=df_bkg['weight'], bins=50,linewidth=3, color='crimson', label='BKG')
	hsig = plt.hist(df_sig['prediction'], histtype='step', weights=df_sig['weight'], bins=50,linewidth=3, color='royalblue', label='SIG')

	plt.xlabel('DNN score', fontsize=17)
	plt.ylabel('Events', fontsize=17)
#	plt.axvline(x=0.90, color='black', linestyle=':', linewidth=2, label='Threshold')
	plt.legend(fontsize=15)
	plt.grid()
	#plt.yscale('log')
	plt.savefig(ch + "_DNN_score.png")
	plt.close()

	hbkg = plt.hist(df_bkg['prediction'], histtype='step', weights=df_bkg['weight'], bins=50,linewidth=3, color='crimson', label='BKG')
	hsig = plt.hist(df_sig['prediction'], histtype='step', weights=df_sig['weight'], bins=50,linewidth=3, color='royalblue', label='SIG')
	plt.xlabel('DNN score', fontsize=17)
	plt.ylabel('Events', fontsize=17)
	plt.axvline(x=0.90, color='black', linestyle=':', linewidth=2, label='Threshold')
	plt.legend(fontsize=15)
	plt.grid()
	#plt.yscale('log')
	plt.savefig(ch + "_DNN_score_thr.png")
	plt.close()




	plt.plot(fpr, tpr, '.',linewidth=2, label='%s %.3f' % ("auc", auc))
	plt.xlim(0, 1.000)
	plt.ylim(0, 1.000)
	plt.xlabel('False Positive Rate', fontsize=17)
	plt.ylabel('True Positive Rate', fontsize=17)
	plt.legend(fontsize =17)
	plt.savefig(ch + "_ROC.png")
	plt.close()



	N_bkg = hbkg[0]
	N_sig = hsig[0]

	#Score = list([round(i*0.02, 2) for i in range(0,50)])

	#eee_arr_sig, eem_arr_sig, emm_arr_sig, mmm_arr_sig = [],[],[],[]
	arr_sig = []

	for cut in range(0,len(N_bkg),1):
		sig_integral = sum(N_sig[:cut])
		bkg_integral = sum(N_bkg[:cut])
		if sig_integral + bkg_integral == 0:
			significance = 0
		else:
			significance = sig_integral / math.sqrt(sig_integral + bkg_integral)
		arr_sig.append(significance)
	#	print(cut, eee_sig_integral, eee_bkg_integral, significance)

	print(arr_sig.index(max(arr_sig)))
	print(max(arr_sig))

'''
plt.rcParams["legend.loc"] = 'lower left'
plt.plot(list([round(i*0.02,2) for i in range(0,50)]),eee_arr_sig,'-o',color='royalblue')
plt.xlabel('DNN score',fontsize=25)
plt.ylabel('Significance',fontsize=25)
plt.legend(prop={'size':14})
plt.grid(which='major', linestyle='-')
plt.minorticks_on()
plt.savefig('eee_sig')
plt.close()

plt.rcParams["legend.loc"] = 'lower left'
plt.plot(list([round(i*0.02,2) for i in range(0,50)]),eem_arr_sig,'-o',color='royalblue')
plt.xlabel('DNN score',fontsize=25)
plt.ylabel('Significance',fontsize=25)
plt.legend(prop={'size':14})
plt.grid(which='major', linestyle='-')
plt.minorticks_on()
plt.savefig('eem_sig')
plt.close()

plt.rcParams["legend.loc"] = 'lower left'
plt.plot(list([round(i*0.02,2) for i in range(0,50)]),emm_arr_sig,'-o',color='royalblue')
plt.xlabel('DNN score',fontsize=25)
plt.ylabel('Significance',fontsize=25)
plt.legend(prop={'size':14})
plt.grid(which='major', linestyle='-')
plt.minorticks_on()
plt.savefig('emm_sig')
plt.close()

plt.rcParams["legend.loc"] = 'lower left'
plt.plot(list([round(i*0.02,2) for i in range(0,50)]),mmm_arr_sig,'-o',color='royalblue')
plt.xlabel('DNN score',fontsize=25)
plt.ylabel('Significance',fontsize=25)
plt.legend(prop={'size':14})
plt.grid(which='major', linestyle='-')
plt.minorticks_on()
plt.savefig('mmm_sig')
plt.close()

'''
