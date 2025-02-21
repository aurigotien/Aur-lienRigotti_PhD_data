#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 20:11:35 2022

@author: rigottia
"""

# This code print all the saved datas as rheologies

import matplotlib.pyplot as plt
import numpy as np
import stack_rheo_function as rheo_f
import stack_rheo_graph as rheo_plt

### Main code ----------------------------------------------------------------- #
## Needed analysis ## --------------------------------------------------------- #

need_ela = 'yes'
need_visc = 'yes'
need_size = 'no'
need_fit = 'no' # fit of µ(I) & hb rheology
need_mu_i = 'no'

analyse = 'pressure' # strain or pressure

## Variables ## --------------------------------------------------------------- #
# Scalars
line = 5 # number of stack
col_stack = 16 # number of variables measured in a stack
col = 19 # number of variable measured of a prop stack
no_ela_file = 19
no_stack = 4
max_stack = 4

# linear fit coeff
no_lin_coeff = 2
no_pow_coeff = 2
no_sig_coeff = 4

# Txt chain
# size effect
"""
tag1 = 'N = 1000 grains, P = 50 kPa'
tag2 = 'N = 5000 grains, P = 50 kPa'
tag3 = 'N = 10000 grains, P = 50 kPa'
tag4 = 'N = 20000 grains, P = 50 kPa'
path_size = ''
"""

# influence of imposed compression
#"""
tag1 = ''
tag2 = ''
tag3 = ''
tag4 = ''
path_size = ''
#"""

# name variables
#press_1 = "P_50000"
press_1 = "P_90000"
grain_1 = "N_10000"

press_2 = "P_50000"
grain_2 = "N_10000"

press_3 = "P_5000"
grain_3 = "N_10000"

press_4 = "P_50000"
grain_4 = "N_10000"

# print(type(x_tot))ensional parameters
E = 5E8 # material (sea ice) young modulus (Pa)
t_n = 7E-2 # grain normal oscillation time (s)
d_ave = 100 # grain average diameter (m)

# Colormaps
colormap_g = plt.get_cmap('jet')
colormap_ela = plt.get_cmap('jet')

# files stack 1
prep_1 = 'prep_no_fric'
name_file_1 = f"{grain_1}_{press_1}"
ela_name_file_1 = f"{grain_1}_{press_1}_ela"
relax_name_file_1 = f"{grain_1}_{press_1}"
cara_ela_1 = f'{prep_1}_{press_1}'

# files stack 2
#prep_2 = 'prep_no_fric'
prep_2 = 'prep_no_fric'
name_file_2 = f"{grain_2}_{press_2}"
ela_name_file_2 = f"{grain_2}_{press_2}_ela"
relax_name_file_2 = f"{grain_2}_{press_2}"
cara_ela_2 = f'{prep_2}_{press_2}'

# files stack 3
prep_3 = 'prep_no_fric'
name_file_3 = f"{grain_3}_{press_3}"
ela_name_file_3 = f"{grain_3}_{press_3}_ela"
relax_name_file_3 = f"{grain_3}_{press_3}"
cara_ela_3 = f'{prep_3}_{press_3}'

# files stack 4
prep_4 = 'prep_fric'
name_file_4 = f"{grain_4}_{press_4}"
ela_name_file_4 = f"{grain_4}_{press_4}_ela"
relax_name_file_4 = f"{grain_4}_{press_4}"
cara_ela_4 = f'{prep_4}_{press_4}'

# Matrix
stack_1 = np.zeros((col,line))
stack_2 = np.zeros((col,line))
stack_3 = np.zeros((col,line))
stack_4 = np.zeros((col,line))

# Phi values
phi_1 = np.zeros((col,line))
phi_2 = np.zeros((col,line))
phi_3 = np.zeros((col,line))
phi_4 = np.zeros((col,line))

# Z values
z_1 = np.zeros((col,line))
z_2 = np.zeros((col,line))
z_3 = np.zeros((col,line))
z_4 = np.zeros((col,line))

sh_1 = np.zeros((col,line))
sh_2 = np.zeros((col,line))
sh_3 = np.zeros((col,line))
sh_4 = np.zeros((col,line))

d_sh_1 = np.zeros((col,line))
d_sh_2 = np.zeros((col,line))
d_sh_3 = np.zeros((col,line))
d_sh_4 = np.zeros((col,line))

q_1 = np.zeros((col,line))
q_2 = np.zeros((col,line))
q_3 = np.zeros((col,line))
q_4 = np.zeros((col,line))

d_q_1 = np.zeros((col,line))
d_q_2 = np.zeros((col,line))
d_q_3 = np.zeros((col,line))
d_q_4 = np.zeros((col,line))

pressure_1 = np.zeros((col,line))
pressure_2 = np.zeros((col,line))
pressure_3 = np.zeros((col,line))
pressure_4 = np.zeros((col,line))

d_pressure_1 = np.zeros((col,line))
d_pressure_2 = np.zeros((col,line))
d_pressure_3 = np.zeros((col,line))
d_pressure_4 = np.zeros((col,line))

# Elasti properties values
if need_ela == 'yes' :
    # shear modulus
    G_1 = np.zeros((col,line))
    G_2 = np.zeros((col,line))
    G_3 = np.zeros((col,line))
    G_4 = np.zeros((col,line))

    # bulk modulus
    K_1 = np.zeros((col,line))
    K_2 = np.zeros((col,line))
    K_3 = np.zeros((col,line))
    K_4 = np.zeros((col,line))

    # error
    # shear modulus
    d_G_1 = np.zeros((col,line))
    d_G_2 = np.zeros((col,line))
    d_G_3 = np.zeros((col,line))
    d_G_4 = np.zeros((col,line))

    # bulk modulus
    d_K_1 = np.zeros((col,line))
    d_K_2 = np.zeros((col,line))
    d_K_3 = np.zeros((col,line))
    d_K_4 = np.zeros((col,line))

    # Damage evolution
    # shear modulus
    dam_G_1 = np.zeros((col,line))
    dam_G_2 = np.zeros((col,line))
    dam_G_3 = np.zeros((col,line))
    dam_G_4 = np.zeros((col,line))

    # bulk modulus
    dam_K_1 = np.zeros((col,line))
    dam_K_2 = np.zeros((col,line))
    dam_K_3 = np.zeros((col,line))
    dam_K_4 = np.zeros((col,line))

    # Damage error evolution
    # shear modulus
    d_dam_G_1 = np.zeros((col,line))
    d_dam_G_2 = np.zeros((col,line))
    d_dam_G_3 = np.zeros((col,line))
    d_dam_G_4 = np.zeros((col,line))

    # bulk modulus
    d_dam_K_1 = np.zeros((col,line))
    d_dam_K_2 = np.zeros((col,line))
    d_dam_K_3 = np.zeros((col,line))
    d_dam_K_4 = np.zeros((col,line))

    # fit param
    G_P = np.zeros(no_pow_coeff)
    G_phi = np.zeros((line,no_pow_coeff))
    G_dam = np.zeros((max_stack,no_lin_coeff))

    K_P = np.zeros((no_pow_coeff))
    K_phi = np.zeros((line,no_pow_coeff))
    K_dam = np.zeros((max_stack,no_lin_coeff))
