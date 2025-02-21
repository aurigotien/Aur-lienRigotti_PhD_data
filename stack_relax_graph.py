import stack_relax_files as rf
import stack_graph as g
import matplotlib.pyplot as plt
import scipy.optimize as sc
import numpy as np
import operator as op

# Function data treamtement
def plot_extr(val,len_val):
    # Function variable
    # Scalar
    # index
    sxy_i = 0
    press_i = 4
    z_i = 6
    cin_i = 8

    # Simulation variable
    dt = 1E-4 # discretisation time
    step = 7500

    # Vector
    time = np.zeros(len_val)

    for i in range(len_val): time[i] = (dt*step*i)

    press = val[:,press_i]
    S_xy = val[:,sxy_i]
    Z = val[:,z_i]
    vel = (val[:,cin_i])
    return time,press,S_xy,Z,vel

def val_var_1def(val1,val2,val3,val4,val5,val6,val7,val8,val9,val10,E,t,d,stack):
    # Function variable
    # Scalar
    # dimension variable
    len_val = len(val1)

    # Matrix
    time = np.zeros((len_val,stack))
    S_xy = np.zeros((len_val,stack))
    press = np.zeros((len_val,stack))
    Z = np.zeros((len_val,stack))
    vel = np.zeros((len_val,stack))

    # data extr
    if stack >= 1 :
        time[:,0],press[:,0],S_xy[:,0],Z[:,0],vel[:,0] = plot_extr(val1,len_val)
    if stack >= 2 :
        time[:,1],press[:,1],S_xy[:,1],Z[:,1],vel[:,1] = plot_extr(val2,len_val)
    if stack >= 3 :
        time[:,2],press[:,2],S_xy[:,2],Z[:,2],vel[:,2] = plot_extr(val3,len_val)
    if stack >= 4 :
        time[:,3],press[:,3],S_xy[:,3],Z[:,3],vel[:,3] = plot_extr(val4,len_val)
    if stack >= 5 :
        time[:,4],press[:,4],S_xy[:,4],Z[:,4],vel[:,4] = plot_extr(val5,len_val)
    if stack >= 6 :
        time[:,5],press[:,5],S_xy[:,5],Z[:,5],vel[:,5] = plot_extr(val6,len_val)
    if stack >= 7 :
        time[:,6],press[:,6],S_xy[:,6],Z[:,6],vel[:,6] = plot_extr(val7,len_val)
    if stack >= 8 :
        time[:,7],press[:,7],S_xy[:,7],Z[:,7],vel[:,7] = plot_extr(val8,len_val)
    if stack >= 9 :
        time[:,8],press[:,8],S_xy[:,8],Z[:,8],vel[:,8] = plot_extr(val9,len_val)
    if stack >= 10 :
        time[:,9],press[:,9],S_xy[:,9],Z[:,9],vel[:,9] = plot_extr(val10,len_val)
    return time/t,press/E,S_xy/E,Z,(vel*d/t)

def val_var_cumul(val1,val2,val3,val4,val5,val6,val7,val8,val9,val10,val11,val12,val13,val14,val15,val16,val17,val18,val19,E,t,d,no_relax):
    # Function variable
    # Scalar
    # dimension variable
    len_val = len(val1)

    # Matrix
    time = np.zeros((len_val,no_relax))
    S_xy = np.zeros((len_val,no_relax))
    press = np.zeros((len_val,no_relax))
    Z = np.zeros((len_val,no_relax))
    vel = np.zeros((len_val,no_relax))

    # data extr
    time[:,0],press[:,0],S_xy[:,0],Z[:,0],vel[:,0] = plot_extr(val1,len_val)
    time[:,1],press[:,1],S_xy[:,1],Z[:,1],vel[:,1] = plot_extr(val2,len_val)
    time[:,2],press[:,2],S_xy[:,2],Z[:,2],vel[:,2] = plot_extr(val3,len_val)
    time[:,3],press[:,3],S_xy[:,3],Z[:,3],vel[:,3] = plot_extr(val4,len_val)
    time[:,4],press[:,4],S_xy[:,4],Z[:,4],vel[:,4] = plot_extr(val5,len_val)
    time[:,5],press[:,5],S_xy[:,5],Z[:,5],vel[:,5] = plot_extr(val6,len_val)
    time[:,6],press[:,6],S_xy[:,6],Z[:,6],vel[:,6] = plot_extr(val7,len_val)
    time[:,7],press[:,7],S_xy[:,7],Z[:,7],vel[:,7] = plot_extr(val8,len_val)
    time[:,8],press[:,8],S_xy[:,8],Z[:,8],vel[:,8] = plot_extr(val9,len_val)
    time[:,9],press[:,9],S_xy[:,9],Z[:,9],vel[:,9] = plot_extr(val10,len_val)
    time[:,10],press[:,10],S_xy[:,10],Z[:,10],vel[:,10] = plot_extr(val11,len_val)
    time[:,11],press[:,11],S_xy[:,11],Z[:,11],vel[:,11] = plot_extr(val12,len_val)
    time[:,12],press[:,12],S_xy[:,12],Z[:,12],vel[:,12] = plot_extr(val13,len_val)
    time[:,13],press[:,13],S_xy[:,13],Z[:,13],vel[:,13] = plot_extr(val14,len_val)
    time[:,14],press[:,14],S_xy[:,14],Z[:,14],vel[:,14] = plot_extr(val15,len_val)
    time[:,15],press[:,15],S_xy[:,15],Z[:,15],vel[:,15] = plot_extr(val16,len_val)
    time[:,16],press[:,16],S_xy[:,16],Z[:,16],vel[:,16] = plot_extr(val17,len_val)
    time[:,17],press[:,17],S_xy[:,17],Z[:,17],vel[:,17] = plot_extr(val18,len_val)
    time[:,18],press[:,18],S_xy[:,18],Z[:,18],vel[:,18] = plot_extr(val19,len_val)
    return time/t,press/E,S_xy/E,Z,(vel*t)/d

