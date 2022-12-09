count=`ls -l ../storage/run_files/|grep ^d|wc -l`
count=`expr $count - 1`
echo $count


mkdir ../storage/run_files/$count/
mkdir ../storage/run_files/$count/eee
mkdir ../storage/run_files/$count/eem
mkdir ../storage/run_files/$count/emm
mkdir ../storage/run_files/$count/mmm

mv eee* ../storage/run_files/$count/eee
mv eem* ../storage/run_files/$count/eem
mv emm* ../storage/run_files/$count/emm
mv mmm* ../storage/run_files/$count/mmm
