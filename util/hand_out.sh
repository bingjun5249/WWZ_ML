count=`ls -l /u/user/bingjun5249/SE_UserHome/WWZ/DNN/storate/util|grep ^d|wc -l`
count=`expr $count + 1`

echo $count

mkdir /u/user/bingjun5249/SE_UserHome/WWZ/DNN/storate/util/trial$count/


mv *.png /u/user/bingjun5249/SE_UserHome/WWZ/DNN/storate/util/trial$count/
