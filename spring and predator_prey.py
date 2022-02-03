# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 21:22:24 2022

@author: maybe_surf
"""

import pylab as plt

def dx_dt2(x_pr, x):
    #returns the value of second derivative for the over damped system
    return -3*x_pr-2*x

def dx_dt2_2 (x_pr, x):
    #returns the value of the  second derivative for the under-damped system
    return -2*x_pr-50*x

def Euler(x, x_pr, step, limit, option):
    #takes the initial values of x and x prime, the step size, the range, and option
    t = [0] #stores t values
    x_vals = [x] #stores x values
    total = 0 #counts number of steps
    while total <= limit:
        if option == 1:
            x_pr2 = dx_dt2(x_pr, x)
        elif option == 2:
            x_pr2 = dx_dt2_2(x_pr, x)
        x += x_pr*step
        x_pr += x_pr2*step
        x_vals.append(x)
        total += step
        t.append(total)
    
    plt.figure()
    #creates separate plots for over damped and under damped systems
    plt.plot(t, x_vals)
    if option == 1:
        plt.title("over-damped")
    elif option == 2:
        plt.title("under-damped")
    plt.xlabel("time")
    plt.ylabel("displacement")
    
def Euler_system(H, L, step, limit):
    #takes the initial values for H and L, as well as step size and range
    t = [0]
    H_vals = [H]
    L_vals = [L]
    # the three vectors above store the time as well as the population sizes
    total = 0
    while total <= limit:
        H_pr = 0.4*H-0.01*H*L
        L_pr = -0.3*L+0.005*H*L
        H += H_pr*step
        L += L_pr*step
        total += step
        t.append(total)
        H_vals.append(H)
        L_vals.append(L)
    plt.figure()
    plt.plot(t, H_vals)
    plt.plot(t, L_vals)
    plt.title("2 by 2 system")
    plt.legend("hare", "lynx")
    plt.xlabel("time")
    plt.ylabel("population")
    

x = 0
x_pr = 1
step = 0.001
limit = 17
Euler(x, x_pr, step, limit, 1) #plots the solution for over-damped system
option = 2
Euler (x, x_pr, step, limit, 2) #plots the solution for the over-damped system

H = 70
L = 50
limit = 100
Euler_system(H, L, step, limit) #plots the solution for the predator-prey system


















