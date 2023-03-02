count=`ls -l ../storage/run_files/total/|grep ^d|wc -l`
count=`expr $count + 1`
echo $count


mkdir ../storage/run_files/total/trial$count/

mv total* ../storage/run_files/total/trial$count/