# end if

# Relaxation parameters
if need_visc == 'yes':
    # Param
    t_sh_1 = np.zeros((col,line))
    t_sh_2 = np.zeros((col,line))
    t_sh_3 = np.zeros((col,line))
    t_sh_4 = np.zeros((col,line))

    t_p_1 = np.zeros((col,line))
    t_p_2 = np.zeros((col,line))
    t_p_3 = np.zeros((col,line))
    t_p_4 = np.zeros((col,line))

    t_q_1 = np.zeros((col,line))
    t_q_2 = np.zeros((col,line))
    t_q_3 = np.zeros((col,line))
    t_q_4 = np.zeros((col,line))

    s_sh_1 = np.zeros((col,line))
    s_sh_2 = np.zeros((col,line))
    s_sh_3 = np.zeros((col,line))
    s_sh_4 = np.zeros((col,line))

    s_q_1 = np.zeros((col,line))
    s_q_2 = np.zeros((col,line))
    s_q_3 = np.zeros((col,line))
    s_q_4 = np.zeros((col,line))

    s_p_1 = np.zeros((col,line))
    s_p_2 = np.zeros((col,line))
    s_p_3 = np.zeros((col,line))
    s_p_4 = np.zeros((col,line))

    beta_sh_1 = np.zeros((col,line))
    beta_sh_2 = np.zeros((col,line))
    beta_sh_3 = np.zeros((col,line))
    beta_sh_4 = np.zeros((col,line))

    beta_p_1 = np.zeros((col,line))
    beta_p_2 = np.zeros((col,line))
    beta_p_3 = np.zeros((col,line))
    beta_p_4 = np.zeros((col,line))

    # Error
    d_t_sh_1 = np.zeros((col,line))
    d_t_sh_2 = np.zeros((col,line))
    d_t_sh_3 = np.zeros((col,line))
    d_t_sh_4 = np.zeros((col,line))

    d_t_p_1 = np.zeros((col,line))
    d_t_p_2 = np.zeros((col,line))
    d_t_p_3 = np.zeros((col,line))
    d_t_p_4 = np.zeros((col,line))

    d_t_q_1 = np.zeros((col,line))
    d_t_q_2 = np.zeros((col,line))
    d_t_q_3 = np.zeros((col,line))
    d_t_q_4 = np.zeros((col,line))

    d_s_sh_1 = np.zeros((col,line))
    d_s_sh_2 = np.zeros((col,line))
    d_s_sh_3 = np.zeros((col,line))
    d_s_sh_4 = np.zeros((col,line))

    d_s_p_1 = np.zeros((col,line))
    d_s_p_2 = np.zeros((col,line))
    d_s_p_3 = np.zeros((col,line))
    d_s_p_4 = np.zeros((col,line))

    d_beta_sh_1 = np.zeros((col,line))
    d_beta_sh_2 = np.zeros((col,line))
    d_beta_sh_3 = np.zeros((col,line))
    d_beta_sh_4 = np.zeros((col,line))

    d_beta_p_1 = np.zeros((col,line))
    d_beta_p_2 = np.zeros((col,line))
    d_beta_p_3 = np.zeros((col,line))
    d_beta_p_4 = np.zeros((col,line))

    t_sh_dam = np.zeros((max_stack,no_lin_coeff))
    t_p_dam = np.zeros((max_stack,no_lin_coeff))

    s_sh_dam = np.zeros((max_stack,no_lin_coeff))
    s_p_dam = np.zeros((max_stack,no_lin_coeff))

    fit_s_sh_dam = np.zeros((max_stack,no_sig_coeff))
    fit_s_p_dam = np.zeros((max_stack,no_sig_coeff))
# end if

if need_size == 'yes':
    path_size = 'size_effect'
elif need_mu_i == 'yes':
    path_size = 'mu_I'
# end if

## Open the data files
if no_stack >= 1 :
    if need_mu_i == 'yes': path_size_1 = path_size
    else : path_size_1 = f"data_{grain_1}/{prep_1}"
    path = f"/home/rigottia/Nextcloud/Documents/stacks_read/rheo/{path_size_1}/{press_1}"

    # open plt file
    stack_1,phi_1,z_1,q_1,d_q_1,sh_1,d_sh_1,pressure_1,d_pressure_1 = rheo_f.data_opening(path,name_file_1,analyse)

    if need_ela == 'yes': # elastic properties file
        G_1,K_1,d_G_1,d_K_1,dam_G_1,dam_K_1,d_dam_G_1,d_dam_K_1 = rheo_f.data_ela_opening(path,ela_name_file_1,analyse)
    # end if

    if need_visc == 'yes': # relaxation parameters
        t_sh_1,t_p_1,t_q_1,s_sh_1,s_q_1,s_p_1,beta_sh_1,beta_p_1 = rheo_f.data_relax_opening(path, relax_name_file_1,analyse)
        d_t_sh_1,d_t_p_1,d_t_q_1,d_s_sh_1,d_s_q_1,d_s_p_1,d_beta_sh_1,d_beta_p_1 = rheo_f.data_relax_err_opening(path, relax_name_file_1,analyse)
    # end if

