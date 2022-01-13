#!/bin/bash

exp_name="connectivity_accuracy_dilemma_d400"

N=270
d=400
s=5
m=20
p=0.4
rho=0.62
solver_mode="distributed"
iter_type="projected"
gamma_group="0.08789"
total=30

for gamma in $gamma_group
do
    echo $gamma
    num_exp=0
    while [ $num_exp -ne $total ]
    do
        if [ "$num_exp" == "0" ]
        then
            command="-N $N -d $d -s $s -m $m -p $p -rho $rho --tol 1e-19 --data_index $num_exp --solver_mode $solver_mode --iter_type $iter_type --gamma $gamma --optimal_lmda --verbose --storing_filepath ./output/$exp_name/N${N}_rho${rho}_exp${num_exp}/ --storing_filename ${solver_mode}_gamma${gamma}.output"
        else
            command="-N $N -d $d -s $s -m $m -p $p -rho $rho --tol 1e-19 --data_index $num_exp --solver_mode $solver_mode --iter_type $iter_type --gamma $gamma --optimal_lmda --storing_filepath ./output/$exp_name/N${N}_rho${rho}_exp${num_exp}/ --storing_filename ${solver_mode}_gamma${gamma}.output"
        fi
        python main.py $command
        # python main.py $command &
        num_exp=$(($num_exp+1))
    done
    wait
done
