#!/bin/bash

exp_name="connectivity_accuracy_dilemma"

N=25600
d=400
s=5
solver_mode="centralized"
iter_type="projected"
gamma_group="0.08789"
total=30

for gamma in $gamma_group
do
    echo $gamma
    num_exp=0
    while [ $num_exp -ne $total ]
    do
        command="-N $N -d $d -s $s --data_index $num_exp --solver_mode $solver_mode --iter_type $iter_type --gamma $gamma --optimal_lmda --verbose --storing_filepath ./output/$exp_name/N${N}_d${d}_s${s}_exp${num_exp}/ --storing_filename ${solver_mode}_gamma${gamma}.output"
        python main.py $command
        # python main.py $command &
        num_exp=$(($num_exp+1))
    done
    wait
done
