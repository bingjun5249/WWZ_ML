count=`ls -l ../storage/run_files/total/|grep ^d|wc -l`
count=`expr $count - 2`
python analysis.py --trial $count
python epoch_vs_loss.py --trial $count
python sigcheck.py --trial $count

