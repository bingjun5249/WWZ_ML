batch=2048
epoch=200
lr=0.01

python train.py --epoch $epoch --batch $batch --lr $lr
python Eval.py --epoch $epoch --batch $batch --lr $lr


#source hand_out.sh
