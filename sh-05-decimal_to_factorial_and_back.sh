#!/bin/bash
oper () {
  foo=$2
  if [ "$1" == "dec2FactString" ]; then
    base=0
    fact=0
    while [ "$fact" -le "$foo" ]; do
      maxfact=$base
      base=$((base + 1))
      fact=$(seq -s "*" 1 "$base" |bc)
    done 
    
    remain=$foo
    out=""
    for (( i=$maxfact; i>= 0; i-- )); do
      num=0
      fi=$(seq -s "*" 1 "$i" |bc)
      ll=$((num * fi))
      while [ "$ll" -le "$remain" ]; do
        nn=$num
        num=$(( num + 1 ))
        ll=$(( num * fi ))
        exit
      done
      remain=$((remain - nn * $(seq -s "*" 1 "$i" |bc)))
      out+="$nn"
      
    done
    
    echo $out
    
    
  else
    declare -A arrNums
    arrNums=([0]=0 [1]=1 [2]=2 [3]=3 [4]=4 [5]=5 [6]=6 [7]=7 [8]=8 [9]=9 [A]=10 [B]=11 [C]=12 [D]=13 [E]=14 [F]=15 [G]=16 [H]=17 [I]=18 [J]=19 [K]=20 [L]=21 [M]=22 [N]=23 [O]=24 [P]=25 [Q]=26 [R]=27 [S]=28 [T]=29 [U]=30 [V]=31 [W]=32 [X]=33 [Y]=34 [Z]=35)
    decimal=0
    for (( i=$((${#foo}-1)); i>=0; i-- )); do
        inum=${foo:$i:1}
        num=${arrNums["$inum"]}
        base=$((${#foo}-1 - $i))
        fact=$(seq -s "*" 1 "$base" |bc)
        bfact=$((num * fact))
        #echo "$num | $base | $fact | $bfact"
        decimal=$((decimal + bfact))
        # - pokryt A - Z prevodem na 10 az...
    done
    echo $decimal
  fi
}
oper "$1" "$2"