if no_stack >= 2 :
    if need_mu_i == 'yes': path_size_2 = path_size
    else : path_size_2 = f"data_{grain_2}/{prep_2}"
    path =  f"/home/rigottia/Nextcloud/Documents/stacks_read/rheo/{path_size_2}/{press_2}"

    # open plt file
    stack_2,phi_2,z_2,q_2,d_q_2,sh_2,d_sh_2,pressure_2,d_pressure_2 = rheo_f.data_opening(path,name_file_2,analyse)

    if need_ela == 'yes': # elastic properties file
        G_2,K_2,d_G_2,d_K_2,dam_G_2,dam_K_2,d_dam_G_2,d_dam_K_2 = rheo_f.data_ela_opening(path,ela_name_file_2,analyse)
    # end if

    if need_visc == 'yes': # relaxation parameters
        t_sh_2,t_p_2,t_q_2,s_sh_2,s_q_2,s_p_2,beta_sh_2,beta_p_2 = rheo_f.data_relax_opening(path,relax_name_file_2,analyse)
        d_t_sh_2,d_t_p_2,d_t_q_2,d_s_sh_2,d_s_q_2,d_s_p_2,d_beta_sh_2,d_beta_p_2 = rheo_f.data_relax_err_opening(path, relax_name_file_2,analyse)
    # end if

if no_stack >= 3 :
    if need_mu_i == 'yes': path_size_3 = path_size
    else : path_size_3 = f"data_{grain_3}/{prep_3}"
    path =  f"/home/rigottia/Nextcloud/Documents/stacks_read/rheo/{path_size_3}/{press_3}"

    # open plt file
    stack_3,phi_3,z_3,q_3,d_q_3,sh_3,d_sh_3,pressure_3,d_pressure_3 = rheo_f.data_opening(path,name_file_3,analyse)

    if need_ela == 'yes': # elastic properties file
        G_3,K_3,d_G_3,d_K_3,dam_G_3,dam_K_3,d_dam_G_3,d_dam_K_3 = rheo_f.data_ela_opening(path,ela_name_file_3,analyse)
    # end if

    if need_visc == 'yes': # relaxation parameters
        t_sh_3,t_p_3,t_q_3,s_sh_3,s_q_3,s_p_3,beta_sh_3,beta_p_3 = rheo_f.data_relax_opening(path,relax_name_file_3,analyse)
        d_t_sh_3,d_t_p_3,d_t_q_3,d_s_sh_3,d_s_q_3,d_s_p_3,d_beta_sh_3,d_beta_p_3 = rheo_f.data_relax_err_opening(path, relax_name_file_3,analyse)
    # end if

if no_stack >= 4 :
    if need_mu_i == 'yes': path_size_4 = path_size
    else : path_size_4 = f"data_{grain_4}/{prep_4}"
    path =  f"/home/rigottia/Nextcloud/Documents/stacks_read/rheo/{path_size_4}/{press_4}"

    # open plt file
    stack_4,phi_4,z_4,q_4,d_q_4,sh_4,d_sh_4,pressure_4,d_pressure_4 = rheo_f.data_opening(path,name_file_4,analyse)

    if need_ela == 'yes': # elastic properties file
        G_4,K_4,d_G_4,d_K_4,dam_G_4,dam_K_4,d_dam_G_4,d_dam_K_4 = rheo_f.data_ela_opening(path,ela_name_file_4,analyse)
    # end if

    if need_visc == 'yes': # relaxation parameters
        t_sh_4,t_p_4,t_q_4,s_sh_4,s_q_4,s_p_4,beta_sh_4,beta_p_4 = rheo_f.data_relax_opening(path,relax_name_file_4,analyse)
        d_t_sh_4,d_t_p_4,d_t_q_4,d_s_sh_4,d_s_q_4,d_s_p_4,d_beta_sh_4,d_beta_p_4 = rheo_f.data_relax_err_opening(path, relax_name_file_4,analyse)
    # end if

# redimmensioned elastic datas for pressure corelation
#"""
pressure_redim_1,pressure_redim_2,pressure_redim_3,pressure_redim_4 = rheo_f.re_adim(pressure_1,pressure_2,pressure_3,pressure_4,d_pressure_1,d_pressure_2,d_pressure_3,d_pressure_4,np.array([press_1,press_2,press_3,press_4]),line,no_stack,'val')
d_pressure_redim_1,d_pressure_redim_2,d_pressure_redim_3,d_pressure_redim_4 = rheo_f.re_adim(pressure_1,pressure_2,pressure_3,pressure_4,d_pressure_1,d_pressure_2,d_pressure_3,d_pressure_4,np.array([press_1,press_2,press_3,press_4]),line,no_stack,'std')

q_redim_1,q_redim_2,q_redim_3,q_redim_4 = rheo_f.re_adim(q_1,q_2,q_3,q_4,d_q_1,d_q_2,d_q_3,d_q_4,np.array([press_1,press_2,press_3,press_4]),line,no_stack,'val')
d_q_redim_1,d_q_redim_2,d_q_redim_3,d_q_redim_4 = rheo_f.re_adim(q_1,q_2,q_3,q_4,d_q_1,d_q_2,d_q_3,d_q_4,np.array([press_1,press_2,press_3,press_4]),line,no_stack,'std')

sh_redim_1,sh_redim_2,sh_redim_3,sh_redim_4 = rheo_f.re_adim(sh_1,sh_2,sh_3,sh_4,d_sh_1,d_sh_2,d_sh_3,d_sh_4,np.array([press_1,press_2,press_3,press_4]),line,no_stack,'val')
d_sh_redim_1,d_sh_redim_2,d_sh_redim_3,d_sh_redim_4 = rheo_f.re_adim(sh_1,sh_2,sh_3,sh_4,d_sh_1,d_sh_2,d_sh_3,d_sh_4,np.array([press_1,press_2,press_3,press_4]),line,no_stack,'std')

s_p_redim_1,s_p_redim_2,s_p_redim_3,s_p_redim_4 = rheo_f.re_adim(s_p_1,s_p_2,s_p_3,s_p_4,d_s_p_1,d_s_p_2,d_s_p_3,d_s_p_4,np.array([press_1,press_2,press_3,press_4]),line,no_stack,'val')
d_s_p_redim_1,d_s_p_redim_2,d_s_p_redim_3,d_s_p_redim_4 = rheo_f.re_adim(s_p_1,s_p_2,s_p_3,s_p_4,d_s_p_1,d_s_p_2,d_s_p_3,d_s_p_4,np.array([press_1,press_2,press_3,press_4]),line,no_stack,'std')

