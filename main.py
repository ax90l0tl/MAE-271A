import numpy as np
import matplotlib.pyplot as plt

w = 0.2 # rad/s
sample_rate = 200 # Hz
V = 0.0004 # (m/s^2)^2

def normal(x, mean, variance):
    f = (1/(variance*np.sqrt(2*np.pi)))*np.exp(-np.pow((x-mean), 2)/(2*np.pow(variance, 2)))
    return(f)
    
b_a = normal(0, 0, 0.01)

def a(t): # m/s^2
    return(10*np.sin(w*t))

def v(t, a): # m/s
    v_0 = normal(0, 100, 1)
    v = v_0 + (a/w)-(a/w)*np.cos(w*t)
    return(v)

def p(t, a):
    p_0 = normal(0, 10)
    v_0 = normal(0, 100, 1)
    p = p_0 + (v_0 + (a/w))*t - (a/w**2)*np.sin(w*t)
    return(p)