def val_mod(stack,ela_relax_1,ela_relax_2,ela_relax_3,ela_relax_4,ela_relax_5,ela_relax_6,ela_relax_7,ela_relax_8,ela_relax_9,ela_relax_10,max_stack,call):
    # Variables
    # Scalar
    # index
    t_sh_i = 0
    t_p_i = 1
    sh_i = 2
    p_i = 3
    b_sh_i = 4
    b_p_i = 5

    # dimmension variable
    len_vec = len(ela_relax_1)

    # Matrix
    t_sh = np.zeros((len_vec,max_stack))
    t_p = np.zeros((len_vec,max_stack))
    T_sh = np.zeros((len_vec,max_stack))
    T_p = np.zeros((len_vec,max_stack))
    sh_c = np.zeros((len_vec,max_stack))
    p_c = np.zeros((len_vec,max_stack))
    b_sh = np.zeros((len_vec,max_stack))
    b_p = np.zeros((len_vec,max_stack))

    for i in range(len_vec):
        for j in range(stack):
            if j == 0 :
                t_sh[i,j] = ela_relax_1[i,t_sh_i]
                t_p[i,j] = ela_relax_1[i,t_p_i]
                sh_c[i,j] = ela_relax_1[i,sh_i]
                p_c[i,j] = ela_relax_1[i,p_i]
                b_sh[i,j] = ela_relax_1[i,b_sh_i]
                b_p[i,j] = ela_relax_1[i,b_p_i]
            if j == 1 :
                t_sh[i,j] = ela_relax_2[i,t_sh_i]
                t_p[i,j] = ela_relax_2[i,t_p_i]
                sh_c[i,j] = ela_relax_2[i,sh_i]
                p_c[i,j] = ela_relax_2[i,p_i]
                b_sh[i,j] = ela_relax_2[i,b_sh_i]
                b_p[i,j] = ela_relax_2[i,b_p_i]
            if j == 2 :
                t_sh[i,j] = ela_relax_3[i,t_sh_i]
                t_p[i,j] = ela_relax_3[i,t_p_i]
                sh_c[i,j] = ela_relax_3[i,sh_i]
                p_c[i,j] = ela_relax_3[i,p_i]
                b_sh[i,j] = ela_relax_3[i,b_sh_i]
                b_p[i,j] = ela_relax_3[i,b_p_i]
            if j == 3 :
                t_sh[i,j] = ela_relax_4[i,t_sh_i]
                t_p[i,j] = ela_relax_4[i,t_p_i]
                sh_c[i,j] = ela_relax_4[i,sh_i]
                p_c[i,j] = ela_relax_4[i,p_i]
                b_sh[i,j] = ela_relax_4[i,b_sh_i]
                b_p[i,j] = ela_relax_4[i,b_p_i]
            if j == 4 :
                t_sh[i,j] = ela_relax_5[i,t_sh_i]
                t_p[i,j] = ela_relax_5[i,t_p_i]
                sh_c[i,j] = ela_relax_5[i,sh_i]
                p_c[i,j] = ela_relax_5[i,p_i]
                b_sh[i,j] = ela_relax_5[i,b_sh_i]
                b_p[i,j] = ela_relax_5[i,b_p_i]
            if j == 5 :
                t_sh[i,j] = ela_relax_6[i,t_sh_i]
                t_p[i,j] = ela_relax_6[i,t_p_i]
                sh_c[i,j] = ela_relax_6[i,sh_i]
                p_c[i,j] = ela_relax_6[i,p_i]
                b_sh[i,j] = ela_relax_6[i,b_sh_i]
                b_p[i,j] = ela_relax_6[i,b_p_i]
            if j == 6 :
                t_sh[i,j] = ela_relax_7[i,t_sh_i]
                t_p[i,j] = ela_relax_7[i,t_p_i]
                sh_c[i,j] = ela_relax_7[i,sh_i]
                p_c[i,j] = ela_relax_7[i,p_i]
                b_sh[i,j] = ela_relax_7[i,b_sh_i]
                b_p[i,j] = ela_relax_7[i,b_p_i]
            if j == 7 :
                t_sh[i,j] = ela_relax_8[i,t_sh_i]
                t_p[i,j] = ela_relax_8[i,t_p_i]
                sh_c[i,j] = ela_relax_8[i,sh_i]
                p_c[i,j] = ela_relax_8[i,p_i]
                b_sh[i,j] = ela_relax_8[i,b_sh_i]
                b_p[i,j] = ela_relax_8[i,b_p_i]
            if j == 8 :
                t_sh[i,j] = ela_relax_9[i,t_sh_i]
                t_p[i,j] = ela_relax_9[i,t_p_i]
                sh_c[i,j] = ela_relax_9[i,sh_i]
                p_c[i,j] = ela_relax_9[i,p_i]
                b_sh[i,j] = ela_relax_9[i,b_sh_i]
                b_p[i,j] = ela_relax_9[i,b_p_i]
            if j == 9 :
                t_sh[i,j] = ela_relax_10[i,t_sh_i]
                t_p[i,j] = ela_relax_10[i,t_p_i]
                sh_c[i,j] = ela_relax_10[i,sh_i]
                p_c[i,j] = ela_relax_10[i,p_i]
                b_sh[i,j] = ela_relax_10[i,b_sh_i]
                b_p[i,j] = ela_relax_10[i,b_p_i]
            # end if
            T_sh[i,j] = (t_sh[i,j]/b_sh[i,j])*rf.gamma_function(b_sh[i,j])
            T_p[i,j] = (t_p[i,j]/b_p[i,j])*rf.gamma_function(b_p[i,j])
        # end of j for loop
    # end of i for loop
    return T_sh,T_p,sh_c,p_c,b_sh,b_p

def val_error_mod(stack,error_1,error_2,error_3,error_4,error_5,error_6,error_7,error_8,error_9,error_10,max_stack,call):
    # Variables
    # Scalar
    # index
    t_sh_i = 0
    t_p_i = 1
    sh_i = 2
    p_i = 3
    b_sh_i = 4
    b_p_i = 5

    # dimmension variable
    len_vec = len(error_1)

    # Matrix
    t_sh = np.zeros((len_vec,max_stack))
    t_p = np.zeros((len_vec,max_stack))
    sh_c = np.zeros((len_vec,max_stack))
    p_c = np.zeros((len_vec,max_stack))
    b_sh = np.zeros((len_vec,max_stack))
    b_p = np.zeros((len_vec,max_stack))

    for i in range(len_vec):
        for j in range(stack):
            if j == 0 :
                t_sh[i,j] = error_1[i,t_sh_i]
                t_p[i,j] = error_1[i,t_p_i]
                sh_c[i,j] = error_1[i,sh_i]
                p_c[i,j] = error_1[i,p_i]
                b_sh[i,j] = error_1[i,b_sh_i]
                b_p[i,j] = error_1[i,b_p_i]
            if j == 1 :
                t_sh[i,j] = error_2[i,t_sh_i]
                t_p[i,j] = error_2[i,t_p_i]
                sh_c[i,j] = error_2[i,sh_i]
                p_c[i,j] = error_2[i,p_i]
                b_sh[i,j] = error_2[i,b_sh_i]
                b_p[i,j] = error_2[i,b_p_i]
            if j == 2 :
                t_sh[i,j] = error_3[i,t_sh_i]
                t_p[i,j] = error_3[i,t_p_i]
                sh_c[i,j] = error_3[i,sh_i]
                p_c[i,j] = error_3[i,p_i]
                b_sh[i,j] = error_3[i,b_sh_i]
                b_p[i,j] = error_3[i,b_p_i]
            if j == 3 :
                t_sh[i,j] = error_4[i,t_sh_i]
                t_p[i,j] = error_4[i,t_p_i]
                sh_c[i,j] = error_4[i,sh_i]
                p_c[i,j] = error_4[i,p_i]
                b_sh[i,j] = error_4[i,b_sh_i]
                b_p[i,j] = error_4[i,b_p_i]
            if j == 4 :
                t_sh[i,j] = error_5[i,t_sh_i]
                t_p[i,j] = error_5[i,t_p_i]
                sh_c[i,j] = error_5[i,sh_i]
                p_c[i,j] = error_5[i,p_i]
                b_sh[i,j] = error_5[i,b_sh_i]
                b_p[i,j] = error_5[i,b_p_i]
            if j == 5 :
                t_sh[i,j] = error_6[i,t_sh_i]
                t_p[i,j] = error_6[i,t_p_i]
                sh_c[i,j] = error_6[i,sh_i]
                p_c[i,j] = error_6[i,p_i]
                b_sh[i,j] = error_6[i,b_sh_i]
                b_p[i,j] = error_6[i,b_p_i]
            if j == 6 :
                t_sh[i,j] = error_7[i,t_sh_i]
                t_p[i,j] = error_7[i,t_p_i]
                sh_c[i,j] = error_7[i,sh_i]
                p_c[i,j] = error_7[i,p_i]
                b_sh[i,j] = error_7[i,b_sh_i]
                b_p[i,j] = error_7[i,b_p_i]
            if j == 7 :
                t_sh[i,j] = error_8[i,t_sh_i]
                t_p[i,j] = error_8[i,t_p_i]
                sh_c[i,j] = error_8[i,sh_i]
                p_c[i,j] = error_8[i,p_i]
                b_sh[i,j] = error_8[i,b_sh_i]
                b_p[i,j] = error_8[i,b_p_i]
            if j == 8 :
                t_sh[i,j] = error_9[i,t_sh_i]
                t_p[i,j] = error_9[i,t_p_i]
                sh_c[i,j] = error_9[i,sh_i]
                p_c[i,j] = error_9[i,p_i]
                b_sh[i,j] = error_9[i,b_sh_i]
                b_p[i,j] = error_9[i,b_p_i]
            if j == 9 :
                t_sh[i,j] = error_10[i,t_sh_i]
                t_p[i,j] = error_10[i,t_p_i]
                sh_c[i,j] = error_10[i,sh_i]
                p_c[i,j] = error_10[i,p_i]
                b_sh[i,j] = error_10[i,b_sh_i]
                b_p[i,j] = error_10[i,b_p_i]
            # end if
        # end of j for loop
    # end of i for loop
    return t_sh,t_p,sh_c,p_c,b_sh,b_p

