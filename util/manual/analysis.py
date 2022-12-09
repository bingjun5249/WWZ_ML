import pandas as pd
from sklearn.metrics import roc_curve, roc_auc_score, confusion_matrix
import matplotlib.pyplot as plt
import numpy as np
from torch import from_numpy

eee_infile = '/home/bjpark/WZG/ML/storage/run_files/storage/180/eee/eee_prediction.csv'
eem_infile = '/home/bjpark/WZG/ML/storage/run_files/storage/144/eem/eem_prediction.csv'
emm_infile = '/home/bjpark/WZG/ML/storage/run_files/storage/144/emm/emm_prediction.csv'
mmm_infile = '/home/bjpark/WZG/ML/storage/run_files/storage/132/mmm/mmm_prediction.csv'

eee_df = pd.read_csv(eee_infile)
eem_df = pd.read_csv(eem_infile)
emm_df = pd.read_csv(emm_infile)
mmm_df = pd.read_csv(mmm_infile)

eee_tpr, eee_fpr, eee_thr = roc_curve(eee_df['label'], eee_df['prediction'], sample_weight=eee_df['weight'], pos_label=0)
eem_tpr, eem_fpr, eem_thr = roc_curve(eem_df['label'], eem_df['prediction'], sample_weight=eem_df['weight'], pos_label=0)
emm_tpr, emm_fpr, emm_thr = roc_curve(emm_df['label'], emm_df['prediction'], sample_weight=emm_df['weight'], pos_label=0)
mmm_tpr, mmm_fpr, mmm_thr = roc_curve(mmm_df['label'], mmm_df['prediction'], sample_weight=mmm_df['weight'], pos_label=0)

eee_auc = roc_auc_score(eee_df['label'], eee_df['prediction'], sample_weight=eee_df['weight'])
eem_auc = roc_auc_score(eem_df['label'], eem_df['prediction'], sample_weight=eem_df['weight'])
emm_auc = roc_auc_score(emm_df['label'], emm_df['prediction'], sample_weight=emm_df['weight'])
mmm_auc = roc_auc_score(mmm_df['label'], mmm_df['prediction'], sample_weight=mmm_df['weight'])

eee_df_bkg = eee_df[eee_df.label == 0]
eee_df_sig = eee_df[eee_df.label == 1]

eem_df_bkg = eem_df[eem_df.label == 0]
eem_df_sig = eem_df[eem_df.label == 1]

emm_df_bkg = emm_df[emm_df.label == 0]
emm_df_sig = emm_df[emm_df.label == 1]

mmm_df_bkg = mmm_df[mmm_df.label == 0]
mmm_df_sig = mmm_df[mmm_df.label == 1]

eee_SF = 10.458301622766731
eem_SF = 20.366929671269794
emm_SF = 18.407198288188823
mmm_SF = 13.76974571541884
lumi = 3000000
genevt = 9899604
xsex = 0.00173

plt.rcParams['figure.figsize'] = (6,6)

eee_hbkg = plt.hist(eee_df_bkg['prediction'], histtype='step', weights=eee_df_bkg['weight'], bins=50,linewidth=3, color='crimson', label='BKG')
eee_hsig = plt.hist(eee_df_sig['prediction'], histtype='step', weights=eee_df_sig['weight'], bins=50,linewidth=3, color='royalblue', label='SIG')

plt.xlabel('DNN score', fontsize=17)
plt.ylabel('Events', fontsize=17)
plt.legend(fontsize=15)
plt.grid()
#plt.yscale('log')
plt.savefig("eee_DNN_score.png")
plt.close()

eem_hbkg = plt.hist(eem_df_bkg['prediction'], histtype='step', weights=eem_df_bkg['weight'], bins=50,linewidth=3, color='crimson', label='BKG')
eem_hsig = plt.hist(eem_df_sig['prediction'], histtype='step', weights=eem_df_sig['weight'], bins=50,linewidth=3, color='royalblue', label='SIG')
plt.xlabel('DNN score', fontsize=17)
plt.ylabel('Events', fontsize=17)
plt.legend(fontsize=15)
plt.grid()
#plt.yscale('log')
plt.savefig("eem_DNN_score.png")
plt.close()

emm_hbkg = plt.hist(emm_df_bkg['prediction'], histtype='step', weights=emm_df_bkg['weight'], bins=50,linewidth=3, color='crimson', label='BKG')
emm_hsig = plt.hist(emm_df_sig['prediction'], histtype='step', weights=emm_df_sig['weight'], bins=50,linewidth=3, color='royalblue', label='SIG')

plt.xlabel('DNN score', fontsize=17)
plt.ylabel('Events', fontsize=17)
plt.legend(fontsize=15)
plt.grid()
#plt.yscale('log')
plt.savefig("emm_DNN_score.png")
plt.close()

