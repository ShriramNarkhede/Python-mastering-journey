

facto(){
      n=$1
      fact=1

      for((i=1;i<=n;i++))
      do
            fact=$((fact * i))
      done

      echo$"factoral is"$fact
}


echo$"Enter a number :"
read a

if [ $a -lt 0 ]; then
      echo$"number is nigga "

else 
 echo$"factoral of number $a is ($facto $a) "

 fi