s_q_redim_1,s_q_redim_2,s_q_redim_3,s_q_redim_4 = rheo_f.re_adim(s_q_1,s_q_2,s_q_3,s_q_4,d_s_q_1,d_s_q_2,d_s_q_3,d_s_q_4,np.array([press_1,press_2,press_3,press_4]),line,no_stack,'val')
d_s_q_redim_1,d_s_q_redim_2,d_s_q_redim_3,d_s_q_redim_4 = rheo_f.re_adim(s_q_1,s_q_2,s_q_3,s_q_4,d_s_q_1,d_s_q_2,d_s_q_3,d_s_q_4,np.array([press_1,press_2,press_3,press_4]),line,no_stack,'std')
#"""

if need_ela == 'yes':
    G_redim_1, G_redim_2, G_redim_3, G_redim_4 = rheo_f.re_adim(G_1,G_2,G_3,G_4,d_G_1,d_G_2,d_G_3,d_G_4,np.array([press_1,press_2,press_3,press_4]),line,no_stack,'val')
    K_redim_1, K_redim_2, K_redim_3, K_redim_4 = rheo_f.re_adim(K_1,K_2,K_3,K_4,d_K_1,d_K_2,d_K_3,d_K_4,np.array([press_1,press_2,press_3,press_4]),line,no_stack,'val')
    d_G_redim_1, d_G_redim_2, d_G_redim_3, d_G_redim_4 = rheo_f.re_adim(d_G_1,d_G_2,d_G_3,d_G_4,d_K_1,d_K_2,d_K_3,d_K_4,np.array([press_1,press_2,press_3,press_4]),line,no_stack,'std')
    d_K_redim_1, d_K_redim_2, d_K_redim_3, d_K_redim_4 = rheo_f.re_adim(d_K_1,d_K_2,d_K_3,d_K_4,d_K_1,d_K_2,d_K_3,d_K_4,np.array([press_1,press_2,press_3,press_4]),line,no_stack,'std')
# end if

# change 0 values to nan in matrix and adimensionement
print('\n Parameter correlations \n')

if need_ela == 'yes' and need_visc == 'yes':
    if no_stack == max_stack :
        #""" # Elasticity vs P power fit
        G_P, dG_P = rheo_f.pow_fit(pressure_redim_1,pressure_redim_2,pressure_redim_3,G_redim_1,G_redim_2,G_redim_3,no_stack)
        K_P, dK_P = rheo_f.pow_fit(pressure_redim_1,pressure_redim_2,pressure_redim_3, K_redim_1,K_redim_2,K_redim_3,no_stack)

        print("G_P = ", G_P)
        print("error G_P fit = ", dG_P)
        print("K_P = ", K_P)
        print("error K_P fit = ", dK_P)

        # Elasticity vs damage linear fit
        G_dam[0,:], d_fit_G_1 = rheo_f.val_fit(dam_G_1, G_1, line, cara_ela_1)
        K_dam[0,:], d_fit_G_1 = rheo_f.val_fit(dam_K_1, K_1, line, cara_ela_1)

        G_dam[1,:], d_fit_G_2 = rheo_f.val_fit(dam_G_2, G_2, line, cara_ela_2)
        K_dam[1,:], d_fit_G_2 = rheo_f.val_fit(dam_K_2, K_2, line, cara_ela_2)

        G_dam[2,:], d_fit_G_3 = rheo_f.val_fit(dam_G_3, G_3, line, cara_ela_3)
        K_dam[2,:], d_fit_G_3 = rheo_f.val_fit(dam_K_3, K_3, line, cara_ela_3)

        G_dam[3,:], d_fit_G_4 = rheo_f.val_fit(dam_G_4, G_4, line, cara_ela_4)
        K_dam[3,:], d_fit_G_4 = rheo_f.val_fit(dam_K_4, K_4, line, cara_ela_4)
    # end if #"""

    if no_stack >= 1 : E_1,nu_1,d_E_1,d_nu_1 = rheo_f.E_nu(G_1, K_1, d_K_1, d_G_1, col, line)
    if no_stack >= 2 : E_2,nu_2,d_E_2,d_nu_2 = rheo_f.E_nu(G_2, K_2, d_K_2, d_G_2, col, line)
    if no_stack >= 3 : E_3,nu_3,d_E_3,d_nu_3 = rheo_f.E_nu(G_3, K_3, d_K_3, d_G_3, col, line)
    if no_stack >= 4 : E_4,nu_4,d_E_4,d_nu_4 = rheo_f.E_nu(G_4, K_4, d_K_4, d_G_4, col, line)

    press_applied = np.array([press_1,press_2,press_3,press_4])
    prep_used = np.array([prep_1,prep_2,prep_3,prep_4])

    dam_E_1,dam_E_2,dam_E_3,dam_E_4 = rheo_f.dam_E(E_1,E_2,E_3,E_4,col,line,no_stack,press_applied,prep_used)
# end if

if need_ela == 'yes' and need_visc == 'yes':
    """
    # Effective shear viscosity
    eta_eff_1, deta_eff_1 = rheo_f.visc_eff_mat(q_1,d_q_1,line,col,1,t_n)
    eta_eff_2, deta_eff_2 = rheo_f.visc_eff_mat(q_2,d_q_2,line,col,2,t_n)
    eta_eff_3, deta_eff_3 = rheo_f.visc_eff_mat(q_3,d_q_3,line,col,3,t_n)
    eta_eff_4, deta_eff_4 = rheo_f.visc_eff_mat(q_4,d_q_4,line,col,4,t_n)

    # Effective pressure viscosity
    zeta_eff_1, dzeta_eff_1 = rheo_f.visc_eff_mat(pressure_1,d_pressure_1,line,col,1,t_n)
    zeta_eff_2, dzeta_eff_2 = rheo_f.visc_eff_mat(pressure_2,d_pressure_2,line,col,2,t_n)
    zeta_eff_3, dzeta_eff_3 = rheo_f.visc_eff_mat(pressure_3,d_pressure_3,line,col,3,t_n)
    zeta_eff_4, dzeta_eff_4 = rheo_f.visc_eff_mat(pressure_4,d_pressure_4,line,col,4,t_n)
    #"""

    # Effective shear viscosity
    #"""
    eta_eff_1, deta_eff_1 = rheo_f.visc_eff_mat(sh_redim_1,d_sh_redim_1,line,col,1,t_n)
    eta_eff_2, deta_eff_2 = rheo_f.visc_eff_mat(sh_redim_2,d_sh_redim_2,line,col,2,t_n)
    eta_eff_3, deta_eff_3 = rheo_f.visc_eff_mat(sh_redim_3,d_sh_redim_3,line,col,3,t_n)
    eta_eff_4, deta_eff_4 = rheo_f.visc_eff_mat(sh_redim_4,d_sh_redim_4,line,col,4,t_n)

    # Effective pressure viscosity
    zeta_eff_1, dzeta_eff_1 = rheo_f.visc_eff_mat(pressure_redim_1,d_pressure_redim_1,line,col,1,t_n)
    zeta_eff_2, dzeta_eff_2 = rheo_f.visc_eff_mat(pressure_redim_2,d_pressure_redim_2,line,col,2,t_n)
    zeta_eff_3, dzeta_eff_3 = rheo_f.visc_eff_mat(pressure_redim_3,d_pressure_redim_3,line,col,3,t_n)
    zeta_eff_4, dzeta_eff_4 = rheo_f.visc_eff_mat(pressure_redim_4,d_pressure_redim_4,line,col,4,t_n)
    #"""