def val_var_sh(val1,val2,val3,val4,val5,val6,val7,val8,val9,val10,stack,anal,adim_var,val_var):
    # Variables
    # Scalar
    # index
    if val_var != 'std':
        sxy_i = 0
        phi_i = 2
        z_i = 4
        vol_i = 6
        cis_i = 8
        p_i = 10
        sy_i = 12
        sx_i = 14
        eq_i = 16
    else :
        sxy_i = 1
        phi_i = 3
        z_i = 5
        vol_i = 7
        cis_i = 9
        p_i = 11
        sy_i = 13
        sx_i = 15
        eq_i = 17
    # end if

    if anal == 'strain': var = 5E8
    elif anal == 'pressure':
        if adim_var == 'P_5000': var = 5E3
        elif adim_var == 'P_50000': var = 5E4
        elif adim_var == 'P_90000': var = 9E4
    # end if

    # dimmension variable
    no_val = 5 # max number of stacks
    len_val = len(val1)

    # Matrix
    press = np.zeros((len_val,no_val))
    S_xx = np.zeros((len_val,no_val))
    S_yy = np.zeros((len_val,no_val))
    S_xy = np.zeros((len_val,no_val))
    cis = np.zeros((len_val,no_val))
    e_vol = np.zeros((len_val,no_val))
    phi = np.zeros((len_val,no_val))
    Z = np.zeros((len_val,no_val))
    e_q = np.zeros((len_val,no_val))

    # Value attribution
    if stack >= 1:
        press[:,0] = abs(val1[:,p_i])
        S_xx[:,0] = val1[:,sx_i]
        S_yy[:,0] = val1[:,sy_i]
        S_xy[:,0] = val1[:,sxy_i]
        cis[:,0] = val1[:,cis_i]
        e_vol[:,0] = ((val1[0,vol_i] - val1[:,vol_i]) / val1[0,vol_i])
        phi[:,0] = val1[:,phi_i]
        Z[:,0] = val1[:,z_i]
        e_q[:,0] = val1[:,eq_i]
    if stack >= 2:
        press[:,1] = abs(val2[:,p_i])
        S_xx[:,1] = val2[:,sx_i]
        S_yy[:,1] = val2[:,sy_i]
        S_xy[:,1] = val2[:,sxy_i]
        cis[:,1] = val2[:,cis_i]
        e_vol[:,1] = ((val2[0,vol_i] - val2[:,vol_i]) / val2[0,vol_i])
        phi[:,1] = val2[:,phi_i]
        Z[:,1] = val2[:,z_i]
        e_q[:,1] = val2[:,eq_i]
    if stack >= 3:
        press[:,2] = abs(val3[:,p_i])
        S_xx[:,2] = val3[:,sx_i]
        S_yy[:,2] = val3[:,sy_i]
        S_xy[:,2] = val3[:,sxy_i]
        cis[:,2] = val3[:,cis_i]
        e_vol[:,2] = ((val3[0,vol_i] - val3[:,vol_i]) / val3[0,vol_i])
        phi[:,2] = val3[:,phi_i]
        Z[:,2] = val3[:,z_i]
        e_q[:,2] = val3[:,eq_i]
    if stack >= 4:
        press[:,3] = abs(val4[:,p_i])
        S_xx[:,3] = val4[:,sx_i]
        S_yy[:,3] = val4[:,sy_i]
        S_xy[:,3] = val4[:,sxy_i]
        cis[:,3] = val1[:,cis_i]
        e_vol[:,3] = ((val4[0,vol_i] - val4[:,vol_i]) / val4[0,vol_i])
        phi[:,3] = val4[:,phi_i]
        Z[:,3] = val4[:,z_i]
        e_q[:,3] = val4[:,eq_i]
    if stack >= 5:
        press[:,4] = abs(val5[:,p_i])
        S_xx[:,4] = val5[:,sx_i]
        S_yy[:,4] = val5[:,sy_i]
        S_xy[:,4] = val5[:,sxy_i]
        cis[:,4] = val5[:,cis_i]
        e_vol[:,4] = ((val5[0,vol_i] - val5[:,vol_i]) / val5[0,vol_i])
        phi[:,4] = val5[:,phi_i]
        Z[:,4] = val5[:,z_i]
        e_q[:,4] = val5[:,eq_i]
    if stack >= 6:
        press[:,5] = abs(val6[:,p_i])
        S_xx[:,5] = val6[:,sx_i]
        S_yy[:,5] = val6[:,sy_i]
        S_xy[:,5] = val6[:,sxy_i]
        cis[:,5] = val6[:,cis_i]
        e_vol[:,5] = ((val6[0,vol_i] - val6[:,vol_i]) / val6[0,vol_i])
        phi[:,5] = val6[:,phi_i]
        Z[:,5] = val6[:,z_i]
        e_q[:,5] = val6[:,eq_i]
    if stack >= 7:
        press[:,6] = abs(val7[:,p_i])
        S_xx[:,6] = val7[:,sx_i]
        S_yy[:,6] = val7[:,sy_i]
        S_xy[:,6] = val7[:,sxy_i]
        cis[:,6] = val7[:,cis_i]
        e_vol[:,6] = ((val7[0,vol_i] - val7[:,vol_i]) / val7[0,vol_i])
        phi[:,6] = val7[:,phi_i]
        Z[:,6] = val7[:,z_i]
        e_q[:,6] = val7[:,eq_i]
    if stack >= 8:
        press[:,7] = abs(val8[:,p_i])
        S_xx[:,7] = val8[:,sx_i]
        S_yy[:,7] = val8[:,sy_i]
        S_xy[:,7] = val8[:,sxy_i]
        cis[:,7] = val8[:,cis_i]
        e_vol[:,7] = ((val8[0,vol_i] - val8[:,vol_i]) / val8[0,vol_i])
        phi[:,7] = val8[:,phi_i]
        Z[:,7] = val8[:,z_i]
        e_q[:,7] = val8[:,eq_i]
    if stack >= 9:
        press[:,8] = abs(val9[:,p_i])
        S_xx[:,8] = val9[:,sx_i]
        S_yy[:,8] = val9[:,sy_i]
        S_xy[:,8] = val9[:,sxy_i]
        cis[:,8] = val9[:,cis_i]
        e_vol[:,8] = ((val9[0,vol_i] - val9[:,vol_i]) / val9[0,vol_i])
        phi[:,8] = val9[:,phi_i]
        Z[:,8] = val9[:,z_i]
        e_q[:,8] = val9[:,eq_i]
    if stack >= 10:
        press[:,9] = abs(val10[:,p_i])
        S_xx[:,9] = val10[:,sx_i]
        S_yy[:,9] = val10[:,sy_i]
        S_xy[:,9] = val10[:,sxy_i]
        cis[:,9] = val10[:,cis_i]
        e_vol[:,9] = ((val10[0,vol_i] - val10[:,vol_i]) / val10[0,vol_i])
        phi[:,9] = val10[:,phi_i]
        Z[:,9] = val10[:,z_i]
        e_q[:,9] = val10[:,eq_i]
    # end if
    return press/var,S_xx/var,S_yy/var,S_xy/var,cis,e_vol,phi,Z,e_q

def sort_mat(xval,yval,yerr,stack): # sort yval and xval as function of xval
    # Sort xval and yval
    for k in range(stack):
        mod_valx,mod_valy,mod_err = xval[:,k],yval[:,k],yerr[:,k]
        sort = sorted(zip(mod_valx,mod_valy,mod_err), key=op.itemgetter(0))
        xval[:,k], yval[:,k], yerr[:,k] = zip(*sort)
    # end of k for loop
    return xval, yval, yerr

