count=`ls -l /u/user/bingjun5249/SE_UserHome/WWZ/DNN/storate/run|grep ^d|wc -l`
count=`expr $count + 1`
echo $count


mkdir /u/user/bingjun5249/SE_UserHome/WWZ/DNN/storate/run/trial$count/

mv total* /u/user/bingjun5249/SE_UserHome/WWZ/DNN/storate/run/trial$count/
