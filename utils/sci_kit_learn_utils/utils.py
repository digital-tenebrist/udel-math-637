import numpy as np
from math import sqrt

from numpy import linalg as LA
from sklearn.metrics.pairwise import euclidean_distances as ED

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

def calc_dist_cor_score(x,y):
    d_x = ED(x,x)
    d_y = ED(y,y)

    n_x = LA.norm(d_x, ord='fro')
    n_y = LA.norm(d_y, ord='fro')
    n_diff = LA.norm(d_y-d_x, ord='fro')

    # print(f'Norm(x) {n_x}')
    # print(f'Norm(y) {n_y}')
    # print(f'Norm(d) {n_diff}')
    # print(f'sqrt(x*y) {sqrt(n_x * n_y)}')

    # find the norm of d_y
    # then divide by product of norm_dx and norm_dy

    return n_diff / sqrt(n_x * n_y)
    #return n_diff / n_x
