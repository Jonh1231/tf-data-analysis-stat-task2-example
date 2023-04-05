import pandas as pd 
import numpy as np 
import math 
 
import scipy.stats 
 
 
chat_id = 5493901342 
 
def solution(p: float, x: np.array) -> tuple: 
    time14 = 14 
    alpha = 1 - p 
    ans = min(x) 
    left = ans - math.log(alpha)/len(x) 
    right = ans - math.log(1-alpha)/len(x) 
    left -= 1/2 
    right -= 1/2 
    left /= (time14*time14) 
    right /= (time14*time14) 
 
    return left, \ 
           right 
