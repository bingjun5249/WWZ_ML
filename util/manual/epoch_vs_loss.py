import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

## Read csv
eee_file = "/home/bjpark/WZG/ML/storage/run_files/storage/180/eee/eee_history.csv"
eem_file = "/home/bjpark/WZG/ML/storage/run_files/storage/144/eem/eem_history.csv"
emm_file = "/home/bjpark/WZG/ML/storage/run_files/storage/144/emm/emm_history.csv"
mmm_file = "/home/bjpark/WZG/ML/storage/run_files/storage/132/mmm/mmm_history.csv"

eee_df = pd.read_csv(eee_file)
eem_df = pd.read_csv(eem_file)
emm_df = pd.read_csv(emm_file)
mmm_df = pd.read_csv(mmm_file)

## Draw acc and loss

# eee channel
eee_df[['train_loss', 'val_loss']].plot()
plt.grid()
plt.text(200,2000,'(eee channel)', fontsize=20)
plt.savefig('eee_loss')
plt.close()

eee_df[['train_accuracy', 'val_accuracy']].plot()
plt.grid()
plt.text(200,2000,'(eee channel)', fontsize=20)
plt.savefig('eee_acc')
plt.close()

# eem channel
eem_df[['train_loss', 'val_loss']].plot()
plt.grid()
plt.text(200,2000,'(eem channel)', fontsize=20)
plt.savefig('eem_loss')
plt.close()

eem_df[['train_accuracy', 'val_accuracy']].plot()
plt.grid()
plt.text(200,2000,'(eem channel)', fontsize=20)
plt.savefig('eem_acc')
plt.close()

# emm channel
emm_df[['train_loss', 'val_loss']].plot()
plt.grid()
plt.text(200,2000,'(emm channel)', fontsize=20)
plt.savefig('emm_loss')
plt.close()

emm_df[['train_accuracy', 'val_accuracy']].plot()
plt.grid()
plt.text(200,2000,'(emm channel)', fontsize=20)
plt.savefig('emm_acc')
plt.close()

# mmm channel
mmm_df[['train_loss', 'val_loss']].plot()
plt.grid()
plt.text(200,2000,'(mmm channel)', fontsize=20)
plt.savefig('mmm_loss')
plt.close()

mmm_df[['train_accuracy', 'val_accuracy']].plot()
plt.grid()
plt.text(200,2000,'(mmm channel)', fontsize=20)
plt.savefig('mmm_acc')
plt.close()

