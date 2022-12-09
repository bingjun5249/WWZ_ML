import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--trial', type=str, default='0', help='--trial TRIAL NUMBER')
args = parser.parse_args()

trial = args.trial

channel = ['eeee','eeem','eemm','emmm','mmmm']
combine = ['even','odd']

for ch in combine:
	## Read csv
	ch_file = "/home/bjpark/WWZ/ML/storage/run_files/" + ch + "/" + ch + "_history.csv"

	df = pd.read_csv(ch_file)

	## Draw acc and loss

	# eee channel
	df[['train_loss', 'val_loss']].plot()
	plt.grid()
	plt.text(200,2000,'('+ch+' channel)', fontsize=20)
	plt.savefig(''+ch+'_loss')
	plt.close()

	df[['train_accuracy', 'val_accuracy']].plot()
	plt.grid()
	plt.text(200,2000,'('+ch+' channel)', fontsize=20)
	plt.savefig(''+ch+'_acc')
	plt.close()


