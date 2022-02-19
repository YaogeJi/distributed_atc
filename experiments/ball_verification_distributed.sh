#!/bin/bash

exp_name="ball_verification"

N_group="240"
d=400
s=5
m=20
p=0.8
rho=0.2
solver_mode="distributed"
iter_type="projected"
gamma=0.08789
total=30

for N in $N_group
do
    num_exp=0
    while [ $num_exp -ne $total ]
    do
        echo $rho $num_exp
        command="-N $N -d $d -s $s -m $m -p $p -rho $rho --tol 1e-19 --data_index $num_exp --solver_mode $solver_mode --iter_type $iter_type --gamma $gamma --optimal_lmda --verbose --storing_filepath ./output/$exp_name/N${N}_d${d}_s${s}_exp${num_exp}/ --storing_filename ${solver_mode}_m${m}_rho${rho}_gamma${gamma}.output"
        python main.py $command
        # python main.py $command &
        num_exp=$(($num_exp+1))
    done
    wait
done
