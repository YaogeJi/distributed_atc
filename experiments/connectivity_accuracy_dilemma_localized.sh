#!/bin/bash

exp_name="connectivity_accuracy_dilemma"

N=320
d=800
s=6
m=20
solver_mode="localized"
iter_type="projected"
gamma_group="0.08789"
total=30

for gamma in $gamma_group
do
    echo $gamma
    num_exp=0
    while [ $num_exp -ne $total ]
    do
        command="-N $N -d $d -s $s -m $m --tol 1e-19 --data_index $num_exp --solver_mode $solver_mode --iter_type $iter_type --gamma $gamma --optimal_lmda --verbose --storing_filepath ./output/$exp_name/N${N}_d${d}_s${s}_exp${num_exp}/ --storing_filename ${solver_mode}_m${m}_gamma${gamma}.output"
        python main.py $command
        # python main.py $command &
        num_exp=$(($num_exp+1))
    done
    wait
done
