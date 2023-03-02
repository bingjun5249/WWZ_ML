trial=$1

python analysis.py --trial $trial
python epoch_vs_loss.py --trial $trial
python sigcheck.py --trial $trial
