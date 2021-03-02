import numpy as np

def dist_to_origin(ar, dim):
    origin=np.zeros(dim)
    return np.linalg.norm(ar-origin)

def dist_between_pts(v_1,v_2):
    return abs(np.linalg.norm(v_1-v_2))

def draw_normal_sample(dim,std):
    m=np.zeros(dim)
    var=std**2
    cov=var*np.identity(dim)
    return np.random.multivariate_normal(m,cov,dim)