mmm_hbkg = plt.hist(mmm_df_bkg['prediction'], histtype='step', weights=mmm_df_bkg['weight'], bins=50,linewidth=3, color='crimson', label='BKG')
mmm_hsig = plt.hist(mmm_df_sig['prediction'], histtype='step', weights=mmm_df_sig['weight'], bins=50,linewidth=3, color='royalblue', label='SIG')

plt.xlabel('DNN score', fontsize=17)
plt.ylabel('Events', fontsize=17)
plt.legend(fontsize=15)
plt.grid()
#plt.yscale('log')
plt.savefig("mmm_DNN_score.png")
plt.close()


plt.plot(eee_fpr, eee_tpr, '.',linewidth=2, label='%s %.3f' % ("auc", eee_auc))
plt.xlim(0, 1.000)
plt.ylim(0, 1.000)
plt.xlabel('False Positive Rate', fontsize=17)
plt.ylabel('True Positive Rate', fontsize=17)
plt.legend(fontsize =17)
plt.savefig("eee_ROC.png")
plt.close()

plt.plot(eem_fpr, eem_tpr, '.',linewidth=2, label='%s %.3f' % ("auc", eem_auc))
plt.xlim(0, 1.000)
plt.ylim(0, 1.000)
plt.xlabel('False Positive Rate', fontsize=17)
plt.ylabel('True Positive Rate', fontsize=17)
plt.legend(fontsize =17)
plt.savefig("eem_ROC.png")
plt.close()

plt.plot(emm_fpr, emm_tpr, '.',linewidth=2, label='%s %.3f' % ("auc", emm_auc))
plt.xlim(0, 1.000)
plt.ylim(0, 1.000)
plt.xlabel('False Positive Rate', fontsize=17)
plt.ylabel('True Positive Rate', fontsize=17)
plt.legend(fontsize =17)
plt.savefig("emm_ROC.png")
plt.close()

plt.plot(mmm_fpr, mmm_tpr, '.',linewidth=2, label='%s %.3f' % ("auc", mmm_auc))
plt.xlim(0, 1.000)
plt.ylim(0, 1.000)
plt.xlabel('False Positive Rate', fontsize=17)
plt.ylabel('True Positive Rate', fontsize=17)
plt.legend(fontsize =17)
plt.savefig("mmm_ROC.png")
plt.close()


eee_N_bkg = eee_hbkg[0]
eee_N_sig = eee_hsig[0]

eem_N_bkg = eem_hbkg[0]
eem_N_sig = eem_hsig[0]

emm_N_bkg = emm_hbkg[0]
emm_N_sig = emm_hsig[0]

mmm_N_bkg = mmm_hbkg[0]
mmm_N_sig = mmm_hsig[0]

#Score = list([round(i*0.02, 2) for i in range(0,50)])

import math
eee_arr_sig, eem_arr_sig, emm_arr_sig, mmm_arr_sig = [],[],[],[]
eem_arr_sig = []

for cut in range(0,len(eee_N_bkg),1):
	eee_sig_integral = sum(eee_N_sig[:cut])
	eee_bkg_integral = sum(eee_N_bkg[:cut])
	if eee_sig_integral + eee_bkg_integral == 0:
		significance = 0
	else:
		significance = eee_sig_integral / math.sqrt(eee_sig_integral + eee_bkg_integral)
	eee_arr_sig.append(significance)
#	print(cut, eee_sig_integral, eee_bkg_integral, significance)

print(eee_arr_sig.index(max(eee_arr_sig)))
print(max(eee_arr_sig))

for cut in range(0,len(eem_N_bkg),1):
        eem_sig_integral = sum(eem_N_sig[:cut])
        eem_bkg_integral = sum(eem_N_bkg[:cut])
        if eem_sig_integral + eem_bkg_integral == 0:
                significance = 0
        else:
                significance = eem_sig_integral / math.sqrt(eem_sig_integral + eem_bkg_integral)
        eem_arr_sig.append(significance)

print(eem_arr_sig.index(max(eem_arr_sig)))
print(max(eem_arr_sig))

for cut in range(0,len(emm_N_bkg),1):
        emm_sig_integral = sum(emm_N_sig[:cut])
        emm_bkg_integral = sum(emm_N_bkg[:cut])
        if emm_sig_integral + emm_bkg_integral == 0:
                significance = 0
        else:
                significance = emm_sig_integral / math.sqrt(emm_sig_integral + emm_bkg_integral)
        emm_arr_sig.append(significance)

print(emm_arr_sig.index(max(emm_arr_sig)))
print(max(emm_arr_sig))

for cut in range(0,len(mmm_N_bkg),1):
        mmm_sig_integral = sum(mmm_N_sig[:cut])
        mmm_bkg_integral = sum(mmm_N_bkg[:cut])
        if mmm_sig_integral + mmm_bkg_integral == 0:
                significance = 0
        else:
                significance = mmm_sig_integral / math.sqrt(mmm_sig_integral + mmm_bkg_integral)
        mmm_arr_sig.append(significance)

print(mmm_arr_sig.index(max(mmm_arr_sig)))
print(max(mmm_arr_sig))
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
