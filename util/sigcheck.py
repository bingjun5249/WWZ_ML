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

lumi = 3000000
genevt = 10000000
xsex = 0.0003051

SF = [69.165539, 122.679065, 101.356199, 113.425582, 113.835373]

idx = 0

for ch in combine:

	infile = '/home/bjpark/WWZ/ML/storage/run_files/'+ch+'/'+ch+'_prediction.csv'

	df = pd.read_csv(infile)

	tpr, fpr, thr = roc_curve(df['label'], df['prediction'], sample_weight=df['weight'], pos_label=0)

	auc = roc_auc_score(df['label'], df['prediction'], sample_weight=df['weight'])

	df_bkg = df[df.label == 0]
	df_sig = df[df.label == 1]

	#hbkg = plt.hist(df_bkg['prediction'], histtype='step', weights=df_bkg['weight'], bins=50, linewidth=3, color='crimson', label='BKG')
	#hsig = plt.hist(df_sig['prediction'], histtype='step', weights=df_sig['weight']*5 * lumi * xsex/genevt, bins=50,linewidth=3, color='royalblue', label='Signal')

	#N_bkg = hbkg[0]
	#N_sig = hsig[0]

	#arr_sig = []

	#for cut in range(0,len(N_bkg),1):
	#	sig_integral = sum(N_sig[:cut])
	#	bkg_integral = sum(N_bkg[:cut])
	#	if sig_integral + bkg_integral == 0:
	#		significance = 0
	#	else:
	#		significance = sig_integral / math.sqrt(sig_integral + bkg_integral)
	#	arr_sig.append(significance)
#
#	print(arr_sig.index(max(arr_sig)))
#	print(max(arr_sig))

	plt.rcParams['figure.figsize'] = (8,8)

	hbkg = plt.hist(df_bkg['prediction'], histtype='step', weights=df_bkg['weight']*5/SF[idx], bins=50,linewidth=3, color='crimson', label='Background')
	hsig = plt.hist(df_sig['prediction'], histtype='step', weights=df_sig['weight']*5 * lumi * xsex/genevt, bins=50,linewidth=3, color='royalblue', label='Signal')
	plt.axvline(x=0.82, color='black', linestyle=':', linewidth=2, label='Threshold')
	plt.title("$\sqrt{s}=14$ TeV, L=3000 $fb^{-1}$", fontsize=13, loc='right')
	plt.xlabel('DNN score', fontsize=17)
	plt.ylabel('Expected Number of Events', fontsize=17)
	plt.ylim(0.1, 1000)
	plt.text(0.3, 300, '('+ch+' channel)', fontsize=20)
	plt.legend(fontsize=14, loc='upper left')
	plt.yscale('log')
	plt.savefig(ch+"_Nor_DNN_score.png")
	#plt.show()
	plt.close()


	plt.plot(fpr, tpr, '.',linewidth=2, label='%s %.3f' % ("auc", auc))
	plt.xlim(0, 1.000)
	plt.ylim(0, 1.000)
	plt.xlabel('False Positive Rate', fontsize=17)
	plt.ylabel('True Positive Rate', fontsize=17)
	plt.legend(fontsize =17)
	plt.savefig(ch+"_ROC.png")
	plt.close()


	N_bkg = hbkg[0]
	N_sig = hsig[0]


	Score = list([round(i*0.02, 2) for i in range(0,50)])

	arr_sig = []

	for cut in range(0,len(N_bkg),1):
		sig_integral = sum(N_sig[cut:])
		bkg_integral = sum(N_bkg[cut:])
		if sig_integral + bkg_integral == 0:
			significance = 0
		else:
			significance = sig_integral / math.sqrt(sig_integral + bkg_integral)
		arr_sig.append(significance)
	#	print(cut, sig_integral, bkg_integral, significance)

	print(arr_sig.index(max(arr_sig)))
	print(max(arr_sig))



	plt.rcParams["legend.loc"] = 'lower left'
	plt.title("$\sqrt{s}=14$ TeV, L=3000 $fb^{-1}$", fontsize=13, loc='right')
	plt.plot(list([round(i*0.02,2) for i in range(0,50)]),arr_sig,'--',color='red', label=ch+' channel', linewidth=2)
	plt.xlabel('DNN score',fontsize=25)
	plt.ylabel('Expected Significance',fontsize=25)
	plt.text(0.2, 1, '('+ch+' channel)', fontsize=20)
	plt.legend(prop={'size':14})
	plt.grid(which='major', linestyle='-')
	plt.minorticks_on()
	plt.savefig(ch+'_sig')
	#plt.show()
	plt.close()

	idx += 1
