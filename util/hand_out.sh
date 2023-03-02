count=`ls -l ../storage/util_files/total/|grep ^d|wc -l`
count=`expr $count + 1`

echo $count

mkdir ../storage/util_files/total/trial$count/


mv *.png ../storage/util_files/total/trial$count/