# end if

if need_visc == 'yes':
    fit_q_c, err_fit_q_c = rheo_f.res_dam_fit(dam_G_1, dam_G_2, dam_G_3, dam_G_4, s_q_1, s_q_2, s_q_3, s_q_4, 'sh')
    print("\n", "param_q_c = ", fit_q_c)
    print("error q_c = ", err_fit_q_c, "\n")

    fit_p_c, err_fit_p_c = rheo_f.res_dam_fit(dam_K_1, dam_K_2, dam_K_3, dam_K_4, s_p_1, s_p_2, s_p_3, s_p_4, 'p')
    print("\n", "param_p_c = ", fit_p_c)
    print("error p_c = ", err_fit_p_c, "\n")

    fit_eta, err_fit_eta = rheo_f.visc_fit(dam_G_1, dam_G_2, dam_G_3, dam_G_4, eta_eff_1, eta_eff_2, eta_eff_3, eta_eff_4,'sh')
    print("\n", "param_eta = ", fit_eta)
    print("error eta = ", err_fit_eta, "\n")

    fit_zeta, err_fit_zeta = rheo_f.visc_fit(dam_K_1, dam_K_2, dam_K_3, dam_K_4, zeta_eff_1, zeta_eff_2, zeta_eff_3, zeta_eff_4,'p')
    print("\n", "param_zeta = ", fit_zeta)
    print("error zeta = ", err_fit_zeta, "\n")
# end if

# Print the rheology
print("(1/6) Show inertial evolution of stack plateau ? (yes/no)")
need_graph_plt = input()

if need_graph_plt == 'yes' :
    # residual values plot
    rheo_plt.graph_rheo(stack_1,stack_2,stack_3,stack_4,E,t_n,d_ave,no_stack,tag1,tag2,tag3,tag4,colormap_g,colormap_ela,need_fit,max_stack)

