#!/bin/bash
perimeter() {
  Num=$1
  Sum=0
  f1=1
  f2=1
  
  for (( i=0;i<=Num;i++ ))
  do
       Sum=$((Sum+f1))
       fn=$((f1+f2))
       f1=$f2
       f2=$fn
  done
  
  echo $((4*Sum))
}
perimeter $1