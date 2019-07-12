#!/bin/sh
#此为原始脚本,不知为何不能工作
catalog=sc-catalog-tel.txt
out=sc-sks.txt

num=`wc -l $catalog| awk '{print $1}'`

for ((i=1;i<=$num;i++))
do

year=`cat $catalog| awk '{print $1}'| cut -c1-4| awk "NR==$i"`
mo=`cat $catalog| awk '{print $1}'| cut -c6-7| awk "NR==$i"`
dy=`cat $catalog| awk '{print $1}'| cut -c9-10| awk "NR==$i"`

hr=`cat $catalog| awk '{print $2}'| cut -c1-2| awk "NR==$i"`
mn=`cat $catalog| awk '{print $2}'| cut -c4-5| awk "NR==$i"`
sec=`cat $catalog| awk '{print $2}'| cut -c7-8| awk "NR==$i"`

lat=`cat $catalog| awk '{print $3}'| awk "NR==$i"`
lon=`cat $catalog| awk '{print $4}'| awk "NR==$i"`

dep=`cat $catalog| awk '{print $5}'| awk "NR==$i"`
m=`cat $catalog| awk '{print $6}'| cut -c1-3| awk "NR==$i"`

msec=00

echo ${year},${mo},${dy},${hr}${mn}${sec}.${msec},${lat},${lon},${m},${dep} >> $out

done