if need_ela == 'yes' or need_visc == 'yes':
    print("(2/6) Show parameters evolution ? (yes/no)")
    need_graph_param = input()

    if need_graph_param == 'yes':
        if need_ela == 'yes':
            rheo_plt.param_ela_graph(phi_1,phi_2,phi_3,phi_4,G_1,G_2,G_3,G_4,K_1,K_2,K_3,K_4,d_G_1,d_G_2,d_G_3,d_G_4,d_K_1,d_K_2,d_K_3,d_K_4,G_phi,K_phi,no_stack,tag1,tag2,tag3,tag4,colormap_g,no_ela_file,no_stack,line,'phi_ela')
            #rheo_plt.param_ela_graph(phi_1,phi_2,phi_3,phi_4,dam_G_1,dam_G_2,dam_G_3,dam_G_4,dam_K_1,dam_K_2,dam_K_3,dam_K_4,d_dam_G_1,d_dam_G_2,d_dam_G_3,d_dam_G_4,d_dam_K_1,d_dam_K_2,d_dam_K_3,d_dam_K_4,G_phi,K_phi,no_stack,tag1,tag2,tag3,tag4,colormap_g,no_ela_file,no_stack,line,'phi_dam')
            #rheo_plt.param_ela_graph(pressure_redim_1,pressure_redim_2,pressure_redim_3,pressure_redim_4,G_redim_1,G_redim_2,G_redim_3,G_redim_4,K_redim_1,K_redim_2,K_redim_3,K_redim_4,d_G_redim_1,d_G_redim_2,d_G_redim_3,d_G_redim_4,d_K_redim_1,d_K_redim_2,d_K_redim_3,d_K_redim_4,G_P,K_P,no_stack,tag1,tag2,tag3,tag4,colormap_g,no_ela_file,no_stack,line,'P_ela')
            #rheo_plt.param_ela_graph(K_redim_1,K_redim_2,K_redim_3,K_redim_4,G_redim_1,G_redim_2,G_redim_3,G_redim_4,K_redim_1,K_redim_2,K_redim_3,K_redim_4,d_G_redim_1,d_G_redim_2,d_G_redim_3,d_G_redim_4,d_K_redim_1,d_K_redim_2,d_K_redim_3,d_K_redim_4,G_P,K_P,no_stack,tag1,tag2,tag3,tag4,colormap_g,no_ela_file,no_stack,line,'ela_ela')
        # end if

        if need_visc == 'yes':
            s_ij_1, s_ij_2, s_ij_3, s_ij_4 = 0.5*np.sqrt((s_q_1**2)+(2*(s_sh_1**2))), 0.5*np.sqrt((s_q_2**2)+(2*(s_sh_2**2))), 0.5*np.sqrt((s_q_3**2)+(2*(s_sh_3**2))), 0.5*np.sqrt((s_q_4**2)+(2*(s_sh_4**2)))

            #rheo_plt.param_relax_graph('cis_time',phi_1,phi_2,phi_3,phi_4,t_sh_1,t_sh_2,t_sh_3,t_sh_4,t_p_1,t_p_2,t_p_3,t_p_4,d_t_sh_1,d_t_sh_2,d_t_sh_3,d_t_sh_4,d_t_p_1,d_t_p_2,d_t_p_3,d_t_p_4,tag1,tag2,tag3,tag4,colormap_g,no_ela_file,no_stack,line)
            rheo_plt.param_relax_graph('phi_time',phi_1,phi_2,phi_3,phi_4,t_sh_1,t_sh_2,t_sh_3,t_sh_4,t_p_1,t_p_2,t_p_3,t_p_4,d_t_sh_1,d_t_sh_2,d_t_sh_3,d_t_sh_4,d_t_p_1,d_t_p_2,d_t_p_3,d_t_p_4,tag1,tag2,tag3,tag4,colormap_g,no_ela_file,no_stack,line)
            #rheo_plt.param_relax_graph('phi_visc',phi_1,phi_2,phi_3,phi_4,eta_eff_1,eta_eff_2,eta_eff_3,eta_eff_4,zeta_eff_1,zeta_eff_2,zeta_eff_3,zeta_eff_4,deta_eff_1,deta_eff_2,deta_eff_3,deta_eff_4,dzeta_eff_1,dzeta_eff_2,dzeta_eff_3,dzeta_eff_4,tag1,tag2,tag3,tag4,colormap_g,no_ela_file,no_stack,line)
            #rheo_plt.param_relax_graph('phi_beta',phi_1,phi_2,phi_3,phi_4,beta_sh_1,beta_sh_2,beta_sh_3,beta_sh_4,beta_p_1,beta_p_2,beta_p_3,beta_p_4,d_beta_sh_1,d_beta_sh_2,d_beta_sh_3,d_beta_sh_4,d_beta_p_1,d_beta_p_2,d_beta_p_3,d_beta_p_4,tag1,tag2,tag3,tag4,colormap_g,no_ela_file,no_stack,line)
            rheo_plt.param_relax_graph('phi_stress',phi_1,phi_2,phi_3,phi_4,s_q_1,s_q_2,s_q_3,s_q_4,s_p_1,s_p_2,s_p_3,s_p_4,d_s_q_1,d_s_q_2,d_s_q_3,d_s_q_4,d_s_p_1,d_s_p_2,d_s_p_3,d_s_p_4,tag1,tag2,tag3,tag4,colormap_g,no_ela_file,no_stack,line)
            #rheo_plt.param_relax_graph('stress_stress',dam_G_1,dam_G_2,dam_G_3,dam_G_4,s_ij_1,s_ij_2,s_ij_3,s_ij_4,s_p_1,s_p_2,s_p_3,s_p_4,d_s_sh_1,d_s_sh_2,d_s_sh_3,d_s_sh_4,d_s_p_1,d_s_p_2,d_s_p_3,d_s_p_4,tag1,tag2,tag3,tag4,colormap_g,no_ela_file,no_stack,line)
            #rheo_plt.param_relax_graph('shear_t_shear',dam_G_1,dam_G_2,dam_G_3,dam_G_4,G_1,G_2,G_3,G_4,t_sh_1,t_sh_2,t_sh_3,t_sh_4,d_G_1,d_G_2,d_G_3,d_G_4,d_t_sh_1,d_t_sh_2,d_t_sh_3,d_t_sh_4,tag1,tag2,tag3,tag4,colormap_g,no_ela_file,no_stack,line)
            #rheo_plt.param_relax_graph('press_t_press',dam_K_1,dam_K_2,dam_K_3,dam_K_4,K_1,K_2,K_3,K_4,t_p_1,t_p_2,t_p_3,t_p_4,d_K_1,d_K_2,d_K_3,d_K_4,d_t_p_1,d_t_p_2,d_t_p_3,d_t_p_4,tag1,tag2,tag3,tag4,colormap_g,no_ela_file,no_stack,line)

            # pressure corelation
            #rheo_plt.param_relax_graph('P_time',pressure_redim_1,pressure_redim_2,pressure_redim_3,pressure_redim_4,t_sh_1,t_sh_2,t_sh_3,t_sh_4,t_p_1,t_p_2,t_p_3,t_p_4,d_t_sh_1,d_t_sh_2,d_t_sh_3,d_t_sh_4,d_t_p_1,d_t_p_2,d_t_p_3,d_t_p_4,tag1,tag2,tag3,tag4,colormap_g,no_ela_file,no_stack,line)
            #rheo_plt.param_relax_graph('P_stress',pressure_redim_1,pressure_redim_2,pressure_redim_3,pressure_redim_4,s_sh_1,s_sh_2,s_sh_3,s_sh_4,s_p_1,s_p_2,s_p_3,s_p_4,d_s_sh_1,d_s_sh_2,d_s_sh_3,d_s_sh_4,d_s_p_1,d_s_p_2,d_s_p_3,d_s_p_4,tag1,tag2,tag3,tag4,colormap_g,no_ela_file,no_stack,line)
            #rheo_plt.param_relax_graph('P_stress',pressure_1,pressure_2,pressure_3,pressure_4,s_q_1,s_q_2,s_q_3,s_q_4,s_p_1,s_p_2,s_p_3,s_p_4,d_s_q_1,d_s_q_2,d_s_q_3,d_s_q_4,d_s_p_1,d_s_p_2,d_s_p_3,d_s_p_4,tag1,tag2,tag3,tag4,colormap_g,no_ela_file,no_stack,line)
        # end if
    # end if
# end if