def regime_relax_split_lines(reg,stack,colormap,lw,a):
    for i in range(stack):
        plt.axvline(reg[0,i].mean(), color = colormap[i], ls = ':', linewidth=lw, alpha = a)
        plt.axvline(reg[1,i], color = colormap[i], ls = '--', linewidth=lw, alpha = a)
        plt.axvline(reg[2,i], color = colormap[i], ls = '-.', linewidth=lw, alpha = a)
    # end of i for loop
    return

def graph_mk_ls():
    mk_v = ['o','s','s','s','s','o','s','s','s','s']
    #mk_v = ['o','s','s','s','o','s','s','s','s','s']
    #mk_v = ['o','o','s','s','s','s','s','s','s','s']

    ls_v = ['-','-.','-','-.','-','-.','','','','']
    #ls_v = ['--','--','--','--','--','-.','-.','-.','-.','-.']
    #ls_v = ['-','-','-','-','-.','-.','-.','-.','--','--']
    #ls_v = ['-','-.','-','-.','-','-.','','','','']
    return ls_v,mk_v

def graph_color_mk_ls(color1,color2):
    """ # size effects
    col_g = ['red','darkorange','green','dodgerblue','black','black','black','black','black','black']
    line = ['-','--','-.',':','-.','-.','-.','-.','--','--']
    mk_vec = ['o','s','s','s','o','s','s','s','s','s'] #"""

    """ # basic datas with 1 x 5 stacks
    col_g = [color1(0.75),color1(0.40),color1(0.25),color1(0.15),color1(0.05),color2(0.6),color2(0.4),color2(0.2),color2(0.1),color2(0.05)]
    line = ['-','--','-.',':','-.','-.','-.','-.','--','--']
    mk_vec = ['o','s','s','s','s','o','s','s','s','s'] #"""

    """ # basic datas with 2 x 5 stacks
    col_g = [color1(0.75),color1(0.40),color1(0.25),color1(0.15),color1(0.05),color1(0.75),color1(0.40),color1(0.25),color1(0.15),color1(0.05)]
    line = ['-','-.','-.','-.','-.','-','-.','-.','-.','-.']
    mk_vec = ['o','s','s','s','s','o','s','s','s','s'] #"""

    #""" # mixed datas with 2 x 3 stacks
    col_g = [color1(0.55),color2(0.6),color1(0.45),color2(0.4),color1(0.25),color2(0.2),color1(0.15),color1(0.05),color2(0.1),color2(0.05)]
    line = ['-','-.','-','-.','-','-.','--','--','--','--']
    mk_vec = ['o','o','s','s','s','s','s','s','s','s'] #"""

    """ # mixed datas with 3 x 2 stacks
    col_g = [color1(0.8),color1(0.75),color1(0.7),color1(0.3),color1(0.25),color1(0.2),color2(0),color2(0),color2(0),color2(0)]
    line = ['-','-.','--','-','-.','--','-','-','-','-']
    mk_vec = ['o','o','o','s','s','s','>','>','>','>'] #"""

    """ # mixed datas with 2 x 4 stacks
    col_g = [color1(0.75),color1(0.40),color1(0.25),color1(0.15),color2(0.6),color2(0.4),color2(0.2),color2(0.1),color1(0),color2(0)]
    line = ['-','-','-','-','-.','-.','-.','-.','--','--']
    mk_vec = ['o','s','s','s','o','s','s','s','s','s'] #"""
    return col_g, line, mk_vec

# Function graph plot
def plot_relax_cumul(xval,yval,fit,data_load,yval_fit,colormap,x_label,y_label,g_label,no_it,cumul):
    # Function variables
    # size of the graphs
    graph_len, graph_wid, font_title, font_axes, font_legend, label_space, linew, set_a = g.graph_param('simple')
    ls, mk_vec = graph_mk_ls()
    # Scalar
    cut = len(yval)-1

    # Vector
    if cumul == '': sel_label = [g_label[0],g_label[1],g_label[2],g_label[3],g_label[4]]
    else : sel_label = g_label
    # end if

    left, bottom, width, height = [0.54, 0.54, 0.30, 0.30]
    # end if

    plt.rcParams['figure.figsize'] = (graph_len,graph_wid) # set the size of the plot
    fig, ax1 = plt.subplots()

    # Graph output
    for i in range(no_it):
        if cumul == 'yes' : #i > 0 and
            if i == 0 or i == 1 or i == 5 or i == 12 or i == 14 or i == 18 :
            #if i >= 0 :
                if data_load == 'coord': ax1.plot(xval[:,i],yval[:,i],color = colormap[i],ls='-',label=sel_label[i],linewidth=linew)
                elif data_load == 'delta': ax1.plot(xval[:,i],(yval_fit[i,:]-yval[:,i])/(yval[0,i]),color = colormap[i],ls='-',label=sel_label[i],linewidth=linew)
                elif data_load == 'stress' : ax1.plot(xval[:,i],yval[:,i],color = colormap[i],ls='-',label=sel_label[i],linewidth=linew)
                elif data_load == 'velocity' : ax1.plot(xval[:cut,i],yval[:cut,i],color = colormap[i],ls='-',label=sel_label[i],linewidth=linew)
                if fit == 'yes': ax1.plot(xval[:,i],yval_fit[i,:],color=colormap[i],ls='--',linewidth=linew)
            # end if
    # end of i for loop
    ax1.ticklabel_format(axis='y', style = 'sci', scilimits = (0,0))

    ax1.set_xlim(xmin = 0)
    ax1.set_xlabel(x_label, fontsize = font_title)
    ax1.set_ylabel(y_label, fontsize = font_title)

    if data_load == 'stress':
        ax2 = fig.add_axes([left, bottom, width, height])
        for i in range(no_it):
            #if i == 0 or i == 1 or i == 2 or i == 5 or i == 8 or i == 10 or i == 12 or i == 14 or i == 16 or i == 18 :
            if i >= 0 :
                if data_load == 'coord': ax2.plot(xval[:,i],yval[:,i],color = colormap[i],ls='-',label=sel_label[i],linewidth=linew)
                elif data_load == 'delta': ax2.plot(xval[:,i],(yval_fit[i,:]-yval[:,i])/(yval[0,i]),color = colormap[i],ls='-',label=sel_label[i],linewidth=linew)
                elif data_load == 'stress' : ax2.plot(xval[:,i],yval[:,i],color = colormap[i],ls='-',label=sel_label[i],linewidth=linew)
                elif data_load == 'velocity' : ax2.plot(xval[:cut,i],yval[:cut,i],color = colormap[i],ls='-',label=sel_label[i],linewidth=linew)
                if fit == 'yes': ax2.plot(xval[:,i],yval_fit[i,:],color=colormap[i],ls='--',linewidth=linew)
        # end of i for loop

        ax2.ticklabel_format(axis='y', style = 'sci', scilimits = (0,0))
        ax2.set_xlabel(x_label, fontsize = font_title)
        ax2.set_ylabel(y_label, fontsize = font_title)

        ax2.set_xscale('log')
    # end if

    if data_load == 'delta':
        #plt.xlim(xmin = 0,xmax = 1000)
        #plt.ylim(ymin = -0.1, ymax = 0.1)
        plt.axhline(-0.05, color = 'silver',linewidth=linew)
        plt.axhline(0.05, color = 'silver',linewidth=linew)
    # end if

    plt.rc('axes', labelsize = font_axes, titlesize = font_axes)
    plt.rc('xtick', labelsize = font_axes)
    plt.rc('ytick', labelsize = font_axes)

    plt.legend(fontsize = font_legend, frameon=False, loc = 'lower left', labelspacing = label_space)
    #plt.savefig('relax_p_vs_t.png')plot
    plt.show()
    return

