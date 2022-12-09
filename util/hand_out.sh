count=`ls -l ../storage/util_files/zgamma/|grep ^d|wc -l`
count=`expr $count - 1`

mkdir ../storage/util_files/zgamma/$count
mkdir ../storage/util_files/zgamma/$count/eee
mkdir ../storage/util_files/zgamma/$count/eem
mkdir ../storage/util_files/zgamma/$count/emm
mkdir ../storage/util_files/zgamma/$count/mmm

mv eee* ../storage/util_files/zgamma/$count/eee
mv eem* ../storage/util_files/zgamma/$count/eem
mv emm* ../storage/util_files/zgamma/$count/emm
mv mmm* ../storage/util_files/zgamma/$count/mmm