if need_ela == 'yes' and need_visc == 'yes':
    print("(3/6) Show parameters vs damage evolution ? (yes/no)")
    need_graph_dam_param = input()

    if need_graph_dam_param == 'yes':
        # visc vs I
        #rheo_plt.visc_graph(dam_G_1,dam_G_2,dam_G_3,dam_G_4,eta_eff_1,eta_eff_2,eta_eff_3,eta_eff_4,deta_eff_1,deta_eff_2,deta_eff_3,deta_eff_4,no_stack,tag1,tag2,tag3,tag4,'visc_sh_I',colormap_g,no_ela_file,no_stack,line)
        #rheo_plt.visc_graph(dam_K_1,dam_K_2,dam_K_3,dam_K_4,zeta_eff_1,zeta_eff_2,zeta_eff_3,zeta_eff_4,dzeta_eff_1,dzeta_eff_2,dzeta_eff_3,dzeta_eff_4,no_stack,tag1,tag2,tag3,tag4,'visc_p_I',colormap_g,no_ela_file,no_stack,line)

        #rheo_plt.visc_graph(pressure_redim_1,pressure_redim_2,pressure_redim_3,pressure_redim_4,eta_eff_1,eta_eff_2,eta_eff_3,eta_eff_4,deta_eff_1,deta_eff_2,deta_eff_3,deta_eff_4,no_stack,tag1,tag2,tag3,tag4,'visc_sh_p',colormap_g,no_ela_file,no_stack,line)
        #rheo_plt.visc_graph(pressure_redim_1,pressure_redim_2,pressure_redim_3,pressure_redim_4,zeta_eff_1,zeta_eff_2,zeta_eff_3,zeta_eff_4,dzeta_eff_1,dzeta_eff_2,dzeta_eff_3,dzeta_eff_4,no_stack,tag1,tag2,tag3,tag4,'visc_p_p',colormap_g,no_ela_file,no_stack,line)

        # visc vs visc
        #rheo_plt.visc_graph(zeta_eff_1,zeta_eff_2,zeta_eff_3,zeta_eff_4,eta_eff_1,eta_eff_2,eta_eff_3,eta_eff_4,dzeta_eff_1,dzeta_eff_2,dzeta_eff_3,dzeta_eff_4,no_stack,tag1,tag2,tag3,tag4,'visc_visc',colormap_g,no_ela_file,no_stack,line)

        # plot param vs dam
        # pressure and shear stress relaxation properties plot
        rheo_plt.param_dam_graph(dam_G_1,dam_G_2,dam_G_3,dam_G_4,dam_K_1,dam_K_2,dam_K_3,dam_K_4,t_sh_1,t_sh_2,t_sh_3,t_sh_4,t_p_1,t_p_2,t_p_3,t_p_4,d_t_sh_1,d_t_sh_2,d_t_sh_3,d_t_sh_4,d_t_p_1,d_t_p_2,d_t_p_3,d_t_p_4,t_sh_dam,t_p_dam,no_stack,tag1,tag2,tag3,tag4,'time_*',colormap_g,no_ela_file,no_stack,line)
        #rheo_plt.param_dam_graph(dam_G_1,dam_G_2,dam_G_3,dam_G_4,dam_K_1,dam_K_2,dam_K_3,dam_K_4,s_sh_1,s_sh_2,s_sh_3,s_sh_4,s_p_1,s_p_2,s_p_3,s_p_4,d_s_sh_1,d_s_sh_2,d_s_sh_3,d_s_sh_4,d_s_p_1,d_s_p_2,d_s_p_3,d_s_p_4,s_sh_dam,s_p_dam,no_stack,tag1,tag2,tag3,tag4,'sigma_c',colormap_g,no_ela_file,no_stack,line)

        # pressure and q_c plot
        #rheo_plt.param_dam_graph(pressure_redim_1,pressure_redim_2,pressure_redim_3,pressure_redim_4,pressure_redim_1,pressure_redim_2,pressure_redim_3,pressure_redim_4,s_q_1,s_q_2,s_q_3,s_q_4,s_p_1,s_p_2,s_p_3,s_p_4,d_s_q_1,d_s_q_2,d_s_q_3,d_s_q_4,d_s_p_1,d_s_p_2,d_s_p_3,d_s_p_4,G_dam,K_dam,no_stack,tag1,tag2,tag3,tag4,'sigma_c_P',colormap_g,no_ela_file,no_stack,line)

        # deviatoric stress and pressure residual stress plot
        #rheo_plt.param_dam_graph(dam_G_1,dam_G_2,dam_G_3,dam_G_4,dam_K_1,dam_K_2,dam_K_3,dam_K_4,s_q_1,s_q_2,s_q_3,s_q_4,s_p_1,s_p_2,s_p_3,s_p_4,d_s_q_1,d_s_q_2,d_s_q_3,d_s_q_4,d_s_p_1,d_s_p_2,d_s_p_3,d_s_p_4,G_dam,K_dam,no_stack,tag1,tag2,tag3,tag4,'iner',colormap_g,no_ela_file,no_stack,line)
        #rheo_plt.param_dam_graph(dam_G_1,dam_G_2,dam_G_3,dam_G_4,dam_K_1,dam_K_2,dam_K_3,dam_K_4,s_q_redim_1,s_q_redim_2,s_q_redim_3,s_q_redim_4,s_p_redim_1,s_p_redim_2,s_p_redim_3,s_p_redim_4,d_s_q_redim_1,d_s_q_redim_2,d_s_q_redim_3,d_s_q_redim_4,d_s_p_redim_1,d_s_p_redim_2,d_s_p_redim_3,d_s_p_redim_4,G_dam,K_dam,no_stack,tag1,tag2,tag3,tag4,'sigma_c',colormap_g,no_ela_file,no_stack,line)

        # stress invariant s and p
        # mu_c
        #rheo_plt.param_dam_graph(dam_G_1,dam_G_2,dam_G_3,dam_G_4,dam_E_1,dam_E_2,dam_E_3,dam_E_4,s_q_1,s_q_2,s_q_3,s_q_4,nu_1,nu_2,nu_3,nu_4,d_s_q_1,d_s_q_2,d_s_q_3,d_s_q_4,d_nu_1,d_nu_2,d_nu_3,d_nu_4,t_sh_dam,t_p_dam,no_stack,tag1,tag2,tag3,tag4,'nu',colormap_g,no_ela_file,no_stack,line)

        # Classical print
        # ela mod
        #rheo_plt.param_dam_graph(dam_G_1,dam_G_2,dam_G_3,dam_G_4,dam_K_1,dam_K_2,dam_K_3,dam_K_4,G_1,G_2,G_3,G_4,K_1,K_2,K_3,K_4,d_G_1,d_G_2,d_G_3,d_G_4,d_K_1,d_K_2,d_K_3,d_K_4,G_dam,K_dam,no_stack,tag1,tag2,tag3,tag4,'ela_mod',colormap_g,no_ela_file,no_stack,line)

        # visc vs dam
        #rheo_plt.visc_graph(dam_G_1,dam_G_2,dam_G_3,dam_G_4,eta_eff_1,eta_eff_2,eta_eff_3,eta_eff_4,deta_eff_1,deta_eff_2,deta_eff_3,deta_eff_4,no_stack,tag1,tag2,tag3,tag4,'visc_sh',colormap_g,no_ela_file,no_stack,line)
        #rheo_plt.visc_graph(dam_K_1,dam_K_2,dam_K_3,dam_K_4,zeta_eff_1,zeta_eff_2,zeta_eff_3,zeta_eff_4,dzeta_eff_1,dzeta_eff_2,dzeta_eff_3,dzeta_eff_4,no_stack,tag1,tag2,tag3,tag4,'visc_p',colormap_g,no_ela_file,no_stack,line)

        # time*
        #rheo_plt.param_dam_graph(dam_G_1,dam_G_2,dam_G_3,dam_G_4,dam_K_1,dam_K_2,dam_K_3,dam_K_4,t_q_1,t_q_2,t_q_3,t_q_4,t_p_1,t_p_2,t_p_3,t_p_4,d_t_q_1,d_t_q_2,d_t_q_3,d_t_q_4,d_t_p_1,d_t_p_2,d_t_p_3,d_t_p_4,t_sh_dam,t_p_dam,no_stack,tag1,tag2,tag3,tag4,'time_*_q',colormap_g,no_ela_file,no_stack,line)

        # residual stress s_c and p_c
        #rheo_plt.param_dam_graph(dam_G_1,dam_G_2,dam_G_3,dam_G_4,dam_K_1,dam_K_2,dam_K_3,dam_K_4,s_q_1,s_q_2,s_q_3,s_q_4,s_p_1,s_p_2,s_p_3,s_p_4,d_s_q_1,d_s_q_2,d_s_q_3,d_s_q_4,d_s_p_1,d_s_p_2,d_s_p_3,d_s_p_4,s_sh_dam,s_p_dam,no_stack,tag1,tag2,tag3,tag4,'sigma_c_q',colormap_g,no_ela_file,no_stack,line)
    # end if