def plot_relax_stacks(stack,xval,yval,y_err,rd,colorm1,colorm2,mk,x_label,y_label,g_label,graph_type,line):
    # Scalar
    # size of the graphs
    graph_len, graph_wid, font_title, font_axes, font_legend, label_space, linew, set_a = g.graph_param('simple')

    cut = 1
    yval_min = yval[cut:,:stack].min()
    yval_max = yval[cut:,:stack].max()

    # Vector
    colormap, ls_vec, marker_vec = graph_color_mk_ls(colorm1, colorm2)

    if graph_type == 'stress':
        if y_label == '$\u03c4_{c}/\u03c3_{yy}$': left, bottom, width, height = [0.58, 0.53, 0.30, 0.30]
        if y_label == '$P_{c}/\u03c3_{yy}$': left, bottom, width, height = [0.57, 0.56, 0.30, 0.30]
        #left, bottom, width, height = [0.32, 0.54, 0.30, 0.30]
    if graph_type == 'time': left, bottom, width, height = [0.61, 0.44, 0.28, 0.28]
    if graph_type == 'beta': left, bottom, width, height = [0.565, 0.25, 0.30, 0.30]
    if graph_type == 'granulence': left, bottom, width, height = [0.29, 0.25, 0.30, 0.30]
    # end if

    plt.rcParams['figure.figsize'] = (graph_len,graph_wid) # set the size of the plot
    fig, ax1 = plt.subplots()

    for i in range(stack):
        if mk == '': ax1.plot(xval[cut:,i], yval[cut:,i], color = colormap[i], ls = ls_vec[i], label = g_label[i], linewidth = linew*line)
        elif mk == 'yes': ax1.plot(xval[cut:,i], yval[cut:,i], color = colormap[i], marker = marker_vec[i], ls = ls_vec[i], label = g_label[i], linewidth = linew*line)
        ax1.fill_between(xval[cut:,i],yval[cut:,i]-y_err[cut:,i],yval[cut:,i]+y_err[cut:,i], color = colormap[i], alpha = 0.5*set_a)
    # end of i for loop

    if graph_type != 'beta': ax1.ticklabel_format(axis='y', style = 'sci', scilimits = (0,0))
    # end if

    g.regime_split_lines(xval, rd, stack, linew, set_a)

    #ax1.set_xlim(xmin = 0)
    if graph_type == 'time':
        #ax1.set_xlim(xmax = 0.32)
        ax1.set_ylim(ymin = 0.95*yval_min, ymax = 1.01*yval_max) # prep no fric
        #ax1.set_ylim(ymin = 0.95*yval_min, ymax = 1.5*yval_max) # prep fric
    if graph_type == 'beta' : ax1.axhline(1, color = 'silver',linewidth=linew), ax1.set_ylim(ymin = 0.9, ymax = 1.05*yval_max)
    if graph_type == 'stress' :
        if y_label == '$\u03c4_{c}/\u03c3_{yy}$' : ax1.set_ylim(ymin = 0, ymax = 1.05*yval_max)
        if y_label == '$P_{c}/\u03c3_{yy}$': ax1.set_ylim(ymin = 0, ymax = 1.6)
    if graph_type == 'granulence':
        ax1.set_ylim(ymin = 0.75*yval_min, ymax = 0.44) #1.01*yval_max)
        #ax1.set_ylim(ymin = 0.97*yval_min, ymax = 1.001*yval_max)
    # end if

    ax1.set_xlabel(x_label, fontsize = font_title)
    ax1.set_ylabel(y_label, fontsize = font_title)
    #ax1.set_xscale('log')

    ax2 = fig.add_axes([left, bottom, width, height])
    for i in range(stack):
        if mk == '':
            ax2.plot(xval[cut:,i], yval[cut:,i], color = colormap[i], ls = ls_vec[i], label = g_label[i], linewidth = linew*line)
        elif mk == 'yes':
            ax2.plot(xval[cut:,i], yval[cut:,i], color = colormap[i], marker = marker_vec[i], ls = ls_vec[i], label = g_label[i], linewidth = linew*line)
        # end if
        ax2.fill_between(xval[cut:,i],yval[cut:,i]-y_err[cut:,i],yval[cut:,i]+y_err[cut:,i], color = colormap[i], alpha = 0.5*set_a)
    # end of i for loop

    if graph_type != 'beta':
        ax2.ticklabel_format(axis='y', style = 'sci', scilimits = (0,0))
    # end if

    g.regime_split_lines(xval, rd, stack, linew, set_a)

    if graph_type == 'beta' :
        ax2.axhline(1, color = 'silver',linewidth=linew)
        ax2.set_ylim(ymin = 0.99*yval_min, ymax = 1.01*yval_max)
    if graph_type == 'time' :
        ax2.set_ylim(ymin = 0, ymax = 1.01*yval_max)
    if graph_type == 'stress' :
        ax2.set_ylim(ymin = 0, ymax = 1.05*yval_max)
    if graph_type == 'granulence':
        ax2.set_ylim(ymin = 0.99*yval_min, ymax = 1.01*yval_max)
    # end if
    ax2.set_xlabel(x_label, fontsize = font_title), ax2.set_ylabel(y_label, fontsize = font_title)
    ax2.set_xscale('log') #"""

    plt.rc('axes', labelsize = font_axes, titlesize = font_axes)
    plt.rc('xtick', labelsize = font_axes), plt.rc('ytick', labelsize = font_axes)
    plt.legend(fontsize = font_legend, frameon=False, labelspacing = label_space)
    #plt.savefig('relax_p_vs_t.png')
    plt.show()
    return

def scatter_rheo_prop(stack,xval,yval,mod1,mod2,colorm1,colorm2,xlabel,ylabel,g_label):
    # Scalar
    # P = 90 kPa
    #cut_s = np.array([1000,1000,1000,950,410])

    # P = 50 kPa (prep no fric / prep_fric)
    cut_s = np.array([1000,1000,1000,620,1000,1000,1000,620,1000])

    # size of the graphs
    graph_len, graph_wid, font_title, font_axes, font_legend, label_space, linew, set_a = g.graph_param('simple')

    # Vector
    colormap, ls_vec, marker_vec = graph_color_mk_ls(colorm1, colorm2)

    x_min, x_max = xval.min(), xval.max()
    y_min, y_max = yval.min(), yval.max()

    # Plot the values
    plt.rcParams['figure.figsize'] = (graph_len,graph_wid) # set the size of the plot
    fig, ax1 = plt.subplots()

    for i in range(stack):
        ax1.scatter(xval[:cut_s[i],i], yval[:cut_s[i],i], color = colormap[i], ls = ls_vec[i], label = g_label[i], linewidth = linew)
        ax1.plot(xval[:cut_s[i],i], ((1/0.7)*xval[:cut_s[i],i])+7.25E-5, color = 'black', ls = '-.', linewidth = linew)
        #ax1.scatter(mod1[:,i], mod2[:,i], color = 'black', linewidth = linew)
    # end of i for loop

    ax1.ticklabel_format(axis='x', style = 'sci', scilimits = (0,0)), ax1.ticklabel_format(axis='y', style = 'sci', scilimits = (0,0))
    ax1.set_xlim(xmin = 0.999*x_min, xmax = 1.01*x_max), ax1.set_ylim(ymin = 0.999*y_min, ymax = 1.01*y_max)
    ax1.set_xlabel(xlabel, fontsize = font_title), ax1.set_ylabel(ylabel, fontsize = font_title)

    plt.rc('axes', labelsize = font_axes, titlesize = font_axes)
    plt.rc('xtick', labelsize = font_axes), plt.rc('ytick', labelsize = font_axes)
    plt.legend(fontsize = font_legend, frameon=False, loc = 'upper right', labelspacing = label_space)
    #plt.savefig('relax_p_vs_t.png')
    plt.show()
    # return
    return

