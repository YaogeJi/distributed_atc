import os


exp_name = "ball_verification"

N = 680
d = 12800
s = 9
m = 20
p_group =   [0.5,0.5,0.5,0.5]
rho_group = [0.55, 0.65, 0.75, 0.85]
solver_mode = "distributed"
iter_type = "projected"
gamma = 0.08789
total = 30

for i in range(len(rho_group)):
    p = p_group[i]
    rho = rho_group[i]
    for num_exp in range(total): 
        command="-N {} -d {} -s {} -m {} -p {} -rho {} --tol 1e-19 --data_index {} --solver_mode {} --iter_type {} --gamma {} --optimal_lmda --verbose --storing_filepath ./output/{}/N{}_d{}_s{}_exp{}/ --storing_filename {}_m{}_rho{}_gamma{}.output".format(N, d, s, m, p, rho, num_exp, solver_mode, iter_type, gamma, exp_name, N, d, s, num_exp, solver_mode, m, rho, gamma)
        # print('python main.py {}'.format(command))
        os.system('python main.py {}'.format(command))

