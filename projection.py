import numpy as np
import pytest


def euclidean_proj_l1ball(v,b=1):
    if len(v.shape) != 1:
        raise ValueError("vector should be (N,) dimension")
    if b <= 0:
        raise ValueError("radius of projection should greater than 0")
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

def test_proj():
    # fucntion random test
    for i in range(100):
        dimension = np.random.randint(1, 10000)
        v = np.random.rand(dimension)
        l1_norm = np.linalg.norm(v, ord=1)
        b = l1_norm * 2
        assert np.linalg.norm(euclidean_proj_l1ball(v, b), ord=1) == l1_norm
        b = l1_norm / 2
        print(np.linalg.norm(euclidean_proj_l1ball(v, b), ord=1), b)
        assert np.abs(np.linalg.norm(euclidean_proj_l1ball(v, b), ord=1) - b) <= 1e-8
        with pytest.raises(ValueError, match="radius of projection should greater than 0"):
            np.linalg.norm(euclidean_proj_l1ball(v, -1), ord=1)
    v = np.random.random((10,10))
    l1_norm = np.linalg.norm(v, ord=1)
    with pytest.raises(ValueError, match="vector should be *"):
            np.linalg.norm(euclidean_proj_l1ball(v, l1_norm/2), ord=1)
    # for i in range(100):
    #     v = np.random.random((10,10))
    #     l1_norm = np.linalg.norm(v, ord=1)
    #     b = l1_norm * 2
    #     assert (np.linalg.norm(euclidean_proj_l1ball(v, b), ord=1) - l1_norm) <= 1e-5
    #     b = l1_norm / 2
    #     assert np.abs(np.linalg.norm(euclidean_proj_l1ball(v, b), ord=1) - b) <= 1e-5
    

if __name__ == "__main__":
    print("testing")
    test_proj()
    print("test passed")