if need_ela == 'yes' and need_visc == 'yes':
    print("(4/6) Show parameters vs damage evolution ? (yes/no)")
    need_3D_graph_dam_param = input()

    if need_3D_graph_dam_param == 'yes':
        #rheo_plt.param_dam_3D_graph(pressure_redim_1,pressure_redim_2,pressure_redim_3,pressure_redim_4,dam_G_1,dam_G_2,dam_G_3,dam_G_4,dam_K_1,dam_K_2,dam_K_3,dam_K_4,G_redim_1,G_redim_2,G_redim_3,G_redim_4,K_redim_1,K_redim_2,K_redim_3,K_redim_4,d_G_redim_1,d_G_redim_2,d_G_redim_3,d_G_redim_4,d_K_redim_1,d_K_redim_2,d_K_redim_3,d_K_redim_4,t_sh_dam,t_p_dam,no_stack,tag1,tag2,tag3,tag4,'ela_mod','press',colormap_g,no_ela_file,no_stack,line)
        #rheo_plt.param_dam_3D_graph(pressure_redim_1,pressure_redim_2,pressure_redim_3,pressure_redim_4,dam_G_1,dam_G_2,dam_G_3,dam_G_4,dam_K_1,dam_K_2,dam_K_3,dam_K_4,t_sh_1,t_sh_2,t_sh_3,t_sh_4,t_p_1,t_p_2,t_p_3,t_p_4,d_t_sh_1,d_t_sh_2,d_t_sh_3,d_t_sh_4,d_t_p_1,d_t_p_2,d_t_p_3,d_t_p_4,t_sh_dam,t_p_dam,no_stack,tag1,tag2,tag3,tag4,'time_*','press',colormap_g,no_ela_file,no_stack,line)
        #rheo_plt.param_dam_3D_graph(pressure_redim_1,pressure_redim_2,pressure_redim_3,pressure_redim_4,dam_G_1,dam_G_2,dam_G_3,dam_G_4,dam_K_1,dam_K_2,dam_K_3,dam_K_4,s_sh_1,s_sh_2,s_sh_3,s_sh_4,s_p_1,s_p_2,s_p_3,s_p_4,d_s_sh_1,d_s_sh_2,d_s_sh_3,d_s_sh_4,d_s_p_1,d_s_p_2,d_s_p_3,d_s_p_4,t_sh_dam,t_p_dam,no_stack,tag1,tag2,tag3,tag4,'sigma_c','press',colormap_g,no_ela_file,no_stack,line)
        #rheo_plt.param_dam_3D_graph(s_sh_1,s_sh_2,s_sh_3,s_sh_4,dam_G_1,dam_G_2,dam_G_3,dam_G_4,dam_K_1,dam_K_2,dam_K_3,dam_K_4,t_sh_1,t_sh_2,t_sh_3,t_sh_4,t_p_1,t_p_2,t_p_3,t_p_4,d_t_sh_1,d_t_sh_2,d_t_sh_3,d_t_sh_4,d_t_p_1,d_t_p_2,d_t_p_3,d_t_p_4,t_sh_dam,t_p_dam,no_stack,tag1,tag2,tag3,tag4,'time_*','$\u03c4_{c}/\u03c3_{yy}$',colormap_g,no_ela_file,no_stack,line)
        #rheo_plt.param_dam_3D_graph(s_p_1,s_p_2,s_p_3,s_p_4,dam_G_1,dam_G_2,dam_G_3,dam_G_4,dam_K_1,dam_K_2,dam_K_3,dam_K_4,t_sh_1,t_sh_2,t_sh_3,t_sh_4,t_p_1,t_p_2,t_p_3,t_p_4,d_t_sh_1,d_t_sh_2,d_t_sh_3,d_t_sh_4,d_t_p_1,d_t_p_2,d_t_p_3,d_t_p_4,t_sh_dam,t_p_dam,no_stack,tag1,tag2,tag3,tag4,'time_*','$P_{c}/\u03c3_{yy}$',colormap_g,no_ela_file,no_stack,line)
        rheo_plt.param_dam_3D_graph(phi_1,phi_2,phi_3,phi_4,dam_G_1,dam_G_2,dam_G_3,dam_G_4,dam_K_1,dam_K_2,dam_K_3,dam_K_4,t_sh_1,t_sh_2,t_sh_3,t_sh_4,t_p_1,t_p_2,t_p_3,t_p_4,d_t_sh_1,d_t_sh_2,d_t_sh_3,d_t_sh_4,d_t_p_1,d_t_p_2,d_t_p_3,d_t_p_4,t_sh_dam,t_p_dam,no_stack,tag1,tag2,tag3,tag4,'time_*','phi',colormap_g,no_ela_file,no_stack,line)
    # end if
# end if

if need_size == 'yes':
    print("(6/6) Show size variability ? (yes/no)")
    need_graph_size = input()

    if need_graph_size == 'yes' :
        rheo_plt.graph_size(stack_1,stack_2,stack_3,stack_4,E,t_n,d_ave,no_stack,colormap_g)
        rheo_plt.graph_size_var(stack_1,stack_2,stack_3,stack_4,E,t_n,d_ave,no_stack,colormap_g)
    # end if
# end if
# End