def plot_rheo_prop(stack,xval,xmod,yval,yerr,mod,dmod,colorm1,colorm2,xlabel,ylabel,g_label):
    # Scalar
    # P = 90 kPa
    #cut_s = np.array([1000,1000,1000,950,410])

    # P = 50 kPa (prep no fric / prep_fric)
    cut_s = np.array([1000,1000,1000,620,1000,1000,1000,620,1000])

    # size of the graphs
    graph_len, graph_wid, font_title, font_axes, font_legend, label_space, linew, set_a = g.graph_param('simple')

    # Vector
    colormap, ls_vec, marker_vec = graph_color_mk_ls(colorm1, colorm2)

    y_min, y_max = yval.min(), yval.max()

    # Plot the values
    plt.rcParams['figure.figsize'] = (graph_len,graph_wid) # set the size of the plot
    fig, ax1 = plt.subplots()

    for i in range(stack):
        ax1.scatter(xval[:cut_s[i],i], yval[:cut_s[i],i], color = colormap[i], ls = ls_vec[i], marker = marker_vec[i], label = g_label[i], linewidth = linew)
        ax1.fill_between(xval[:cut_s[i],i],yval[:cut_s[i],i]-yerr[:cut_s[i],i],yval[:cut_s[i],i]+yerr[:cut_s[i],i], color = 'black', alpha = 0.5*set_a)

        ax1.scatter(xmod[:,i],mod[:,i], color = 'black', ls = ls_vec[i], marker = marker_vec[i], label = g_label[i], linewidth = linew)
        ax1.fill_between(xmod[:,i],mod[:,i]-dmod[:,i],mod[:,i]+dmod[:,i], color = 'black', alpha = 0.5*set_a)
    # end of i for loop

    ax1.ticklabel_format(axis='y', style = 'sci', scilimits = (0,0)), ax1.set_ylim(ymin = 0.99*y_min, ymax = 1.1*y_max)
    ax1.set_xlabel(xlabel, fontsize = font_title), ax1.set_ylabel(ylabel, fontsize = font_title)

    plt.rc('axes', labelsize = font_axes, titlesize = font_axes)
    plt.rc('xtick', labelsize = font_axes), plt.rc('ytick', labelsize = font_axes)
    plt.legend(fontsize = font_legend, frameon=False, loc = 'upper right', labelspacing = label_space)
    #plt.savefig('relax_p_vs_t.png')
    plt.show()
    # return
    return

def scatter_relax_stacks(stack,xval,yval,y_err,rd,colorm1,colorm2,x_label,y_label,g_label,graph_type):
    # size of the graphs
    graph_len, graph_wid, font_title, font_axes, font_legend, label_space, elinew, set_a = g.graph_param('simple')
    colormap, ls_vec, marker_vec = graph_color_mk_ls(colorm1, colorm2)

    # Scalar
    # dimension variable
    len_vec = len(xval)

    cut = 1

    yval_min = yval[cut:,:stack].min()
    yval_max = yval[cut:,:].max()

    # sort xval and yval as function of xval
    xval, yval, y_err = sort_mat(xval,yval,y_err,stack)

    # Plot datas
    plt.figure(figsize= (graph_len,graph_wid)) # set the size of the plot

    for i in range(len_vec):
        for j in range(stack):
            if i >= cut :
                plt.scatter(xval[i,j], yval[i,j], color = colormap[j], marker = marker_vec[j], ls = ls_vec[j], label = g_label[j], linewidth = elinew)
                plt.fill_between(xval[cut:,j],yval[cut:,j]-y_err[cut:,j],yval[cut:,j]+y_err[cut:,j], color = colormap[j], alpha = 0.04*set_a)
            # end if
        # end of j for loop
    # end of i for loop

    plt.ticklabel_format(axis='y', style = 'sci', scilimits = (0,0))
    plt.xlabel(x_label, fontsize = font_title), plt.ylabel(y_label, fontsize = font_title)

    if graph_type == 'time':
        #plt.xlim(xmin = 0)
        plt.ylim(ymin = 0.99*yval_min, ymax = 1.05*yval_max)
    if graph_type == 'beta' :
        plt.axhline(1, color = 'silver',linewidth=elinew)
        #plt.xlim(xmin = 0)
        plt.ylim(ymin = 0.99*yval_min, ymax = 1.05*yval_max)
    if graph_type == 'stress' :
        #plt.xlim(xmin = 0)
        plt.ylim(ymin = 0)
    if graph_type == 'granulence': plt.ylim(ymin = 0.99*yval_min, ymax = 1.05*yval_max)
    # end if

    if x_label == '$\u03b3$':
        g.regime_split_lines(xval, rd, stack, colormap, elinew, set_a)
    #if x_label == '$d_{G}$' or x_label == '$d_{K}$' or x_label == '\u03b8 / $\u27E8 \u03b8 \u27E9$' :
    #    regime_relax_split_lines(rd, stack, colormap, elinew, set_a)
    # end if

    plt.rc('axes', labelsize = font_axes, titlesize = font_axes)
    plt.rc('xtick', labelsize = font_axes), plt.rc('ytick', labelsize = font_axes)
    plt.legend(fontsize = font_legend, frameon=False, loc = 'upper left', labelspacing = label_space)
    #plt.savefig('relax_p_vs_t.png')
    plt.show()
    # return
    return

# Function graph call
def graph_ela_relax_I(val1,val2,val3,val4,val5,tag1,tag2,tag3,tag4,tag5,colormap,E,t,d,mod,no_stack):
    # Function variables
    # Scalar
    len_val = len(val1)

    # Vector
    color_g = [colormap(0.75),colormap(0.40),colormap(0.25),colormap(0.15),colormap(0.0)]
    tag_sh = ['','','','','']
    tag_p = [tag1,tag2,tag3,tag4,tag5]

    # Matrix
    y_fit_sh, y_fit_p = np.zeros((no_stack,len_val)), np.zeros((no_stack,len_val))
    time_adim,press_adim,S_xy_adim,Z_adim,vel_adim = val_var_1def(val1,val2,val3,val4,val5,E,t,d,no_stack)

    # Measured shear stress relaxation
    plot_relax_cumul(time_adim,S_xy_adim,'no','stress',y_fit_sh,color_g,'t / $t_{N}$','\u03c4/$E_{g}$',tag_sh,no_stack,'')

    # Pressure evolution
    plot_relax_cumul(time_adim,press_adim,'no','stress',y_fit_p,color_g,'t/ $t_{N}$','P/$E_{g}$',tag_p,no_stack,'')
    return

