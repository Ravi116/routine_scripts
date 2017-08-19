if [ "$#" -lt "1" ];
then
        echo "Opening single terminal"
        gnome-terminal
else
        strin="--tab "
        if [ "$1" -gt "10" ];
        then
                echo "DO YOU REALLY NEED THAT MANY TABS????"
                exit
        fi

	for j in $(seq 1 $1)
	do  
		option+=$strin
	done
	echo $option
	eval gnome-terminal "$option"
fi


