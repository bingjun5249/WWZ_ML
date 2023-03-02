batch=2048
epoch=200
lr=0.01

python train.py --epoch $epoch --batch $batch --lr $lr
python Eval.py --epoch $epoch --batch $batch --lr $lr

count=`ls -l ../storage/run_files/total/|grep ^d|wc -l`
count=`expr $count + 1`
echo $count


mkdir ../storage/run_files/total/trial$count/

mv total* ../storage/run_files/total/trial$count/