def graph_ela_relax(val1,val2,val3,val4,val5,val6,val7,val8,val9,val10,val11,val12,val13,val14,val15,val16,val17,val18,val19,coeff_sh,coeff_p,colormap,E,t,d,mod,no_relax): # !!! graph for the elastic relaxation
    # Function variables
    # Vector
    tag_sh = ['','','','','','','','','','','','','','','','','','','']
    #tag_sh = ['\u03b3 = 0','','$\u03b3 = 1.5 \u00b7 10^{-3}$','','','$\u03b3 = 1.5 \u00b7 10^{-2}$','','','','','$\u03b3 = 1.5 \u00b7 10^{-1}$','','','','$\u03b3 = 2 \u00b7 10^{-1}$','','','','$\u03b3 = 3 \u00b7 10^{-1}$']
    tag_p = ['','','','','','','','','','','','','','','','','','','']
    #tag_p = ['$\u03b3 = 0$','$\u03b3 = 7.5 \u00b7 10^{-4}$','$\u03b3 = 1.5 \u00b7 10^{-3}$','','','$\u03b3 = 1.5 \u00b7 10^{-2}$','','','','','$\u03b3 = 1.5 \u00b7 10^{-1}$','','','','$\u03b3 = 2 \u00b7 10^{-1}$','','','','$\u03b3 = 3 \u00b7 10^{-1}$']

    color_g = [colormap(0),colormap(0.05),colormap(0.1),colormap(0.15),colormap(0.2),colormap(0.25),colormap(0.3),colormap(0.35),colormap(0.4),colormap(0.45),colormap(0.5),colormap(0.55),colormap(0.6),colormap(0.65),colormap(0.7),colormap(0.75),colormap(0.8),colormap(0.85),colormap(0.9)]

    # Matrix
    y_fit_sh, y_fit_p = np.zeros((no_relax,len(val1))), np.zeros((no_relax,len(val1)))
    time,press,S_xy,Z,vel = val_var_cumul(val1,val2,val3,val4,val5,val6,val7,val8,val9,val10,val11,val12,val13,val14,val15,val16,val17,val18,val19,E,t,d,no_relax)

    for i in range(no_relax):
        for j in range(len(val1)):
            y_fit_sh[i,j] = rf.power_exp(time[j,i]*t,coeff_sh[i,0],coeff_sh[i,1],coeff_sh[i,2],coeff_sh[i,3])/E #,coeff_sh[i,4])/E
            y_fit_p[i,j] = rf.power_exp(time[j,i]*t,coeff_p[i,0],coeff_p[i,1],coeff_p[i,2],coeff_p[i,3])/E #,coeff_p[i,4])/E
        # end of j for loop
    # end of i for loop

    # Plot #
    # Coordination number relaxation
    plot_relax_cumul(time,Z,'no','coord',y_fit_sh,color_g,'t / $t_{N}$','Z',tag_sh,no_relax,'yes')

    # Measured shear stress relaxation
    plot_relax_cumul(time,S_xy,'yes','stress',y_fit_sh,color_g,'t / $t_{N}$','\u03c4 / $E_{g}$',tag_sh,no_relax,'yes')

    # Error with fit
    #plot_relax_cumul(time,S_xy,'no','delta',y_fit_sh,color_g,'t / $t_{N}$','\u0394 \u03c4 / $\u03c4_{0}$',tag_sh,no_relax,'yes')

    # Pressure evolution
    plot_relax_cumul(time,press,'yes','stress',y_fit_p,color_g,'t / $t_{N}$','P /$E_{g}$',tag_p,no_relax,'yes')

    # Error with fit
    #plot_relax_cumul(time,press,'no','delta',y_fit_p,color_g,'t/ $t_{N}$','\u0394 P / $P_{0}$',tag_p,no_relax,'yes')

    # Mean velocity relaxation
    #plot_relax_cumul(time, vel,'no','velocity',np.zeros((no_relax,len(val1))),color_g,'t/ $t_{N}$','(v $t_{N}$)/ $d_{ave}$',tag_sh,no_relax,'yes')
    return

def graph_granulence(x_val1,x_val2,x_val3,y_val,std_y_val,r_d,r_d_G,r_d_K,colormap1,colormap2,tag1,tag2,tag3,tag4,tag5,tag6,tag7,tag8,tag9,tag10,stack,max_stack,no_relax,mod,analysis):
    # Function variable
    # Vector
    color_g1, color_g2 = colormap1, colormap2

    #tag_gran = [tag1,tag2,tag3,tag4,tag5,tag6,tag7,tag8,tag9,tag10]
    tag_gran = ['','','','','','','','','','']

    y_label = '\u03b8 / $\u03c1_{g} (\.{\u03b3} \u00b7 l_{x} \u00b7 d\u0304_g)^2$'

    # Matrix
    # plot evolution of granulence versus gamma
    plot_relax_stacks(stack,x_val1,y_val,std_y_val,r_d,color_g1,color_g2,'yes','\u03b3',y_label,tag_gran,'granulence',1)

    # plot evolution of granulence versus d_G
    #scatter_relax_stacks(stack, x_val2, y_val, std_y_val, color_g, '$d_{G}$', '\u0394 \u03b8 / $\u03b8_{0}$', tag_gran, 'granulence')
    #scatter_relax_stacks(stack, x_val2, y_val, std_y_val, r_d_G, color_g, '$d_{G}$', y_label, tag_gran, 'granulence')

    # plot evolution of granulence versus d_K
    #scatter_relax_stacks(stack, x_val3, y_val, std_y_val, color_g, '$d_{K}$', '\u0394 \u03b8 / $\u03b8_{0}$', tag_gran, 'granulence')
    #scatter_relax_stacks(stack, x_val3, y_val, std_y_val, r_d_K, color_g, '$d_{K}$', y_label, tag_gran, 'granulence')
    return

def graph_relax(plt_ela_relax_1,plt_ela_relax_2,plt_ela_relax_3,plt_ela_relax_4,plt_ela_relax_5,plt_ela_relax_6,plt_ela_relax_7,plt_ela_relax_8,plt_ela_relax_9,plt_ela_relax_10,error_relax_1,error_relax_2,error_relax_3,error_relax_4,error_relax_5,error_relax_6,error_relax_7,error_relax_8,error_relax_9,error_relax_10,x_val,r_d,colormap1,colormap2,tag1,tag2,tag3,tag4,tag5,tag6,tag7,tag8,tag9,tag10,stack,max_stack,analysis,mod,x_type): # !!! graph for the relaxation time
    # Function variables #
    # Vector
    color_g1, color_g2 = colormap1, colormap2

    tag = ['','','','','','','','','','']
    #tag = [tag1,tag2,tag3,tag4,tag5,tag6,tag7,tag8,tag9,tag10]

    if x_type == 'gamma_0':
        x_label = '\u03b3'
        line = 1
    if x_type == 'phi':
        x_label = '\u03d5'
        line = 0
    if x_type == 'Z':
        x_label = 'Z'
        line = 0
    # end if

    if analysis == 'strain': tau_c_label, p_c_label = '$\u03c4_{c}/E_g$', '$P_{c}/E_g$'
    elif analysis == 'pressure': tau_c_label, p_c_label = '$\u03c4_{c}/\u03c3_{yy}$', '$P_{c}/\u03c3_{yy}$'

    # Matrix
    t_sh, t_p, sh_c, p_c, b_sh, b_p = val_mod(stack, plt_ela_relax_1, plt_ela_relax_2, plt_ela_relax_3, plt_ela_relax_4, plt_ela_relax_5, plt_ela_relax_6, plt_ela_relax_7, plt_ela_relax_8, plt_ela_relax_9, plt_ela_relax_10, max_stack,'d_evo')
    d_t_sh, d_t_p, d_sh_c, d_p_c, d_b_sh, d_b_p = val_error_mod(stack,error_relax_1,error_relax_2,error_relax_3,error_relax_4,error_relax_5, error_relax_6, error_relax_7, error_relax_8, error_relax_9, error_relax_10, max_stack,'d_evo')

    # Relaxation time of shear stress versus time
    plot_relax_stacks(stack,x_val,t_sh,d_t_sh,r_d,color_g1,color_g2,'yes',x_label,'$t_{\u03c4}^{*} / t_{N}$',tag,'time',line)

    # Relaxation time of pressure
    plot_relax_stacks(stack,x_val,t_p,d_t_p,r_d,color_g1,color_g2,'yes',x_label,'$t_{P}^{*} /t_{N}$',tag,'time',line)

    # Beta sh
    plot_relax_stacks(stack,x_val,b_sh,d_b_sh,r_d,color_g1,color_g2,'yes',x_label,'$\u03b2_{\u03c4}$',tag,'beta',line)

    # Beta p
    plot_relax_stacks(stack,x_val,b_p,d_b_p,r_d,color_g1,color_g2,'yes',x_label,'$\u03b2_{P}$',tag,'beta',line)

    # Shear yield stress
    plot_relax_stacks(stack,x_val,sh_c,d_sh_c,r_d,color_g1,color_g2,'yes',x_label,tau_c_label,tag,'stress',line)

    # Measured residual mean stress versus shear strain
    plot_relax_stacks(stack,x_val,p_c,d_p_c,r_d,color_g1,color_g2,'yes',x_label,p_c_label,tag,'stress',line)

    # Corelation beta and t* ?
    #scatter_relax_stacks(stack,b_sh[1:],t_sh[1:],d_t_sh[1:],color_g,'$\u03b2_{\u03c4}$','$t_{\u03c4}^{*}/t_{N}$',tag,'time')
    #scatter_relax_stacks(stack,b_p[1:],t_p[1:],d_t_p[1:],color_g,'$\u03b2_{P}$','$t_{P}^{*}/t_{N}$',tag,'time')
    return

