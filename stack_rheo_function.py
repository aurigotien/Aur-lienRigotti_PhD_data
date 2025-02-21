#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 13:41:27 2023

@author: rigottia
"""
import numpy as np
import scipy.optimize as sc

## File openning ##
def data_opening(path,name_file,ana):
    # open plt file
    stack = open(f"{path}/sh_ela/plt_{name_file}_{ana}.txt")
    stack.readline()
    stack_val = np.loadtxt(stack)

    # open phi value file
    phi = open(f"{path}/sh_ela/phi_{name_file}_{ana}.txt")
    phi.readline()
    phi_val = np.loadtxt(phi)

    # open z value file
    z = open(f"{path}/sh_ela/z_{name_file}_{ana}.txt")
    z.readline()
    z_val = np.loadtxt(z)

    # open q value file
    q = open(f"{path}/sh_ela/q_{name_file}_{ana}.txt")
    q.readline()
    q_val = np.loadtxt(q)

    # open q value file
    d_q = open(f"{path}/sh_ela/q_{name_file}_{ana}_std.txt")
    d_q.readline()
    d_q_val = np.loadtxt(d_q)

    # open sh value file
    sh = open(f"{path}/sh_ela/tau_{name_file}_{ana}.txt")
    sh.readline()
    sh_val = np.loadtxt(sh)

    # open sh value file
    d_sh = open(f"{path}/sh_ela/tau_{name_file}_{ana}_std.txt")
    d_sh.readline()
    d_sh_val = np.loadtxt(d_sh)

    # open pressure val file
    pressure = open(f"{path}/sh_ela/pressure_{name_file}_{ana}.txt")
    pressure.readline()
    pressure_val = np.loadtxt(pressure)

    # open d_pressure val file
    d_pressure = open(f"{path}/sh_ela/pressure_{name_file}_{ana}_std.txt")
    d_pressure.readline()
    d_pressure_val = np.loadtxt(d_pressure)

    # Close the file
    stack.close()
    phi.close()
    z.close()
    q.close()
    d_q.close()
    sh.close()
    d_sh.close()
    pressure.close()
    d_pressure.close()
    return stack_val,phi_val,z_val,q_val,d_q_val,sh_val,d_sh_val,pressure_val,d_pressure_val

def data_ela_opening(path,ela_name_file,ana):
    # Opening and extraction
    G = open(f"{path}/sh_ela/G_{ela_name_file}_{ana}.txt")
    G.readline()
    ela_G = np.loadtxt(G)

    # bulk modulus
    K = open(f"{path}/sh_ela/K_{ela_name_file}_{ana}.txt")
    K.readline()
    ela_K = np.loadtxt(K)

    # open error evolution file
    # shear modulus error
    d_G = open(f"{path}/sh_ela/std(G)_{ela_name_file}_{ana}.txt")
    d_G.readline()
    d_ela_G = np.loadtxt(d_G)

    # bulk modulus error
    d_K = open(f"{path}/sh_ela/std(K)_{ela_name_file}_{ana}.txt")
    d_K.readline()
    d_ela_K = np.loadtxt(d_K)

    # open damage evolution file
    # shear modulus damage
    dam_G = open(f"{path}/sh_ela/dam_G_{ela_name_file}_{ana}.txt")
    dam_G.readline()
    dam_ela_G = np.loadtxt(dam_G)

    # bulk modulus damage
    dam_K = open(f"{path}/sh_ela/dam_K_{ela_name_file}_{ana}.txt")
    dam_K.readline()
    dam_ela_K = np.loadtxt(dam_K)

    # open damage error evolution file
    # shear modulus damage
    ddam_G = open(f"{path}/sh_ela/std(dam_G)_{ela_name_file}_{ana}.txt")
    ddam_G.readline()
    ddam_ela_G = np.loadtxt(ddam_G)

    # bulk modulus damage
    ddam_K = open(f"{path}/sh_ela/std(dam_K)_{ela_name_file}_{ana}.txt")
    ddam_K.readline()
    ddam_ela_K = np.loadtxt(ddam_K)

    # Close the file
    G.close()
    K.close()
    d_G.close()
    d_K.close()
    return ela_G,ela_K,d_ela_G,d_ela_K,dam_ela_G,dam_ela_K,ddam_ela_G,ddam_ela_K

def data_relax_opening(path,relax_name_file,ana):
    # Relaxation parameters
    # Shear stress relaxation time
    t_sh = open(f"{path}/relax/t_sh_relax_{relax_name_file}_{ana}.txt")
    t_sh.readline()
    t_sh_relax = np.loadtxt(t_sh)

    # Mean stress relaxation time
    t_p = open(f"{path}/relax/t_p_relax_{relax_name_file}_{ana}.txt")
    t_p.readline()
    t_p_relax = np.loadtxt(t_p)

    # Deviatoric stress relaxation time
    t_q = open(f"{path}/relax/t_q_relax_{relax_name_file}_{ana}.txt")
    t_q.readline()
    t_q_relax = np.loadtxt(t_q)

    # Shear stress relaxation time
    s_sh = open(f"{path}/relax/s_sh_relax_{relax_name_file}_{ana}.txt")
    s_sh.readline()
    s_sh_relax = np.loadtxt(s_sh)

    # Deviatoric stress relaxation time
    s_q = open(f"{path}/relax/s_q_relax_{relax_name_file}_{ana}.txt")
    s_q.readline()
    s_q_relax = np.loadtxt(s_q)

    # Shear stress relaxation time
    s_p = open(f"{path}/relax/s_p_relax_{relax_name_file}_{ana}.txt")
    s_p.readline()
    s_p_relax = np.loadtxt(s_p)

    # Shear stress relaxation time
    b_sh = open(f"{path}/relax/beta_sh_relax_{relax_name_file}_{ana}.txt")
    b_sh.readline()
    b_sh_relax = np.loadtxt(b_sh)

    # Shear stress relaxation time
    b_p = open(f"{path}/relax/beta_p_relax_{relax_name_file}_{ana}.txt")
    b_p.readline()
    b_p_relax = np.loadtxt(b_p)

    # Close the file
    t_sh.close()
    t_p.close()
    s_sh.close()
    s_p.close()
    b_sh.close()
    b_p.close()
    return t_sh_relax,t_p_relax,t_q_relax,s_sh_relax,s_q_relax,s_p_relax,b_sh_relax,b_p_relax

def data_relax_err_opening(path,relax_name_file,ana):
    # Relaxation parameters
    # Shear stress relaxation time
    t_sh = open(f"{path}/relax/std_t_sh_relax_{relax_name_file}_{ana}.txt")
    t_sh.readline()
    t_sh_relax = np.loadtxt(t_sh)

    # Mean stress relaxation time
    t_p = open(f"{path}/relax/std_t_p_relax_{relax_name_file}_{ana}.txt")
    t_p.readline()
    t_p_relax = np.loadtxt(t_p)

    # Mean stress relaxation time
    t_q = open(f"{path}/relax/std_t_q_relax_{relax_name_file}_{ana}.txt")
    t_q.readline()
    t_q_relax = np.loadtxt(t_q)

    # Shear stress relaxation time
    s_sh = open(f"{path}/relax/std_s_sh_relax_{relax_name_file}_{ana}.txt")
    s_sh.readline()
    s_sh_relax = np.loadtxt(s_sh)

    # Deviatoric stress relaxation time
    s_q = open(f"{path}/relax/std_s_q_relax_{relax_name_file}_{ana}.txt")
    s_q.readline()
    s_q_relax = np.loadtxt(s_q)

    # Shear stress relaxation time
    s_p = open(f"{path}/relax/std_s_p_relax_{relax_name_file}_{ana}.txt")
    s_p.readline()
    s_p_relax = np.loadtxt(s_p)

    # Shear stress relaxation time
    b_sh = open(f"{path}/relax/std_beta_sh_relax_{relax_name_file}_{ana}.txt")
    b_sh.readline()
    b_sh_relax = np.loadtxt(b_sh)

    # Shear stress relaxation time
    b_p = open(f"{path}/relax/std_beta_p_relax_{relax_name_file}_{ana}.txt")
    b_p.readline()
    b_p_relax = np.loadtxt(b_p)

    # Close the file
    t_sh.close()
    t_p.close()
    s_sh.close()
    s_p.close()
    b_sh.close()
    b_p.close()
    return t_sh_relax,t_p_relax,t_q_relax,s_sh_relax,s_q_relax,s_p_relax,b_sh_relax,b_p_relax

## Value attribution in globale vector ##
# iner Matrix
def iner_mat(no_ela,max_stacks,cut):
    iner_1 = np.zeros((no_ela,max_stacks))
    iner_2 = np.zeros((no_ela,max_stacks))
    iner_3 = np.zeros((no_ela,max_stacks))
    iner_4 = np.zeros((no_ela,max_stacks))

    if cut == 'yes': cut_line = np.array([13,13,13,16,19])
    else : cut_line = np.array([0,0,0,0,0])

    for j in range(max_stacks):
        cut_lin = cut_line[j]
        for i in range(no_ela):
            if i >= cut_lin :
                # inertial number attribution
                if j == 0 : iner_1[i,j],iner_2[i,j],iner_3[i,j],iner_4[i,j] = 5E-3, 5E-3, 5E-3, 5E-3
                if j == 1 : iner_1[i,j],iner_2[i,j],iner_3[i,j],iner_4[i,j] = 1E-3, 1E-3, 1E-3, 1E-3
                if j == 2 : iner_1[i,j],iner_2[i,j],iner_3[i,j],iner_4[i,j] = 5E-4, 5E-4, 5E-4, 5E-4
                if j == 3 : iner_1[i,j],iner_2[i,j],iner_3[i,j],iner_4[i,j] = 1E-4, 1E-4, 1E-4, 1E-4
                if j == 4 : iner_1[i,j],iner_2[i,j],iner_3[i,j],iner_4[i,j] = 5E-5, 5E-5, 5E-5, 5E-5
            else :
                iner_1[i,j] = np.nan
                iner_2[i,j] = np.nan
                iner_3[i,j] = np.nan
                iner_4[i,j] = np.nan
        # end of i for loop
    # end of j for loop
    return iner_1, iner_2, iner_3, iner_4
# put the N plateau_N matrix into one matrix plateau
def global_rheo_vec(plat,plt1,plt2,plt3,plt4,stack,no_data):
    for i in range(no_data):
        for j in range(0,stack):
            if i == 0 :
                plat[j + 0,:] = plt1[j,:]
            elif i == 1 :
                plat[j + 5,:] = plt2[j,:]
            elif i == 2 :
                plat[j + 10,:] = plt3[j,:]
            elif i == 3 :
                plat[j + 15,:] = plt4[j,:]
    # end of i for loop
    return plat

def global_ela_vec(ela,ela1,ela2,ela3,ela4,stacks,no_data):
    for i in range(no_data):
        for j in range(0,stacks):
            if i == 0 :
                ela[:,j + 0] = ela1[:]
            elif i == 1 :
                ela[:,j + 5] = ela2[:]
            elif i == 2 :
                ela[:,j + 10] = ela3[:]
            elif i == 3 :
                ela[:,j + 15] = ela4[:]
    # end of i for loop
    return ela

def global_size_vec(size,size1,size2,size3,size4,stack,no_data):
    # Function variable
    step = 4 # value of the step of the i for loop

    for i in range(0,len(size),step):
        j = int(i / step) # compute ident to extract the size_N files
        # create the global matrix size
        size[i + 0,:] = size1[j,:]
        size[i + 1,:] = size2[j,:]
        size[i + 2,:] = size3[j,:]
        size[i + 3,:] = size4[j,:]
    # end of i for loop
    return size

def global_vec_fit(val1,val2,no_line,no_stack):
    # Function variable
    # Scalar
    len_tot = no_line*no_stack
    it = 0

    # Vector
    tot_vec = np.zeros((len_tot,2))

    # value attribution
    for i in range(no_line):
        for j in range(no_stack):
            tot_vec[it,0] = val1[i,j]
            tot_vec[it,1] = val2[i,j]
            it = it + 1
        # end of j for loop
    # end of i for loop
    return tot_vec

def global_param_vec(vec,vec1,vec2,vec3,vec4,vec5,stacks,no_data):
    for i in range(stacks):
        step = i*no_data
        for j in range(no_data):
            if i == 0:
                vec[step+j] = vec1[j]
            if i == 1:
                vec[step+j] = vec2[j]
            if i == 2:
                vec[step+j] = vec3[j]
            if i == 3:
                vec[step+j] = vec4[j]
            if i == 4:
                vec[step+j] = vec5[j]
            # end if
        # end of j for loop
    # end of i for loop
    return vec

def re_adim(val1,val2,val3,val4,dval1,dval2,dval3,dval4,source_press,no_line,no_data,val_adim):
    # Function variables
    # Scalar
    adim = 5E8 # input grain young modulus
    comp_max = 9E4
    comp_int = 5E4
    comp_min = 5E3

    # Vector
    comp = np.ones(no_data)

    # re-adimmensionement (function of E_g)
    for i in range(no_data):
        if source_press[i] == 'P_90000': comp[i] = comp_max
        elif source_press[i] == 'P_50000': comp[i] = comp_int
        elif source_press[i] == 'P_5000': comp[i] = comp_min

        if val_adim == 'val':
            if i == 0 : f1 = (val1*comp[i])/adim
            if i == 1 : f2 = (val2*comp[i])/adim
            if i == 2 : f3 = (val3*comp[i])/adim
            if i == 3 : f4 = (val4*comp[i])/adim
        elif val_adim == 'std':
            if i == 0 : f1 = (dval1/val1)*((val1*comp[i])/adim)
            if i == 1 : f2 = (dval2/val2)*((val2*comp[i])/adim)
            if i == 2 : f3 = (dval3/val3)*((val3*comp[i])/adim)
            if i == 3 : f4 = (dval4/val4)*((val4*comp[i])/adim)
        # end of i for loop
    return f1,f2,f3,f4

def E_nu(G,K,d_K,d_G,no_line,no_col):
    # Function variables
    # Matrix
    # elastic modulus
    E = np.zeros((no_line,no_col))
    nu = np.zeros((no_line,no_col))

    # uncertainty
    d_E = np.zeros((no_line,no_col))
    d_nu = np.zeros((no_line,no_col))

    for i in range(no_line):
        for j in range(no_col):
            # Elastic modulus
            if (K[i,j] + G[i,j]) == 0 : E[i,j], nu[i,j] = 0, 0
            else :
                E[i,j] = (4*K[i,j]*G[i,j])/(K[i,j]+G[i,j])
                nu[i,j] = (K[i,j]-G[i,j])/(K[i,j]+G[i,j])

            # uncertainty
            if K[i,j] == 0 or G[i,j] == 0 : d_E[i,j], d_nu[i,j] = 0, 0
            else :
                d_E[i,j] = 2*((d_K[i,j]/K[i,j])+(d_G[i,j]/G[i,j]))*E[i,j]
                d_nu[i,j] = 2*((d_K[i,j]/K[i,j])+(d_G[i,j]/G[i,j]))*nu[i,j]
        # end of j for loop
    # end of i for loop
    return E,nu,d_E,d_nu

def dam_E(E_1,E_2,E_3,E_4,no_line,no_col,no_val,press,prep):
    # Function variables
    # Matrix
    e_0 = np.zeros((no_val,no_col))

    # damage
    d_1 = np.zeros((no_line,no_col))
    d_2 = np.zeros((no_line,no_col))
    d_3 = np.zeros((no_line,no_col))
    d_4 = np.zeros((no_line,no_col))

    for i in range(no_val):
        e_0[0,:] = E_1[0,:]
        e_0[1,:] = E_2[0,:]
        e_0[2,:] = E_3[0,:]
        e_0[3,:] = E_2[0,:]
    # end of i for loop

    for i in range(no_line):
        for j in range(no_col):
            if e_0[0,j] != 0 : d_1[i,j] = 1-(E_1[i,j]/e_0[0,j])
            if e_0[1,j] != 0 : d_2[i,j] = 1-(E_2[i,j]/e_0[1,j])
            if e_0[2,j] != 0 : d_3[i,j] = 1-(E_3[i,j]/e_0[2,j])
            if e_0[3,j] != 0 and E_4[i,j] !=0 : d_4[i,j] = 1-(E_4[i,j]/e_0[3,j])
    return d_1, d_2, d_3, d_4

def mu_I(I, mu_c, mu_2, I_0):
    return mu_c + ((mu_2 - mu_c )/((I_0/I)+1))

def phi_I(I, phi_c, c_phi):
    return phi_c - c_phi*I

def herschel_bulkley(dg_dt,T_0,b,c):
    return T_0 + c*(dg_dt**b) # compute µ for val_coeff

def linear_fit(x_val,A,B):
    return A*x_val + B

def linear_dam_fit(x_val,A,B):
    return A*(1-x_val) + B

def power_fit(x_val,n,m):
    return n*x_val**(m)

def sigmoid_fit(x_val,A,B,C,D):
    return A + (B/(1+C*np.exp(D*x_val)))

def res_fit_sh(xval,alpha,beta):
    return (1/alpha)*(0.24 - xval)**(beta)

def res_fit_p(xval,alpha,beta):
    return (1/alpha)*(0.225 - xval)**(beta)

def state_function(x_val,val_c,alpha,beta):
    func = x_val
    for i in range(len(x_val)):
        if x_val[i] < val_c : func[i] = (1/alpha)*(val_c - x_val[i])**(beta)
        else: func[i] = 0
    # end of i for loop
    return func

## Fit compute ##
def mu_I_fit(x_data,y_data):
    # Function variable
    param = np.zeros(3) # store the parameters : m,t
    max_it = 1E3

    # First guess
    mu_c_ini = 0.4
    mu_2_ini = 0.7
    I_0_ini = 0.1
    val_0 = (mu_c_ini,mu_2_ini,I_0_ini) # start with values near those we expect

    # Perform the fit
    param[:], cv = sc.curve_fit(mu_I, np.float64(x_data), np.float64(y_data), p0 = np.float64(val_0), bounds = (0,1), method = 'trf', maxfev=max_it)

    # determine quality of the fit
    squaredDiffs = np.square(y_data - mu_I(x_data, param[0], param[1], param[2]))
    squaredDiffsFromMean = np.square(y_data - np.mean(y_data))
    Rsquare = (1 - np.sum(squaredDiffs) / np.sum(squaredDiffsFromMean))**0.5

    # end if
    print('first guess = ', val_0[:])
    print('param = ', param[:])
    print('dµ_c = ', cv[0,0])
    print('dµ_0 = ', cv[1,1])
    print('dI_0 = ', cv[2,2], '\n')
    #print(f"R² = {Rsquare**2}", "\n")
    # end while loop
    return param[:], Rsquare

def phi_fit(x_data,y_data):
    # Function variable
    param = np.zeros(2) # store the parameters : m,t
    max_it = 1E4

    # First guess
    phi_c = y_data[0]
    phi_min = y_data[len(y_data)-3]-y_data[0]
    val_0 = (phi_c,phi_min) # start with values near those we expect

    # Perform the fit
    param[:], cv = sc.curve_fit(phi_I, np.float64(x_data), np.float64(y_data), p0 = np.float64(val_0), bounds = (0,1), method = 'trf', maxfev=max_it)
    param[1] = param[0]-param[1]

    # determine quality of the fit
    squaredDiffs = np.square(y_data - phi_I(x_data, param[0], param[1]))
    squaredDiffsFromMean = np.square(y_data - np.mean(y_data))
    Rsquare = (1 - np.sum(squaredDiffs) / np.sum(squaredDiffsFromMean))**0.5

    # end if
    print('first guess = ', val_0[:])
    print('param = ', param[:])
    print('d_phi_c = ', cv[0,0])
    print('d_phi_min = ', cv[1,1], '\n')
    #print(f"R² = {Rsquare**2}", "\n")
    # end while loop
    return param[:], Rsquare

def herschel_bulkley_fit(x_data,y_data):
    # Function variable
        # Vector
    param = np.zeros(3) # store the parameters : m,t

    # First guess
    T_0_ini = y_data[0]
    b_ini = 1
    c_ini = 1
    val_0 = (T_0_ini,b_ini,c_ini) # start with values near those we expect

    # Perform the fit
    param[:], cv = sc.curve_fit(herschel_bulkley, np.float64(x_data), np.float64(y_data), p0 = np.float64(val_0))

    # determine quality of the fit
    squaredDiffs = np.square(y_data - herschel_bulkley(x_data, param[0], param[1], param[2]))
    squaredDiffsFromMean = np.square(y_data - np.mean(y_data))
    Rsquare = (1 - np.sum(squaredDiffs) / np.sum(squaredDiffsFromMean))**0.5

    # end if
    print('first guess = ', val_0[:])
    print('param = ', param[:])
    print(f"R² = {Rsquare**2}", "\n")
    # end while loop
    return param[:], Rsquare

def pow_fit(x_val1,x_val2,x_val3,y_val1,y_val2,y_val3,no_data):
    # Function variables
    # Scalar
    no_param = 2

    # Vector
    error = np.zeros(no_param)

    # Computation
    # reshape datas
    x_redim = np.array([x_val1[:1,:],x_val2[:1,:],x_val3[:1,:]])
    y_redim = np.array([y_val1[:1,:],y_val2[:1,:],y_val3[:1,:]])
    val = np.array([np.reshape(x_redim,1*5*(no_data-1)),np.reshape(y_redim,1*5*(no_data-1))])

    ## Fit function ##
    # power fit
    param, cv = sc.curve_fit(power_fit, val[0,:], val[1,:],p0 = (1,0.15),bounds=(0, 15),method='trf')
    for i in range(no_param): error[i] = cv[i,i]**0.5
    return param, error

def res_dam_fit(x_val1,x_val2,x_val3,x_val4,y_val1,y_val2,y_val3,y_val4,datatype):
    # Function variables
    # Scalar
    no_param = 2
    no_line = 19
    no_col = 5

    # Vector
    coeff = np.zeros(no_param)
    #prediction = np.zeros(no_col*no_line*4)

    # Computation
    # reshape datas
    x_redim = np.array([x_val1,x_val2,x_val3,x_val4])
    y_redim = np.array([y_val1,y_val2,y_val3,y_val4])

    valx = np.array(np.reshape(x_redim,no_col*no_line*4))
    valy = np.array(np.reshape(y_redim,no_col*no_line*4))

    xval_fit = np.zeros(no_col*no_line*4)
    yval_fit = np.zeros(no_col*no_line*4)

    if datatype == 'sh': d_c = 0.24
    elif datatype == 'p' : d_c = 0.225

    idx = 0
    for i in range(len(valx)):
        if valx[i] <= d_c and valx[i] > 0 :
            xval_fit[idx], yval_fit[idx] = valx[i], valy[i]
            idx = idx+1
        # end if
    # end of i for loop

    ## Fit function ##
    # residual stress vs dam fit
    if datatype == 'sh' : param, cv = sc.curve_fit(res_fit_sh, xval_fit[:idx], yval_fit[:idx], p0 = (0.6,1), bounds=(0,2),method='trf')
    elif datatype == 'p' : param, cv = sc.curve_fit(res_fit_p, xval_fit[:idx], yval_fit[:idx], p0 = (0.6,1), bounds=(0,2),method='trf')

    error = cv[1,1]**0.5
    coeff[0], coeff[1] = d_c, param[1]
    print("\n", "alpha = ", param[0])
    print("d_alpha = ", cv[0,0]**0.5)

    # compute R^2
    #prediction[:idx] = state_function(xval_fit[:idx],coeff[0],param[0],coeff[1])
    #num = sum((yval_fit[:idx]-prediction[:idx])**2)
    #denum = sum((yval_fit[:idx]-np.mean(yval_fit[:idx]))**2)
    #r = 1-(num/denum)
    #print("\n", "R^2 = ", r)
    return coeff, error

def visc_fit(x_val1,x_val2,x_val3,x_val4,y_val1,y_val2,y_val3,y_val4,data_type):
    # Function variables
    # Scalar
    no_param = 2
    no_line  = 19
    no_col = 5
    nos = 4
    no_visc_val = 21*4
    idx = 0

    # Vector
    coeff = np.zeros(no_param)
    dam_val = np.zeros(no_visc_val)
    visc = np.zeros(no_visc_val)
    prediction = np.zeros(no_visc_val)

    # Computation
    # reshape datas
    for h in range(nos):
        if h == 0 : xval, yval = x_val1, y_val1
        if h == 1 : xval, yval = x_val2, y_val2
        if h == 2 : xval, yval = x_val3, y_val3
        if h == 3 : xval, yval = x_val4, y_val4
        for i in range(no_line):
            for j in range(no_col):
                # remove nan values
                if np.isnan(yval[i,j]) == False :
                    dam_val[idx] = xval[i,j]
                    visc[idx] = yval[i,j]
                    idx = idx + 1
                # end if
            # end of j for loop
        # end of i for loop
    # end of h for loop

    # fit
    if data_type == 'sh' : param, cv = sc.curve_fit(power_fit,dam_val,visc,p0=(1E-4,-5),bounds=((0,-10),(5E-3,0)), method='trf')
    if data_type == 'p' : param, cv = sc.curve_fit(power_fit,dam_val,visc,p0=(1E-4,-5), bounds=((0,-10),(5E-3,0)), method ='trf')

    # r2
    if data_type == 'sh' : coeff[0], coeff[1] = 7E-4, -6.99
    if data_type == 'p' : coeff[0], coeff[1] = 1.95E-3, -6.99
    prediction = power_fit(dam_val,param[0],param[1])
    num = sum((visc - prediction)**2)
    denum = sum((visc - np.mean(visc))**2)
    r2 = 1 - (num/denum)
    print(data_type, ": R^2 = ", r2)
    return param, cv**0.5

def val_fit(x_val,y_val,stack,source):
    # Function variable
    # Scalar
    no_param = 2

    # Vector
    param = np.zeros(no_param)
    error = np.zeros(no_param)

    if source == 'no_fric_P_5000' or source == 'fric_P_50000': cut = 3
    else : cut = 4

    param[0], param[1] = - y_val[0,:cut].mean(), y_val[0,:cut].mean()
    return param, error

# Treatement function
## Matrix modifier ##
def visc_eff_mat(valu,std_valu,lin,col,no,t_adim):
    # Function variable
    # Vector
    visc = np.zeros((col,lin))
    std_visc = np.zeros((col,lin))

    cut_line = np.array([13,13,13,16,19])
    if no == 1 : cis = np.array([5E-4,1E-4,5E-5,1E-5,5E-6])
    if no == 2 : cis = np.array([3.75E-4,7.5E-5,3.75E-5,7.5E-6,3.75E-6])
    if no == 3 : cis = np.array([1.2E-4,2.5E-5,1.2E-5,2.5E-6,1.2E-6])
    if no == 4 : cis = np.array([3.75E-4,7.5E-5,3.75E-5,7.5E-6,3.75E-6])
    # end if

    # Visc computation
    for j in range(lin):
        cut_lin = cut_line[j]
        for i in range(col):
            if i >= cut_lin :
                visc[i,j] = valu[i,j]/(cis[j]*t_adim)
                std_visc[i,j] = (std_valu[i,j] / valu[i,j])*(valu[i,j]/(cis[j]*t_adim))
                """
                if j == 0 :
                    visc[i,j] = valu[i,j]/(cis[j])*9E4
                    std_visc[i,j] = (std_valu[i,j] / valu[i,j])*(valu[i,j]/(cis[j]))
                if j == 1 or j == 3 :
                    visc[i,j] = valu[i,j]/(cis[j])*5E4
                    std_visc[i,j] = (std_valu[i,j] / valu[i,j])*(valu[i,j]/(cis[j]))
                if j == 2 :
                    visc[i,j] = valu[i,j]/(cis[j])*5E3
                    std_visc[i,j] = (std_valu[i,j] / valu[i,j])*(valu[i,j]/(cis[j]))
                """
            else :
                visc[i,j] = np.nan
                std_visc[i,j] = np.nan
            # end if
        # end of i for loop
    # end j for loop
    return visc, std_visc

def eff_res_fric(s_c,p_c,ds_c,dp_c,no_line,no_col):
    # Function variable
    # Matrix
    mu_c = np.zeros((no_line,no_col))
    dmu_c = np.zeros((no_line,no_col))

    # Values matrix
    p_res = np.zeros((no_line,no_col))
    q_res = np.zeros((no_line,no_col))

    # compute residual friction mu_c
    for i in range(no_line):
        for j in range(no_col):
            # Matrix attribution
            q_res[i,j] = s_c[i,j]
            p_res[i,j] = p_c[i,j]

            # residual friction mu_c computation
            if p_res[i,j] != 0 : mu_c[i,j] = q_res[i,j] / p_res[i,j]
            else : mu_c[i,j] = 0

            # residual friction error computation
            if p_c[i,j] != 0 and s_c[i,j] != 0 :
                dmu_c[i,j] = ((ds_c[i,j]/q_res[i,j])+(dp_c[i,j]/p_res[i,j]))*mu_c[i,j]
            else : dmu_c[i,j] = 0
        # end of j for loop
    # end of i for loop
    return mu_c,dmu_c