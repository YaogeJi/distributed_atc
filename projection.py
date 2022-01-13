import numpy as np


def euclidean_proj_l1ball(v,b=1):
    if b < 0:
        return
    else:
        if np.linalg.norm(v,1) <= b:
            return v
        u = np.sort(np.abs(v))[::-1]
#         print(u)
        sv = np.cumsum(u)
#         print(sv)
        rho = u - (sv - b) / np.arange(1, len(u)+1) > 0
        rho = np.nonzero(rho)[0][-1]
#         print(rho)
#         print(sv[rho])
        theta = ((sv[rho]-b)*1.0/(rho+1)).clip(min=0)
    #        print(theta)
        # theta = theta.clip(min=0)
        w = np.sign(v) * ((np.abs(v) - theta).clip(min=0))
        return w