def rheo_ela_prop(gamma,val1,val2,val3,val4,val5,val6,val7,val8,val9,val10,mod1,mod2,mod3,mod4,mod5,mod6,mod7,mod8,mod9,mod10,dmod1,dmod2,dmod3,dmod4,dmod5,dmod6,dmod7,dmod8,dmod9,dmod10,stack,stack_max,tag1,tag2,tag3,tag4,tag5,tag6,tag7,tag8,tag9,tag10,colormap1,colormap2,ana,mod,adim): # !!! graph for the rheo and ela prop
    # Function variable
    # Scalar
    #\u03c3_{yy}
    xlabel, ylabel = '$|s|/E_{g}$', '$P/E_{g}$'

    # Vector
    tag = [tag1,tag2,tag3,tag4,tag5,tag6,tag7,tag8,tag9,tag10]
    tag = ['','','','','','','','','','']

    # Extract rheo datas
    # Matrix
    press,S_xx,S_yy,S_xy,cis,e_vol,phi,Z,E_q = val_var_sh(val1,val2,val3,val4,val5,val6,val7,val8,val9,val10,stack,ana,adim,'')
    d_press,d_S_xx,d_S_yy,d_S_xy,d_cis,d_e_vol,d_phi,d_Z,d_E_q = val_var_sh(val1,val2,val3,val4,val5,val6,val7,val8,val9,val10,stack,ana,adim,'std')

    t_sh, t_p, sh_c, p_c, b_sh, b_p = val_mod(stack, mod1, mod2, mod3, mod4, mod5, mod6, mod7, mod8, mod9, mod10, stack_max,'d_evo')
    d_t_sh, d_t_p, d_sh_c, d_p_c, d_b_sh, d_b_p = val_error_mod(stack,dmod1,dmod2,dmod3,dmod4,dmod5,dmod6,dmod7,dmod8,dmod9,dmod10,stack_max,'d_evo')

    # Stress invariant computation
    s_ij = 0.5*((((S_xx-S_yy)**2)+(S_xy**2))**0.5)

    # s_c and yplot vs gamma
    scatter_rheo_prop(stack,s_ij,press,p_c,sh_c,colormap1,colormap2,xlabel,ylabel,tag)

    # tau & s_c
    #plot_rheo_prop(stack,cis,gamma,S_xy,d_S_xy,sh_c,d_sh_c,colormap1,colormap2,xlabel,ylabel,tag)

    # P & P_c
    #plot_rheo_prop(stack,cis,gamma,press,d_press,p_c,d_p_c,colormap1,colormap2,xlabel,ylabel,tag)
    return

def evo_prop(x_val,plt_ela_relax_1,plt_ela_relax_2,plt_ela_relax_3,plt_ela_relax_4,plt_ela_relax_5,plt_ela_relax_6,plt_ela_relax_7,plt_ela_relax_8,plt_ela_relax_9,plt_ela_relax_10,dG_ela,dam_G,dam_K,d_dam_G,d_dam_K,error_1,error_2,error_3,error_4,error_5,error_6,error_7,error_8,error_9,error_10,reg_dG,reg_dK,stack,tag1,tag2,tag3,tag4,tag5,tag6,tag7,tag8,tag9,tag10,colormap1,colormap2,max_stack,analysis,mod,graph_type):
    # Function variables #
    # Vector
    color_g1, color_g2 = colormap1, colormap2

    #tag = [tag1,tag2,tag3,tag4,tag5]
    tag = ['','','','','']

    if analysis == 'strain':
        if mod == 'shear' : tau_c_label = '$\u03c4_{c}/E_g$'
        elif mod == 'deviatoric' : tau_c_label = '$q_{c}/E_g$'
        p_c_label = '$P_{c}/E_g$'
    elif analysis == 'pressure':
        if mod == 'shear' : tau_c_label = '$\u03c4_{c}/\u03c3_{yy}$'
        elif mod == 'deviatoric' : tau_c_label = '$q_{c}/\u03c3_{yy}$'
        p_c_label = '$P_{c}/\u03c3_{yy}$'
    # end if
    # Matrix
    t_sh,t_p,sh_c,p_c,b_sh,b_p = val_mod(stack,plt_ela_relax_1,plt_ela_relax_2,plt_ela_relax_3,plt_ela_relax_4,plt_ela_relax_5,plt_ela_relax_6,plt_ela_relax_7,plt_ela_relax_8,plt_ela_relax_9,plt_ela_relax_10,max_stack,'d_evo')
    d_t_sh,d_t_p,d_sh_c,d_p_c,d_b_sh,d_b_p = val_error_mod(stack,error_1,error_2,error_3,error_4,error_5,error_6,error_7,error_8,error_9,error_10,max_stack,'d_evo')

    if graph_type == 'damage':
        # Shear stress yield versus damage d_G
        scatter_relax_stacks(stack,dam_G,sh_c,d_sh_c,reg_dG,color_g1,color_g2,'$d_{G}$',tau_c_label,tag,'stress')

        # Mean stress yield versus damage d_K
        scatter_relax_stacks(stack,dam_K,p_c,d_p_c,reg_dK,color_g1,color_g2,'$d_{K}$',p_c_label,tag,'stress')

        # Beta_sh versus damage d_G
        scatter_relax_stacks(stack,dam_G,b_sh,d_b_sh,reg_dG,color_g1,color_g2,'$d_{G}$','$\u03b2_{\u03c4}$',tag,'beta')

        # Beta_P versus damage d_K
        scatter_relax_stacks(stack,dam_K,b_p,d_b_p,reg_dK,color_g1,color_g2,'$d_{K}$','$\u03b2_{P}$',tag,'beta')

        # Shear stress relaxation time versus damage d_G
        scatter_relax_stacks(stack,dam_G,t_sh,d_t_sh,reg_dG,color_g1,color_g2,'$d_{G}$','$t_{\u03c4}^{*} /t_{N}$',tag,'time')

        # Mean stress relaxation time versus damage d_K
        scatter_relax_stacks(stack,dam_K,t_p,d_t_p,reg_dK,color_g1,color_g2,'$d_{K}$','$t_{P}^{*} /t_{N}$',tag,'time')
    # end if

    if graph_type == 'granulence':
        x_label = '\u03b8 / $\u03c1_{g} (\.{\u03b3} \u00b7 l_{x} \u00b7 d\u0304_g)^2$'
        # Shear stress yield versus granulence
        scatter_relax_stacks(stack,x_val,sh_c,d_sh_c,reg_dG,color_g1,color_g2,x_label,tau_c_label,tag,'stress')

        # Mean stress yield versus granulence
        scatter_relax_stacks(stack,x_val,p_c,d_p_c,reg_dG,color_g1,color_g2,x_label,p_c_label,tag,'stress')

        # Beta_sh versus damage granulence
        scatter_relax_stacks(stack,x_val,b_sh,d_b_sh,reg_dG,color_g1,color_g2,x_label,'$\u03b2_{\u03c4}$',tag,'beta')

        # Beta_P versus damage granulence
        scatter_relax_stacks(stack,x_val,b_p,d_b_p,reg_dG,color_g1,color_g2,x_label,'$\u03b2_{P}$',tag,'beta')

        # Shear stress relaxation time versus granulence+9
        scatter_relax_stacks(stack,x_val,t_sh,d_t_sh,reg_dG,color_g1,color_g2,x_label,'$t_{\u03c4}^{*} /t_{N}$',tag,'time')

        # Mean stress relaxation time versus granulence
        scatter_relax_stacks(stack,x_val,t_p,d_t_p,reg_dG,color_g1,color_g2,x_label,'$t_{P}^{*} /t_{N}$',tag,'time')
    # end if
    return