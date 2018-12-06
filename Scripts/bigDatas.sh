#!/bin/bash

echo "<===="
iteration=0
until [ $iteration -gt 60 ]
do
  echo "$iteration";
  start=$((iteration*1000+1))
  end=$((start+999))
  sed -n "$start,$end p" all.txt > $iteration.txt
  sed ':a;N;$!ba;s/\n/],[/g' $iteration.txt > $iteration.txt.tmp && mv $iteration.txt.tmp $iteration.txt
  echo '"]]}' >> $iteration.txt
  sed '1i{datas:[["\' $iteration.txt > $iteration.txt.tmp && mv $iteration.txt.tmp $iteration.txt
  sed ':a;N;$!ba;s/\n//g' $iteration.txt > $iteration.txt.tmp && mv $iteration.txt.tmp $iteration.txt
  ((iteration++));
done
echo "====>"
