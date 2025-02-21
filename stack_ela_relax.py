### !!! The code need to be modify depending of which version of the lammps script your are using !!!
### !!! Line to modify : l.214 / l.217 ; l.271 / l.275 ; l.330 / l.333 ; l.388 / l.392 ; l.427 / l.432

### !!! As this code is made to work on my computer the path for the log.lammps file need to be modified

# Plot the graph from the log.lammps file
# Beginning

import numpy as np
import matplotlib.pyplot as plt
import stack_files as rf
import stack_relax_files as rf_relax
import stack_relax_graph as g_relax

# Save variables
save_variable = 'yes'
grain = '10000'
name_file_relax_t_sh = 't_sh_relax'
name_file_relax_s_sh = 's_sh_relax'
name_file_relax_b_sh = 'beta_sh_relax'
name_file_relax_t_p = 't_p_relax'
name_file_relax_s_p = 's_p_relax'
name_file_relax_b_p = 'beta_p_relax'
name_file_relax_gran = 'gran_sh'

### Problem variable ---------------------------------------------------------- ###

## Scalar variables ----------------------------------------------------------- ##
# dg_dt traitement & colorbar
preparation = 'no_fric' # fric or no_fric
shear_stress = 'deviatoric' # shear or deviatoric
analyse = 'pressure' # analyse (strain or pressure)
stress = 'P_50kPa' # = P_90kPa, P_50kPa, P_5kPa, P_50_90_kPa, P_5_50_90kPa, I_cste or size
damage_comp = 'idealise' # val_0 (take module val at onset of shear) or idealise (take the highest, save ini mod)

zoom = 0 # number of data line to cut in elastic files# Number of stacks used
stack_max = 5 # maximum number of stack
stack = 5 # number of stack use
nb_ela_file = 19 # number of elastic shearing/compression files

if preparation == 'no_fric' and (stress == 'P_5kPa' or stress == 'P_50kPa' or stress == 'P_90kPa') :
    stack_file = f'stacks/strain_pressure/prep_{preparation}/{stress}'
    if stress == 'P_5kPa': press = 'P_5000'
    if stress == 'P_50kPa': press = 'P_50000'
    if stress == 'P_90kPa': press = 'P_90000'
elif preparation == 'fric' and stress == 'P_50kPa' :
    stack_file = f'stacks/strain_pressure/prep_{preparation}/{stress}'
    if stress == 'P_50kPa': press = 'P_50000'
elif stress == 'I_cste' :
    stack_file = f'stacks_read/plot_with_I/{stress}'
    if stress == 'P_50kPa': press = 'P_50000'
elif stress == 'P_50_90_kPa' or stress == 'P_50_90_kPa_I':
    stack_file = f'stacks_read/{stress}'
    press = 'P_50000_90000'
elif stress == 'P_5_50_90_kPa':
    stack_file = f'stacks_read/{stress}'
    press = 'P_5000_50000_90000'
elif preparation == 'fric_1' and stress == 'P_50kPa' :
    preparation = 'fric'
    stack_file = f'stacks_read/prep_{preparation}/{stress}'
    if stress == 'P_50kPa': press = 'P_50000_no_f_f'
elif stress == 'size' :
    stack_file = f'stacks/{stress}'
    press = 'P_50000'
# end if

dg_dt, colormap_g_1, colormap_g_2 = rf.applied_shear(analyse, preparation, stress)

col_ela_cis = 8 # number of column in elastic oscillatory test files
col_ela_comp = 8
col_ela_relax = 10 # number of column in elastic relaxation files
val_relax_col = 14 # number of column in val ela relax
line = 1000
line_ela_comp = 401 # number of line of ela_comp file
line_ela_cis = 401 # number of line of ela_cis file
no_coeff = 4 # fit coefficient

### Needed anaylsis ----------------------------------------------------------- ###
# Output of the program
print('Granulence data extraction ? (yes/no)')
need_gran = input()

# Tag for the graph
if analyse == 'strain': # I(d gamma / dt)
    tag1 = '$I(\.{\gamma})$  = $5 \cdot 10^{-3}$' # tag for stack 1 graph output
    tag2 = '$I(\.{\gamma})$  = $1 \cdot 10^{-3}$' # tag for stack 2 graph output
    tag3 = '$I(\.{\gamma})$  = $5 \cdot 10^{-4}$' # tag for stack 3 graph output
    tag4 = '$I(\.{\gamma})$  = $1 \cdot 10^{-4}$' # tag for stack 4 graph output
    tag5 = '$I(\.{\gamma})$  = $5 \cdot 10^{-5}$' # tag for stack 5 graph output
    tag6 = '$I(\.{\gamma})$  = $5 \cdot 10^{-3}$'
    tag7 = '$I(\.{\gamma})$  = $1 \cdot 10^{-3}$'
    tag8 = '$I(\.{\gamma})$  = $5 \cdot 10^{-4}$'
    tag9 = '$I(\.{\gamma})$  = $1 \cdot 10^{-4}$'
    tag10 = '$I(\.{\gamma})$  = $5 \cdot 10^{-5}$'
elif analyse == 'pressure': # I(S_yy)
    """
    tag1 = '$I(\u03c3_{yy}/ E_{g} = 1 \cdot 10^{-4})$  = $5 \cdot 10^{-3}$' # tag for stack 1 graph output
    tag2 = '$I(\u03c3_{yy}/ E_{g} = 1 \cdot 10^{-4})$  = $5 \cdot 10^{-3}$' # tag for stack 2 graph output
    tag3 = '$I(\u03c3_{yy}/ E_{g} = 1 \cdot 10^{-4})$  = $5 \cdot 10^{-4}$' # tag for stack 3 graph output
    tag4 = '$I(\u03c3_{yy}/ E_{g} = 1 \cdot 10^{-4})$  = $5 \cdot 10^{-4}$' # tag for stack 4 graph output
    tag5 = '$I(\u03c3_{yy}/ E_{g} = 1 \cdot 10^{-4})$  = $5 \cdot 10^{-5}$' # tag for stack 5 graph output
    tag6 = '$I(\u03c3_{yy}/ E_{g} = 1.8 \cdot 10^{-4})$  = $5 \cdot 10^{-3}$'
    tag7 = '$I(\u03c3_{yy}/ E_{g} = 1.8 \cdot 10^{-4})$  = $1 \cdot 10^{-3}$'
    tag8 = '$I(\u03c3_{yy}/ E_{g} = 1.8 \cdot 10^{-4})$  = $5 \cdot 10^{-4}$'
    tag9 = '$I(\u03c3_{yy}/ E_{g} = 1.8 \cdot 10^{-4})$  = $1 \cdot 10^{-4}$'
    tag10 = '$I(\u03c3_{yy}/ E_{g} = 1.8 \cdot 10^{-4})$  = $5 \cdot 10^{-5}$'
    """
    tag1 = '$I(\u03bc_{g} = 0)$  = $5 \cdot 10^{-3}$' # tag for stack 1 graph output
    tag2 = '$I(\u03bc_{g} = 0)$  = $5 \cdot 10^{-3}$' # tag for stack 2 graph output
    tag3 = '$I(\u03bc_{g} = 0)$  = $5 \cdot 10^{-4}$' # tag for stack 3 graph output
    tag4 = '$I(\u03bc_{g} = 0)$  = $5 \cdot 10^{-4}$' # tag for stack 4 graph output
    tag5 = '$I(\u03bc_{g} = 0.7)$  = $5 \cdot 10^{-3}$'
    tag6 = '$I(\u03bc_{g} = 0.7)$  = $1 \cdot 10^{-3}$'
    tag7 = '$I(\u03bc_{g} = 0.7)$  = $5 \cdot 10^{-4}$'
    tag8 = '$I(\u03bc_{g} = 0.7)$  = $1 \cdot 10^{-4}$'
    tag9 = ''
    tag10 = ''
# end if

# Colors of the graphs
colormap_ela = plt.get_cmap('gnuplot')

# Scalar
line = 1000
col_cis = 16

line_ela_relax = 401 # number of line of ela_relax file
col_ela_relax = 14 # number of column in elastic relaxation test files

col_ela_cis = 8 # number of column in elastic oscillatory test files
line_ela_cis = 401 # number of line of ela_cis file

# Adimensional parameters
E_g = 5E8 # material (sea ice) young modulus (Pa)
t_n = 7E-2 # grain normal oscillation time (s)
d_ave = 100 # grain average diameter (m)
rho = 900 # grain density (kg/m^2)

# Vector
beta = np.zeros(stack_max)

# Store the values of data_cis.txt #
val_sh_1 = np.zeros((line,col_cis)) # stack 1
val_sh_2 = np.zeros((line,col_cis)) # stack 2
val_sh_3 = np.zeros((line,col_cis)) # stack 3
val_sh_4 = np.zeros((line,col_cis)) # stack 4
val_sh_5 = np.zeros((line,col_cis)) # stack 5
val_sh_6 = np.zeros((line,col_cis)) # stack 6
val_sh_7 = np.zeros((line,col_cis)) # stack 7
val_sh_8 = np.zeros((line,col_cis)) # stack 8
val_sh_9 = np.zeros((line,col_cis)) # stack 9
val_sh_10 = np.zeros((line,col_cis)) # stack 10

# file 2 (def = 0.25%)
val_ela_relax_1_2 = np.zeros((line_ela_cis,val_relax_col))
val_ela_relax_2_2 = np.zeros((line_ela_cis,val_relax_col))
val_ela_relax_3_2 = np.zeros((line_ela_cis,val_relax_col))
val_ela_relax_4_2 = np.zeros((line_ela_cis,val_relax_col))
val_ela_relax_5_2 = np.zeros((line_ela_cis,val_relax_col))
val_ela_relax_6_2 = np.zeros((line_ela_cis,val_relax_col))
val_ela_relax_7_2 = np.zeros((line_ela_cis,val_relax_col))
val_ela_relax_8_2 = np.zeros((line_ela_cis,val_relax_col))
val_ela_relax_9_2 = np.zeros((line_ela_cis,val_relax_col))
val_ela_relax_10_2 = np.zeros((line_ela_cis,val_relax_col))

# file 6 (def = 5 %)
val_ela_relax_1_6 = np.zeros((line_ela_cis,val_relax_col))
val_ela_relax_2_6 = np.zeros((line_ela_cis,val_relax_col))
val_ela_relax_3_6 = np.zeros((line_ela_cis,val_relax_col))
val_ela_relax_4_6 = np.zeros((line_ela_cis,val_relax_col))
val_ela_relax_5_6 = np.zeros((line_ela_cis,val_relax_col))
val_ela_relax_6_6 = np.zeros((line_ela_cis,val_relax_col))
val_ela_relax_7_6 = np.zeros((line_ela_cis,val_relax_col))
val_ela_relax_8_6 = np.zeros((line_ela_cis,val_relax_col))
val_ela_relax_9_6 = np.zeros((line_ela_cis,val_relax_col))
val_ela_relax_10_6 = np.zeros((line_ela_cis,val_relax_col))

# file 14 (def = 50 %)
val_ela_relax_1_14 = np.zeros((line_ela_cis,val_relax_col))
val_ela_relax_2_14 = np.zeros((line_ela_cis,val_relax_col))
val_ela_relax_3_14 = np.zeros((line_ela_cis,val_relax_col))
val_ela_relax_4_14 = np.zeros((line_ela_cis,val_relax_col))
val_ela_relax_5_14 = np.zeros((line_ela_cis,val_relax_col))
val_ela_relax_6_14 = np.zeros((line_ela_cis,val_relax_col))
val_ela_relax_7_14 = np.zeros((line_ela_cis,val_relax_col))
val_ela_relax_8_14 = np.zeros((line_ela_cis,val_relax_col))
val_ela_relax_9_14 = np.zeros((line_ela_cis,val_relax_col))
val_ela_relax_10_14 = np.zeros((line_ela_cis,val_relax_col))

# file 19 (def = 100 %)
val_ela_relax_1_19 = np.zeros((line_ela_cis,val_relax_col))
val_ela_relax_2_19 = np.zeros((line_ela_cis,val_relax_col))
val_ela_relax_3_19 = np.zeros((line_ela_cis,val_relax_col))
val_ela_relax_4_19 = np.zeros((line_ela_cis,val_relax_col))
val_ela_relax_5_19 = np.zeros((line_ela_cis,val_relax_col))
val_ela_relax_6_19 = np.zeros((line_ela_cis,val_relax_col))
val_ela_relax_7_19 = np.zeros((line_ela_cis,val_relax_col))
val_ela_relax_8_19 = np.zeros((line_ela_cis,val_relax_col))
val_ela_relax_9_19 = np.zeros((line_ela_cis,val_relax_col))
val_ela_relax_10_19 = np.zeros((line_ela_cis,val_relax_col))
# end if

# Store the final value of stress of elastic relaxation (1 stack / col)
plt_ela_relax_1 = np.zeros((nb_ela_file,6))
plt_ela_relax_2 = np.zeros((nb_ela_file,6))
plt_ela_relax_3 = np.zeros((nb_ela_file,6))
plt_ela_relax_4 = np.zeros((nb_ela_file,6))
plt_ela_relax_5 = np.zeros((nb_ela_file,6))
plt_ela_relax_6 = np.zeros((nb_ela_file,6))
plt_ela_relax_7 = np.zeros((nb_ela_file,6))
plt_ela_relax_8 = np.zeros((nb_ela_file,6))
plt_ela_relax_9 = np.zeros((nb_ela_file,6))
plt_ela_relax_10 = np.zeros((nb_ela_file,6))

error_relax_1 = np.zeros((nb_ela_file,6))
error_relax_2 = np.zeros((nb_ela_file,6))
error_relax_3 = np.zeros((nb_ela_file,6))
error_relax_4 = np.zeros((nb_ela_file,6))
error_relax_5 = np.zeros((nb_ela_file,6))
error_relax_6 = np.zeros((nb_ela_file,6))
error_relax_7 = np.zeros((nb_ela_file,6))
error_relax_8 = np.zeros((nb_ela_file,6))
error_relax_9 = np.zeros((nb_ela_file,6))
error_relax_10 = np.zeros((nb_ela_file,6))
# end if

# Exponential fit coefficient & std
coeff_1_sh = np.zeros((nb_ela_file,no_coeff))
coeff_2_sh = np.zeros((nb_ela_file,no_coeff))
coeff_3_sh = np.zeros((nb_ela_file,no_coeff))
coeff_4_sh = np.zeros((nb_ela_file,no_coeff))
coeff_5_sh = np.zeros((nb_ela_file,no_coeff))
coeff_6_sh = np.zeros((nb_ela_file,no_coeff))
coeff_7_sh = np.zeros((nb_ela_file,no_coeff))
coeff_8_sh = np.zeros((nb_ela_file,no_coeff))
coeff_9_sh = np.zeros((nb_ela_file,no_coeff))
coeff_10_sh = np.zeros((nb_ela_file,no_coeff))

coeff_1_p = np.zeros((nb_ela_file,no_coeff))
coeff_2_p = np.zeros((nb_ela_file,no_coeff))
coeff_3_p = np.zeros((nb_ela_file,no_coeff))
coeff_4_p = np.zeros((nb_ela_file,no_coeff))
coeff_5_p = np.zeros((nb_ela_file,no_coeff))
coeff_6_p = np.zeros((nb_ela_file,no_coeff))
coeff_7_p = np.zeros((nb_ela_file,no_coeff))
coeff_8_p = np.zeros((nb_ela_file,no_coeff))
coeff_9_p = np.zeros((nb_ela_file,no_coeff))
coeff_10_p = np.zeros((nb_ela_file,no_coeff))

error_fit_1_sh = np.zeros((nb_ela_file,no_coeff)) # store square error **0.5 of the model (col 1 = sh error / col2 = p error)
error_fit_2_sh = np.zeros((nb_ela_file,no_coeff))
error_fit_3_sh = np.zeros((nb_ela_file,no_coeff))
error_fit_4_sh = np.zeros((nb_ela_file,no_coeff))
error_fit_5_sh = np.zeros((nb_ela_file,no_coeff))
error_fit_6_sh = np.zeros((nb_ela_file,no_coeff))
error_fit_7_sh = np.zeros((nb_ela_file,no_coeff))
error_fit_8_sh = np.zeros((nb_ela_file,no_coeff))
error_fit_9_sh = np.zeros((nb_ela_file,no_coeff))
error_fit_10_sh = np.zeros((nb_ela_file,no_coeff))

error_fit_1_p = np.zeros((nb_ela_file,no_coeff))
error_fit_2_p = np.zeros((nb_ela_file,no_coeff))
error_fit_3_p = np.zeros((nb_ela_file,no_coeff))
error_fit_4_p = np.zeros((nb_ela_file,no_coeff))
error_fit_5_p = np.zeros((nb_ela_file,no_coeff))
error_fit_6_p = np.zeros((nb_ela_file,no_coeff))
error_fit_7_p = np.zeros((nb_ela_file,no_coeff))
error_fit_8_p = np.zeros((nb_ela_file,no_coeff))
error_fit_9_p = np.zeros((nb_ela_file,no_coeff))
error_fit_10_p = np.zeros((nb_ela_file,no_coeff))

# store the elastic shear modulus values
gamma_0 = np.zeros((nb_ela_file,stack_max)) # deformation of restart files
std_gran = np.zeros((nb_ela_file,stack_max))
ly = np.zeros((nb_ela_file,stack_max))

if need_gran == 'yes':
    granulence = np.zeros((nb_ela_file,stack_max)) # granulence at begining of relaxation
# end if

G_ela_1 = np.zeros((nb_ela_file,2))
G_ela_2 = np.zeros((nb_ela_file,2))
G_ela_3 = np.zeros((nb_ela_file,2))
G_ela_4 = np.zeros((nb_ela_file,2))
G_ela_5 = np.zeros((nb_ela_file,2))
G_ela_6 = np.zeros((nb_ela_file,2))
G_ela_7 = np.zeros((nb_ela_file,2))
G_ela_8 = np.zeros((nb_ela_file,2))
G_ela_9 = np.zeros((nb_ela_file,2))
G_ela_10 = np.zeros((nb_ela_file,2))

K_ela_1 = np.zeros((nb_ela_file,2))
K_ela_2 = np.zeros((nb_ela_file,2))
K_ela_3 = np.zeros((nb_ela_file,2))
K_ela_4 = np.zeros((nb_ela_file,2))
K_ela_5 = np.zeros((nb_ela_file,2))
K_ela_6 = np.zeros((nb_ela_file,2))
K_ela_7 = np.zeros((nb_ela_file,2))
K_ela_8 = np.zeros((nb_ela_file,2))
K_ela_9 = np.zeros((nb_ela_file,2))
K_ela_10 = np.zeros((nb_ela_file,2))

G_ela = np.zeros((nb_ela_file,nb_ela_file))
K_ela = np.zeros((nb_ela_file,nb_ela_file))

# store shear modulus damage + std for each stack of simulation
d_G1 = np.zeros((nb_ela_file,2))
d_G2 = np.zeros((nb_ela_file,2))
d_G3 = np.zeros((nb_ela_file,2))
d_G4 = np.zeros((nb_ela_file,2))
d_G5 = np.zeros((nb_ela_file,2))
d_G6 = np.zeros((nb_ela_file,2))
d_G7 = np.zeros((nb_ela_file,2))
d_G8 = np.zeros((nb_ela_file,2))
d_G9 = np.zeros((nb_ela_file,2))
d_G10 = np.zeros((nb_ela_file,2))

# store bulk modulus damage + std for each stack of simulation
d_K1 = np.zeros((nb_ela_file,2))
d_K2 = np.zeros((nb_ela_file,2))
d_K3 = np.zeros((nb_ela_file,2))
d_K4 = np.zeros((nb_ela_file,2))
d_K5 = np.zeros((nb_ela_file,2))
d_K6 = np.zeros((nb_ela_file,2))
d_K7 = np.zeros((nb_ela_file,2))
d_K8 = np.zeros((nb_ela_file,2))
d_K9 = np.zeros((nb_ela_file,2))
d_K10 = np.zeros((nb_ela_file,2))

dG_ela = np.zeros((nb_ela_file,nb_ela_file))
dK_ela = np.zeros((nb_ela_file,nb_ela_file))

# Viscosity and associated uncertainty
# Shear dynamic viscosity
eta_sh = np.zeros((nb_ela_file,col_ela_relax))
d_eta_sh = np.zeros((nb_ela_file,col_ela_relax))

# Volumetric dynamic viscosity
eta_p = np.zeros((nb_ela_file,col_ela_cis))
d_eta_p = np.zeros((nb_ela_file,col_ela_cis))

# Cut the stress overshoot values
fit_cut_eta = np.zeros((nb_ela_file,col_ela_cis))

# Creation of variable to store ela_comp_N.txt/ela_cis_N.txt files values #
G_ela = np.zeros((nb_ela_file,stack_max))
K_ela = np.zeros((nb_ela_file,stack_max))
dG_ela = np.zeros((nb_ela_file,stack_max))
dK_ela = np.zeros((nb_ela_file,stack_max))

dam_G = np.zeros((nb_ela_file,stack_max)) # store the shear modulus damage of all the stacks
dam_G_std = np.zeros((nb_ela_file,stack_max))# store the std of shear modulus damage of all the stacks

dam_K = np.zeros((nb_ela_file,stack_max)) # store the bulk modulus damage of all the stacks
dam_K_std = np.zeros((nb_ela_file,stack_max))# store the std of bulk modulus damage of all the stacks
# end of if

## Extraction of the data file and plot the curves ##
for num_simu in range(1,stack+1): # number of num_simu of simulation
    path = f"/home/rigottia/Nextcloud/Documents/{stack_file}/simu_{num_simu}"

    # Simple shear test data extraction #
    if num_simu == 1 : val_sh_1 = rf.file_data(line,path,num_simu,shear_stress,dg_dt[num_simu-1]) # num_simu 1
    elif num_simu == 2 : val_sh_2 = rf.file_data(line,path,num_simu,shear_stress,dg_dt[num_simu-1]) # num_simu 2
    elif num_simu == 3 : val_sh_3 = rf.file_data(line,path,num_simu,shear_stress,dg_dt[num_simu-1]) # num_simu 3
    elif num_simu == 4 : val_sh_4 = rf.file_data(line,path,num_simu,shear_stress,dg_dt[num_simu-1]) # num_simu 4
    elif num_simu == 5 : val_sh_5 = rf.file_data(line,path,num_simu,shear_stress,dg_dt[num_simu-1]) # num_simu 5
    elif num_simu == 6 : val_sh_6 = rf.file_data(line,path,num_simu,shear_stress,dg_dt[num_simu-1]) # num_simu 6
    elif num_simu == 7 : val_sh_7 = rf.file_data(line,path,num_simu,shear_stress,dg_dt[num_simu-1]) # num_simu 7
    elif num_simu == 8 : val_sh_8 = rf.file_data(line,path,num_simu,shear_stress,dg_dt[num_simu-1]) # num_simu 8
    elif num_simu == 9 : val_sh_9 = rf.file_data(line,path,num_simu,shear_stress,dg_dt[num_simu-1]) # num_simu 9
    elif num_simu == 10 : val_sh_10 = rf.file_data(line,path,num_simu,shear_stress,dg_dt[num_simu-1]) # num_simu 10

    print("\n", "num_simu = ", num_simu, "\n")
    path = f"/home/rigottia/Nextcloud/Documents/{stack_file}/simu_{num_simu}"

    for no_ela_file in range(nb_ela_file): # counter of the no of the ela file
        print("no_ela_file = ", no_ela_file)
        if num_simu == 1 :
            if no_ela_file == 0 :
                val_ela_relax_1_1, ly[no_ela_file,num_simu-1] = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_1_1 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_1_sh[no_ela_file,:], error_fit_1_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_1_p[no_ela_file,:], error_fit_1_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_1[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_1[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 1 :
                val_ela_relax_1_2, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_1_2 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_1_sh[no_ela_file,:], error_fit_1_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_1_p[no_ela_file,:], error_fit_1_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                 # Extract mecanical properties
                G_ela_1[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_1[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 2 :
                val_ela_relax_1_3, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_1_3 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_1_sh[no_ela_file,:], error_fit_1_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_1_p[no_ela_file,:], error_fit_1_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_1[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_1[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 3 :
                val_ela_relax_1_4, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_1_4 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_1_sh[no_ela_file,:], error_fit_1_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_1_p[no_ela_file,:], error_fit_1_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_1[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_1[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 4 :
                val_ela_relax_1_5, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_1_5 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_1_sh[no_ela_file,:], error_fit_1_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_1_p[no_ela_file,:], error_fit_1_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_1[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_1[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 5 :
                val_ela_relax_1_6, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_1_6 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_1_sh[no_ela_file,:], error_fit_1_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_1_p[no_ela_file,:], error_fit_1_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_1[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_1[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 6 :
                val_ela_relax_1_7, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_1_7 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_1_sh[no_ela_file,:], error_fit_1_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_1_p[no_ela_file,:], error_fit_1_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_1[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_1[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 7 :
                val_ela_relax_1_8, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_1_8 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_1_sh[no_ela_file,:], error_fit_1_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_1_p[no_ela_file,:], error_fit_1_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_1[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_1[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 8 :
                val_ela_relax_1_9, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_1_9 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_1_sh[no_ela_file,:], error_fit_1_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_1_p[no_ela_file,:], error_fit_1_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_1[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_1[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 9 :
                val_ela_relax_1_10, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_1_10 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_1_sh[no_ela_file,:], error_fit_1_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_1_p[no_ela_file,:], error_fit_1_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_1[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_1[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 10 :
                val_ela_relax_1_11, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_1_11 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_1_sh[no_ela_file,:], error_fit_1_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_1_p[no_ela_file,:], error_fit_1_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_1[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_1[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 11 :
                val_ela_relax_1_12, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_1_12 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_1_sh[no_ela_file,:], error_fit_1_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_1_p[no_ela_file,:], error_fit_1_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_1[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_1[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 12 :
                val_ela_relax_1_13, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_1_13 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_1_sh[no_ela_file,:], error_fit_1_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_1_p[no_ela_file,:], error_fit_1_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_1[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_1[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 13 :
                val_ela_relax_1_14, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_1_14 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_1_sh[no_ela_file,:], error_fit_1_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_1_p[no_ela_file,:], error_fit_1_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_1[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_1[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 14 :
                val_ela_relax_1_15, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_1_15 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_1_sh[no_ela_file,:], error_fit_1_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_1_p[no_ela_file,:], error_fit_1_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_1[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_1[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 15 :
                val_ela_relax_1_16, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_1_16 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_1_sh[no_ela_file,:], error_fit_1_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_1_p[no_ela_file,:], error_fit_1_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_1[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_1[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 16 :
                val_ela_relax_1_17, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_1_17 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_1_sh[no_ela_file,:], error_fit_1_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_1_p[no_ela_file,:], error_fit_1_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_1[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_1[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 17 :
                val_ela_relax_1_18, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_1_18 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_1_sh[no_ela_file,:], error_fit_1_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_1_p[no_ela_file,:], error_fit_1_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_1[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_1[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 18 :
                val_ela_relax_1_19, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_1_19 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_1_sh[no_ela_file,:], error_fit_1_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_1_p[no_ela_file,:], error_fit_1_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_1[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_1[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

        elif num_simu == 2 :
            if no_ela_file == 0 :
                val_ela_relax_2_1, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_2_1 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_2_sh[no_ela_file,:], error_fit_1_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_2_p[no_ela_file,:], error_fit_1_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_2[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_2[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 1 :
                val_ela_relax_2_2, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_2_2 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_2_sh[no_ela_file,:], error_fit_2_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_2_p[no_ela_file,:], error_fit_2_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_2[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_2[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 2 :
                val_ela_relax_2_3, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_2_3 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_2_sh[no_ela_file,:], error_fit_2_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_2_p[no_ela_file,:], error_fit_2_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_2[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_2[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 3 :
                val_ela_relax_2_4, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_2_4 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_2_sh[no_ela_file,:], error_fit_2_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_2_p[no_ela_file,:], error_fit_2_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_2[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_2[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 4 :
                val_ela_relax_2_5, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_2_5 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_2_sh[no_ela_file,:], error_fit_2_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_2_p[no_ela_file,:], error_fit_2_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_2[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_2[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 5 :
                val_ela_relax_2_6, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_2_6 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_2_sh[no_ela_file,:], error_fit_2_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_2_p[no_ela_file,:], error_fit_2_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_2[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_2[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 6 :
                val_ela_relax_2_7, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_2_7 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_2_sh[no_ela_file,:], error_fit_2_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_2_p[no_ela_file,:], error_fit_2_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_2[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_2[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 7 :
                val_ela_relax_2_8, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_2_8 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_2_sh[no_ela_file,:], error_fit_2_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_2_p[no_ela_file,:], error_fit_2_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_2[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_2[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 8 :
                val_ela_relax_2_9, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_2_9 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_2_sh[no_ela_file,:], error_fit_2_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_2_p[no_ela_file,:], error_fit_2_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_2[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_2[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 9 :
                val_ela_relax_2_10, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_2_10 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_2_sh[no_ela_file,:], error_fit_2_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_2_p[no_ela_file,:], error_fit_2_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_2[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_2[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 10 :
                val_ela_relax_2_11, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_2_11 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_2_sh[no_ela_file,:], error_fit_2_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_2_p[no_ela_file,:], error_fit_2_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_2[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_2[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 11 :
                val_ela_relax_2_12, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_2_12 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_2_sh[no_ela_file,:], error_fit_2_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_2_p[no_ela_file,:], error_fit_2_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_2[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_2[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 12 :
                val_ela_relax_2_13, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_2_13 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_2_sh[no_ela_file,:], error_fit_1_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_2_p[no_ela_file,:], error_fit_1_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_2[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_2[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 13 :
                val_ela_relax_2_14, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_2_14 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_2_sh[no_ela_file,:], error_fit_2_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_2_p[no_ela_file,:], error_fit_2_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_2[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_2[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 14 :
                val_ela_relax_2_15, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_2_15 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_2_sh[no_ela_file,:], error_fit_2_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_2_p[no_ela_file,:], error_fit_2_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_2[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_2[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 15 :
                val_ela_relax_2_16, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_2_16 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_2_sh[no_ela_file,:], error_fit_2_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_2_p[no_ela_file,:], error_fit_2_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_2[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_2[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 16 :
                val_ela_relax_2_17, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_2_17 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_2_sh[no_ela_file,:], error_fit_2_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_2_p[no_ela_file,:], error_fit_2_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_2[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_2[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 17 :
                val_ela_relax_2_18, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_2_18 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_2_sh[no_ela_file,:], error_fit_2_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_2_p[no_ela_file,:], error_fit_2_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_2[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_2[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 18 :
                val_ela_relax_2_19, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_2_19 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_2_sh[no_ela_file,:], error_fit_2_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_2_p[no_ela_file,:], error_fit_2_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

               # Extract mecanical properties
                G_ela_2[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_2[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

        elif num_simu == 3 :
            if no_ela_file == 0 :
                val_ela_relax_3_1, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_3_1 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_3_sh[no_ela_file,:], error_fit_3_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_3_p[no_ela_file,:], error_fit_3_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_3[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_3[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 1 :
                val_ela_relax_3_2, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_3_2 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_3_sh[no_ela_file,:], error_fit_3_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_3_p[no_ela_file,:], error_fit_3_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_3[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_3[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 2 :
                val_ela_relax_3_3, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_3_3 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_3_sh[no_ela_file,:], error_fit_3_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_3_p[no_ela_file,:], error_fit_3_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_3[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_3[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 3 :
                val_ela_relax_3_4, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_3_4 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_3_sh[no_ela_file,:], error_fit_3_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_3_p[no_ela_file,:], error_fit_3_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                #Extract viscosity
                G_ela_3[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_3[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 4 :
                val_ela_relax_3_5, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_3_5 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_3_sh[no_ela_file,:], error_fit_3_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_3_p[no_ela_file,:], error_fit_3_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_3[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_3[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 5 :
                val_ela_relax_3_6, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_3_6 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_3_sh[no_ela_file,:], error_fit_3_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_3_p[no_ela_file,:], error_fit_3_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_3[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_3[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 6 :
                val_ela_relax_3_7, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_3_7 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_3_sh[no_ela_file,:], error_fit_3_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_3_p[no_ela_file,:], error_fit_3_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_3[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_3[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 7 :
                val_ela_relax_3_8, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_3_8 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_3_sh[no_ela_file,:], error_fit_3_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_3_p[no_ela_file,:], error_fit_3_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_3[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_3[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 8 :
                val_ela_relax_3_9, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_3_9 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_3_sh[no_ela_file,:], error_fit_3_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_3_p[no_ela_file,:], error_fit_3_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_3[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_3[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 9 :
                val_ela_relax_3_10, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_3_10 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_3_sh[no_ela_file,:], error_fit_3_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_3_p[no_ela_file,:], error_fit_3_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_3[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_3[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 10 :
                val_ela_relax_3_11, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_3_11 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_3_sh[no_ela_file,:], error_fit_3_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_3_p[no_ela_file,:], error_fit_3_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_3[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_3[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 11 :
                val_ela_relax_3_12, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_3_12 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_3_sh[no_ela_file,:], error_fit_3_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_3_p[no_ela_file,:], error_fit_3_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_3[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_3[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 12 :
                val_ela_relax_3_13, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_3_13 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_3_sh[no_ela_file,:], error_fit_3_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_3_p[no_ela_file,:], error_fit_3_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_3[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_3[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 13 :
                val_ela_relax_3_14, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_3_14 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_3_sh[no_ela_file,:], error_fit_3_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_3_p[no_ela_file,:], error_fit_3_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_3[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_3[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 14 :
                val_ela_relax_3_15, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_3_15 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_3_sh[no_ela_file,:], error_fit_3_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_3_p[no_ela_file,:], error_fit_3_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_3[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_3[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 15 :
                val_ela_relax_3_16, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_3_16 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_3_sh[no_ela_file,:], error_fit_3_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_3_p[no_ela_file,:], error_fit_3_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_3[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_3[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 16 :
                val_ela_relax_3_17, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_3_17 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_3_sh[no_ela_file,:], error_fit_3_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_3_p[no_ela_file,:], error_fit_3_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_3[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_3[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 17 :
                val_ela_relax_3_18, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_3_18 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_3_sh[no_ela_file,:], error_fit_3_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_3_p[no_ela_file,:], error_fit_3_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_3[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_3[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 18 :
                val_ela_relax_3_19, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_3_19 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_3_sh[no_ela_file,:], error_fit_3_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_3_p[no_ela_file,:], error_fit_3_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_3[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_3[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

        elif num_simu == 4 :
            if no_ela_file == 0 :
                val_ela_relax_4_1, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_4_1 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_4_sh[no_ela_file,:], error_fit_4_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_4_p[no_ela_file,:], error_fit_4_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_4[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_4[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 1 :
                val_ela_relax_4_2, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_4_2 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_4_sh[no_ela_file,:], error_fit_4_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_4_p[no_ela_file,:], error_fit_4_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_4[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_4[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 2 :
                val_ela_relax_4_3, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_4_3 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_4_sh[no_ela_file,:], error_fit_4_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_4_p[no_ela_file,:], error_fit_4_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_4[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_4[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 3 :
                val_ela_relax_4_4, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_4_4 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_4_sh[no_ela_file,:], error_fit_4_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_4_p[no_ela_file,:], error_fit_4_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_4[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_4[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 4 :
                val_ela_relax_4_5, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_4_5 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_4_sh[no_ela_file,:], error_fit_4_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_4_p[no_ela_file,:], error_fit_4_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_4[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_4[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 5 :
                val_ela_relax_4_6, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_4_6 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_4_sh[no_ela_file,:], error_fit_4_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_4_p[no_ela_file,:], error_fit_4_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_4[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_4[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 6 :
                val_ela_relax_4_7, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_4_7 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_4_sh[no_ela_file,:], error_fit_4_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_4_p[no_ela_file,:], error_fit_4_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_4[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_4[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 7 :
                val_ela_relax_4_8, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_4_8 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_4_sh[no_ela_file,:], error_fit_4_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_4_p[no_ela_file,:], error_fit_4_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_4[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_4[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 8 :
                val_ela_relax_4_9, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_4_9 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_4_sh[no_ela_file,:], error_fit_4_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_4_p[no_ela_file,:], error_fit_4_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_4[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_4[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 9 :
                val_ela_relax_4_10, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_4_10 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_4_sh[no_ela_file,:], error_fit_4_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_4_p[no_ela_file,:], error_fit_4_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_4[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_4[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 10 :
                val_ela_relax_4_11, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_4_11 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_4_sh[no_ela_file,:], error_fit_4_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_4_p[no_ela_file,:], error_fit_4_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_4[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_4[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 11 :
                val_ela_relax_4_12, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_4_12 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_4_sh[no_ela_file,:], error_fit_4_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_4_p[no_ela_file,:], error_fit_4_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_4[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_4[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 12 :
                val_ela_relax_4_13, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_4_13 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_4_sh[no_ela_file,:], error_fit_4_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_4_p[no_ela_file,:], error_fit_4_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_4[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_4[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 13 :
                val_ela_relax_4_14, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_4_14 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_4_sh[no_ela_file,:], error_fit_4_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_4_p[no_ela_file,:], error_fit_4_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_4[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_4[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 14 :
                val_ela_relax_4_15, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_4_15 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_4_sh[no_ela_file,:], error_fit_4_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_4_p[no_ela_file,:], error_fit_4_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_4[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] =rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_4[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 15 :
                val_ela_relax_4_16, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_4_16 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_4_sh[no_ela_file,:], error_fit_4_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_4_p[no_ela_file,:], error_fit_4_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_4[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_4[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 16 :
                val_ela_relax_4_17, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_4_17 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_4_sh[no_ela_file,:], error_fit_4_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_4_p[no_ela_file,:], error_fit_4_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_4[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_4[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 17 :
                val_ela_relax_4_18, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_4_18 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_4_sh[no_ela_file,:], error_fit_4_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_4_p[no_ela_file,:], error_fit_4_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_4[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_4[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 18 :
                val_ela_relax_4_19, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_4_19 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_4_sh[no_ela_file,:], error_fit_4_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_4_p[no_ela_file,:], error_fit_4_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_4[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_4[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

        elif num_simu == 5 :
            if no_ela_file == 0 :
                val_ela_relax_5_1, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_5_1 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_5_sh[no_ela_file,:], error_fit_5_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_5_p[no_ela_file,:], error_fit_5_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_5[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_5[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 1 :
                val_ela_relax_5_2, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_5_2 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_5_sh[no_ela_file,:], error_fit_5_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_5_p[no_ela_file,:], error_fit_5_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_5[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_5[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 2 :
                val_ela_relax_5_3, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_5_3 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_5_sh[no_ela_file,:], error_fit_5_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_5_p[no_ela_file,:], error_fit_5_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_5[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_5[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 3 :
                val_ela_relax_5_4, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_5_4 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_5_sh[no_ela_file,:], error_fit_5_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_5_p[no_ela_file,:], error_fit_5_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_5[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_5[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 4 :
                val_ela_relax_5_5, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_5_5 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_5_sh[no_ela_file,:], error_fit_5_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_5_p[no_ela_file,:], error_fit_5_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_5[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_5[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 5 :
                val_ela_relax_5_6, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_5_6 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_5_sh[no_ela_file,:], error_fit_5_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_5_p[no_ela_file,:], error_fit_5_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_5[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_5[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 6 :
                val_ela_relax_5_7, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_5_7 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_5_sh[no_ela_file,:], error_fit_5_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_5_p[no_ela_file,:], error_fit_5_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_5[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_5[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 7 :
                val_ela_relax_5_8, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_5_8 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_5_sh[no_ela_file,:], error_fit_5_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_5_p[no_ela_file,:], error_fit_5_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_5[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_5[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 8 :
                val_ela_relax_5_9, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_5_9 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_5_sh[no_ela_file,:], error_fit_5_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_5_p[no_ela_file,:], error_fit_5_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_5[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_5[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 9 :
                val_ela_relax_5_10, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_5_10 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_5_sh[no_ela_file,:], error_fit_5_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_5_p[no_ela_file,:], error_fit_5_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_5[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_5[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 10 :
                val_ela_relax_5_11, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_5_11 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_5_sh[no_ela_file,:], error_fit_5_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_5_p[no_ela_file,:], error_fit_5_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_5[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_5[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 11 :
                val_ela_relax_5_12, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_5_12 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_5_sh[no_ela_file,:], error_fit_5_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_5_p[no_ela_file,:], error_fit_5_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_5[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_5[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 12 :
                val_ela_relax_5_13, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_5_13 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_5_sh[no_ela_file,:], error_fit_5_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_5_p[no_ela_file,:], error_fit_5_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_5[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_5[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 13 :
                val_ela_relax_5_14, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_5_14 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_5_sh[no_ela_file,:], error_fit_5_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_5_p[no_ela_file,:], error_fit_5_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_5[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_5[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 14 :
                val_ela_relax_5_15, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_5_15 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_5_sh[no_ela_file,:], error_fit_5_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_5_p[no_ela_file,:], error_fit_5_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_5[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_5[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 15 :
                val_ela_relax_5_16, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_5_16 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_5_sh[no_ela_file,:], error_fit_5_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_5_p[no_ela_file,:], error_fit_5_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_5[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_5[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 16 :
                val_ela_relax_5_17, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_5_17 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_5_sh[no_ela_file,:], error_fit_5_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_5_p[no_ela_file,:], error_fit_5_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_5[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_5[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 17 :
                val_ela_relax_5_18, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_5_18 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_5_sh[no_ela_file,:], error_fit_5_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_5_p[no_ela_file,:], error_fit_5_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_5[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_5[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 18 :
                val_ela_relax_5_19, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_5_19 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_5_sh[no_ela_file,:], error_fit_5_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_5_p[no_ela_file,:], error_fit_5_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_5[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_5[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

        elif num_simu == 6 :
            if no_ela_file == 0 :
                val_ela_relax_6_1, ly[no_ela_file,num_simu-1] = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_6_1 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_6_sh[no_ela_file,:], error_fit_6_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_6_p[no_ela_file,:], error_fit_6_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_6[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_6[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 1 :
                val_ela_relax_6_2, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_6_2 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_6_sh[no_ela_file,:], error_fit_6_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_6_p[no_ela_file,:], error_fit_6_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                 # Extract mecanical properties
                G_ela_6[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_6[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 2 :
                val_ela_relax_6_3, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_6_3 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_6_sh[no_ela_file,:], error_fit_6_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_6_p[no_ela_file,:], error_fit_6_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_6[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_6[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 3 :
                val_ela_relax_6_4, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_6_4 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_6_sh[no_ela_file,:], error_fit_6_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_6_p[no_ela_file,:], error_fit_6_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_6[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_6[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 4 :
                val_ela_relax_6_5, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_6_5 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_6_sh[no_ela_file,:], error_fit_6_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_6_p[no_ela_file,:], error_fit_6_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_6[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_6[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 5 :
                val_ela_relax_6_6, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_6_6 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_6_sh[no_ela_file,:], error_fit_6_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_6_p[no_ela_file,:], error_fit_6_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_6[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_6[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 6 :
                val_ela_relax_6_7, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_6_7 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_6_sh[no_ela_file,:], error_fit_6_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_6_p[no_ela_file,:], error_fit_6_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_6[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_6[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 7 :
                val_ela_relax_6_8, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_6_8 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_6_sh[no_ela_file,:], error_fit_6_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_6_p[no_ela_file,:], error_fit_6_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_6[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_6[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 8 :
                val_ela_relax_6_9, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_6_9 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_6_sh[no_ela_file,:], error_fit_6_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_6_p[no_ela_file,:], error_fit_6_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_6[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_6[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 9 :
                val_ela_relax_6_10, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_6_10 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_6_sh[no_ela_file,:], error_fit_6_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_6_p[no_ela_file,:], error_fit_6_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_6[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_6[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 10 :
                val_ela_relax_6_11, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_6_11 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_6_sh[no_ela_file,:], error_fit_6_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_6_p[no_ela_file,:], error_fit_6_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_6[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_6[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 11 :
                val_ela_relax_6_12, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_6_12 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_6_sh[no_ela_file,:], error_fit_6_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_6_p[no_ela_file,:], error_fit_6_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_6[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_6[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 12 :
                val_ela_relax_6_13, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_6_13 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_6_sh[no_ela_file,:], error_fit_6_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_6_p[no_ela_file,:], error_fit_6_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_6[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_6[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 13 :
                val_ela_relax_6_14, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_6_14 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_6_sh[no_ela_file,:], error_fit_6_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_6_p[no_ela_file,:], error_fit_6_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_6[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_6[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 14 :
                val_ela_relax_6_15, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_6_15 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_6_sh[no_ela_file,:], error_fit_6_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_6_p[no_ela_file,:], error_fit_6_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_6[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_6[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 15 :
                val_ela_relax_6_16, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_6_16 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_6_sh[no_ela_file,:], error_fit_6_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_6_p[no_ela_file,:], error_fit_6_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_6[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_6[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 16 :
                val_ela_relax_6_17, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_6_17 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_6_sh[no_ela_file,:], error_fit_6_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_6_p[no_ela_file,:], error_fit_6_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_6[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_6[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 17 :
                val_ela_relax_6_18, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_6_18 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_6_sh[no_ela_file,:], error_fit_6_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_6_p[no_ela_file,:], error_fit_6_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_6[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_6[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 18 :
                val_ela_relax_6_19, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_6_19 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_6_sh[no_ela_file,:], error_fit_6_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_6_p[no_ela_file,:], error_fit_6_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_6[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_6[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

        elif num_simu == 7 :
            if no_ela_file == 0 :
                val_ela_relax_7_1, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_7_1 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_7_sh[no_ela_file,:], error_fit_7_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_7_p[no_ela_file,:], error_fit_7_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_7[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_7[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 1 :
                val_ela_relax_7_2, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_7_2 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_7_sh[no_ela_file,:], error_fit_7_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_7_p[no_ela_file,:], error_fit_7_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_7[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_7[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 2 :
                val_ela_relax_7_3, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_7_3 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_7_sh[no_ela_file,:], error_fit_7_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_7_p[no_ela_file,:], error_fit_7_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_7[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_7[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 3 :
                val_ela_relax_7_4, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_7_4 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_7_sh[no_ela_file,:], error_fit_7_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_7_p[no_ela_file,:], error_fit_7_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_7[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_7[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 4 :
                val_ela_relax_7_5, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_7_5 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_7_sh[no_ela_file,:], error_fit_7_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_7_p[no_ela_file,:], error_fit_7_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_7[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_7[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 5 :
                val_ela_relax_7_6, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_7_6 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_7_sh[no_ela_file,:], error_fit_7_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_7_p[no_ela_file,:], error_fit_7_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_7[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_7[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 6 :
                val_ela_relax_7_7, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_7_7 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_7_sh[no_ela_file,:], error_fit_7_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_7_p[no_ela_file,:], error_fit_7_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_7[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_7[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 7 :
                val_ela_relax_7_8, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_7_8 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_7_sh[no_ela_file,:], error_fit_7_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_7_p[no_ela_file,:], error_fit_7_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_7[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_7[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 8 :
                val_ela_relax_7_9, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_7_9 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_7_sh[no_ela_file,:], error_fit_7_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_7_p[no_ela_file,:], error_fit_7_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_7[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_7[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 9 :
                val_ela_relax_7_10, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_7_10 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_7_sh[no_ela_file,:], error_fit_7_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_7_p[no_ela_file,:], error_fit_7_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_7[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_7[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 10 :
                val_ela_relax_7_11, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_7_11 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_7_sh[no_ela_file,:], error_fit_7_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_7_p[no_ela_file,:], error_fit_7_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_7[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_7[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 11 :
                val_ela_relax_7_12, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_7_12 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_7_sh[no_ela_file,:], error_fit_7_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_7_p[no_ela_file,:], error_fit_7_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_7[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_7[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 12 :
                val_ela_relax_7_13, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_7_13 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_7_sh[no_ela_file,:], error_fit_7_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_7_p[no_ela_file,:], error_fit_7_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_7[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_7[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 13 :
                val_ela_relax_7_14, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_7_14 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_7_sh[no_ela_file,:], error_fit_7_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_7_p[no_ela_file,:], error_fit_7_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_7[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_7[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 14 :
                val_ela_relax_7_15, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_7_15 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_7_sh[no_ela_file,:], error_fit_7_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_7_p[no_ela_file,:], error_fit_7_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_7[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_7[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 15 :
                val_ela_relax_7_16, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_7_16 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_7_sh[no_ela_file,:], error_fit_7_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_7_p[no_ela_file,:], error_fit_7_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_7[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_7[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 16 :
                val_ela_relax_7_17, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_7_17 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_7_sh[no_ela_file,:], error_fit_7_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_7_p[no_ela_file,:], error_fit_7_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_7[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_7[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 17 :
                val_ela_relax_7_18, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_7_18 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_7_sh[no_ela_file,:], error_fit_7_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_7_p[no_ela_file,:], error_fit_7_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_7[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_7[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 18 :
                val_ela_relax_7_19, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_7_19 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_7_sh[no_ela_file,:], error_fit_7_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_7_p[no_ela_file,:], error_fit_7_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

               # Extract mecanical properties
                G_ela_7[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_7[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

        elif num_simu == 8 :
            if no_ela_file == 0 :
                val_ela_relax_8_1, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_8_1 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_8_sh[no_ela_file,:], error_fit_8_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_8_p[no_ela_file,:], error_fit_8_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_8[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_8[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 1 :
                val_ela_relax_8_2, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_8_2 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_8_sh[no_ela_file,:], error_fit_8_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_8_p[no_ela_file,:], error_fit_8_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_8[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_8[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 2 :
                val_ela_relax_8_3, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_8_3 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_8_sh[no_ela_file,:], error_fit_8_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_8_p[no_ela_file,:], error_fit_8_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_8[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_8[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 3 :
                val_ela_relax_8_4, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_8_4 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_8_sh[no_ela_file,:], error_fit_8_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_8_p[no_ela_file,:], error_fit_8_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                #Extract viscosity
                G_ela_8[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_8[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 4 :
                val_ela_relax_8_5, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_8_5 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_8_sh[no_ela_file,:], error_fit_8_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_8_p[no_ela_file,:], error_fit_8_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_8[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_8[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 5 :
                val_ela_relax_8_6, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_8_6 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_8_sh[no_ela_file,:], error_fit_8_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_8_p[no_ela_file,:], error_fit_8_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_8[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_8[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 6 :
                val_ela_relax_8_7, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_8_7 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_8_sh[no_ela_file,:], error_fit_8_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_8_p[no_ela_file,:], error_fit_8_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_8[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_8[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 7 :
                val_ela_relax_8_8, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_8_8 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_8_sh[no_ela_file,:], error_fit_8_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_8_p[no_ela_file,:], error_fit_8_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_8[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_8[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 8 :
                val_ela_relax_8_9, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_8_9 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_8_sh[no_ela_file,:], error_fit_8_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_8_p[no_ela_file,:], error_fit_8_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_8[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_8[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 9 :
                val_ela_relax_8_10, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_8_10 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_8_sh[no_ela_file,:], error_fit_8_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_8_p[no_ela_file,:], error_fit_8_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_8[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_8[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 10 :
                val_ela_relax_8_11, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_8_11 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_8_sh[no_ela_file,:], error_fit_8_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_8_p[no_ela_file,:], error_fit_8_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_8[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_8[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 11 :
                val_ela_relax_8_12, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_8_12 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_8_sh[no_ela_file,:], error_fit_8_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_8_p[no_ela_file,:], error_fit_8_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_8[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_8[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 12 :
                val_ela_relax_8_13, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_8_13 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_8_sh[no_ela_file,:], error_fit_8_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_8_p[no_ela_file,:], error_fit_8_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_8[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_8[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 13 :
                val_ela_relax_8_14, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_8_14 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_8_sh[no_ela_file,:], error_fit_8_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_8_p[no_ela_file,:], error_fit_8_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_8[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_8[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 14 :
                val_ela_relax_8_15, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_8_15 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_8_sh[no_ela_file,:], error_fit_8_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_8_p[no_ela_file,:], error_fit_8_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_8[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_8[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 15 :
                val_ela_relax_8_16, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_8_16 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_8_sh[no_ela_file,:], error_fit_8_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_8_p[no_ela_file,:], error_fit_8_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_8[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_8[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 16 :
                val_ela_relax_8_17, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_8_17 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_8_sh[no_ela_file,:], error_fit_8_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_8_p[no_ela_file,:], error_fit_8_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_8[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_8[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 17 :
                val_ela_relax_8_18, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_8_18 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_8_sh[no_ela_file,:], error_fit_8_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_8_p[no_ela_file,:], error_fit_8_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_8[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_8[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 18 :
                val_ela_relax_8_19, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_8_19 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_8_sh[no_ela_file,:], error_fit_8_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_8_p[no_ela_file,:], error_fit_8_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_8[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_8[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

        elif num_simu == 9 :
            if no_ela_file == 0 :
                val_ela_relax_9_1, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_9_1 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_9_sh[no_ela_file,:], error_fit_9_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_9_p[no_ela_file,:], error_fit_9_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_9[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_9[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 1 :
                val_ela_relax_9_2, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_9_2 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_9_sh[no_ela_file,:], error_fit_9_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_9_p[no_ela_file,:], error_fit_9_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_9[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_9[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 2 :
                val_ela_relax_9_3, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_9_3 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_9_sh[no_ela_file,:], error_fit_9_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_9_p[no_ela_file,:], error_fit_9_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_9[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_9[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 3 :
                val_ela_relax_9_4, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_9_4 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_9_sh[no_ela_file,:], error_fit_9_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_9_p[no_ela_file,:], error_fit_9_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_9[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_9[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 4 :
                val_ela_relax_9_5, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_9_5 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_9_sh[no_ela_file,:], error_fit_9_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_9_p[no_ela_file,:], error_fit_9_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_9[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_9[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 5 :
                val_ela_relax_9_6, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_9_6 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_9_sh[no_ela_file,:], error_fit_9_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_9_p[no_ela_file,:], error_fit_9_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_9[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_9[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 6 :
                val_ela_relax_9_7, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_9_7 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_9_sh[no_ela_file,:], error_fit_9_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_9_p[no_ela_file,:], error_fit_9_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_9[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_9[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 7 :
                val_ela_relax_9_8, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_9_8 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_9_sh[no_ela_file,:], error_fit_9_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_9_p[no_ela_file,:], error_fit_9_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_9[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_9[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 8 :
                val_ela_relax_9_9, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_9_9 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_9_sh[no_ela_file,:], error_fit_9_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_9_p[no_ela_file,:], error_fit_9_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_9[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_9[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 9 :
                val_ela_relax_9_10, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_9_10 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_9_sh[no_ela_file,:], error_fit_9_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_9_p[no_ela_file,:], error_fit_9_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_9[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_9[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 10 :
                val_ela_relax_9_11, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_9_11 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_9_sh[no_ela_file,:], error_fit_9_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_9_p[no_ela_file,:], error_fit_9_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_9[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_9[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 11 :
                val_ela_relax_9_12, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_9_12 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_9_sh[no_ela_file,:], error_fit_9_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_9_p[no_ela_file,:], error_fit_9_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_9[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_9[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 12 :
                val_ela_relax_9_13, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_9_13 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_9_sh[no_ela_file,:], error_fit_9_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_9_p[no_ela_file,:], error_fit_9_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_9[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_9[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 13 :
                val_ela_relax_9_14, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_9_14 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_9_sh[no_ela_file,:], error_fit_9_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_9_p[no_ela_file,:], error_fit_9_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_9[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_9[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 14 :
                val_ela_relax_9_15, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_9_15 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_9_sh[no_ela_file,:], error_fit_9_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_9_p[no_ela_file,:], error_fit_9_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_9[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] =rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_9[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 15 :
                val_ela_relax_9_16, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_9_16 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_9_sh[no_ela_file,:], error_fit_9_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_9_p[no_ela_file,:], error_fit_9_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_9[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_9[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 16 :
                val_ela_relax_9_17, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_9_17 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_9_sh[no_ela_file,:], error_fit_9_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_9_p[no_ela_file,:], error_fit_9_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_9[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_9[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 17 :
                val_ela_relax_9_18, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_9_18 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_9_sh[no_ela_file,:], error_fit_9_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_9_p[no_ela_file,:], error_fit_9_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_9[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_9[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 18 :
                val_ela_relax_9_19, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_9_19 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_9_sh[no_ela_file,:], error_fit_9_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_9_p[no_ela_file,:], error_fit_9_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_9[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_9[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

        elif num_simu == 10 :
            if no_ela_file == 0 :
                val_ela_relax_10_1, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_10_1 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_10_sh[no_ela_file,:], error_fit_10_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_10_p[no_ela_file,:], error_fit_10_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_10[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_10[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 1 :
                val_ela_relax_10_2, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_10_2 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_10_sh[no_ela_file,:], error_fit_10_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_10_p[no_ela_file,:], error_fit_10_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_10[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_10[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 2 :
                val_ela_relax_10_3, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_10_3 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_10_sh[no_ela_file,:], error_fit_10_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_10_p[no_ela_file,:], error_fit_10_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_10[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_10[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 3 :
                val_ela_relax_10_4, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_10_4 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_10_sh[no_ela_file,:], error_fit_10_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_10_p[no_ela_file,:], error_fit_10_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_10[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_10[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 4 :
                val_ela_relax_10_5, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_10_5 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_10_sh[no_ela_file,:], error_fit_10_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_10_p[no_ela_file,:], error_fit_10_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_10[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_10[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 5 :
                val_ela_relax_10_6, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_10_6 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_10_sh[no_ela_file,:], error_fit_10_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_10_p[no_ela_file,:], error_fit_10_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_10[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_10[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 6 :
                val_ela_relax_10_7, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_10_7 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_10_sh[no_ela_file,:], error_fit_10_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_10_p[no_ela_file,:], error_fit_10_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_10[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_10[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 7 :
                val_ela_relax_10_8, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_10_8 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_10_sh[no_ela_file,:], error_fit_10_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_10_p[no_ela_file,:], error_fit_10_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_10[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_10[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 8 :
                val_ela_relax_10_9, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_10_9 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_10_sh[no_ela_file,:], error_fit_10_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_10_p[no_ela_file,:], error_fit_10_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_10[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_10[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 9 :
                val_ela_relax_10_10, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_10_10 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_10_sh[no_ela_file,:], error_fit_10_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_10_p[no_ela_file,:], error_fit_10_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_10[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_10[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 10 :
                val_ela_relax_10_11, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_10_11 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_10_sh[no_ela_file,:], error_fit_10_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_10_p[no_ela_file,:], error_fit_10_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_10[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_10[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 11 :
                val_ela_relax_10_12, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_10_12 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_10_sh[no_ela_file,:], error_fit_10_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_10_p[no_ela_file,:], error_fit_10_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_10[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_10[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 12 :
                val_ela_relax_10_13, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_10_13 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_10_sh[no_ela_file,:], error_fit_10_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_10_p[no_ela_file,:], error_fit_10_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_10[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_10[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 13 :
                val_ela_relax_10_14, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_10_14 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_10_sh[no_ela_file,:], error_fit_10_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_10_p[no_ela_file,:], error_fit_10_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_10[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_10[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 14 :
                val_ela_relax_10_15, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_10_15 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_10_sh[no_ela_file,:], error_fit_10_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_10_p[no_ela_file,:], error_fit_10_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_10[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_10[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 15 :
                val_ela_relax_10_16, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_10_16 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_10_sh[no_ela_file,:], error_fit_10_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_10_p[no_ela_file,:], error_fit_10_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_10[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_10[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 16 :
                val_ela_relax_10_17, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_10_17 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_10_sh[no_ela_file,:], error_fit_10_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_10_p[no_ela_file,:], error_fit_10_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_10[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_10[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 17 :
                val_ela_relax_10_18, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_10_18 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_10_sh[no_ela_file,:], error_fit_10_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_10_p[no_ela_file,:], error_fit_10_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_10[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_10[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)

            elif no_ela_file == 18 :
                val_ela_relax_10_19, ly[no_ela_file,num_simu-1]  = rf_relax.file_ela_relax_data(no_ela_file+1,line_ela_relax,shear_stress,path)
                if need_gran == 'yes' : granulence_10_19 = rf_relax.file_granulence_data(no_ela_file+1, path)

                # Extract relaxation properties
                coeff_10_sh[no_ela_file,:], error_fit_10_sh[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, shear_stress,num_simu)
                coeff_10_p[no_ela_file,:], error_fit_10_p[no_ela_file,:] = rf_relax.file_ela_relax_param(no_ela_file+1, line_ela_relax, path, 'pressure',num_simu)

                # Extract mecanical properties
                G_ela_10[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)
                K_ela_10[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
    # end of j for loop

    G_ela = rf_relax.ela_matrix(G_ela_1, G_ela_2, G_ela_3, G_ela_4, G_ela_5, G_ela_6, G_ela_7, G_ela_8, G_ela_9, G_ela_10, E_g, nb_ela_file,'elastic modulus',stack_max)
    K_ela = rf_relax.ela_matrix(K_ela_1, K_ela_2, K_ela_3, K_ela_4, K_ela_5, K_ela_6, K_ela_7, K_ela_8, K_ela_9, K_ela_10, E_g, nb_ela_file,'elastic modulus',stack_max)
    dG_ela = rf_relax.ela_matrix(G_ela_1, G_ela_2, G_ela_3, G_ela_4, G_ela_5, G_ela_6, G_ela_7, G_ela_8, G_ela_9, G_ela_10, E_g, nb_ela_file,'std',stack_max)
    dK_ela = rf_relax.ela_matrix(K_ela_1, K_ela_2, K_ela_3, K_ela_4, K_ela_5, K_ela_6, K_ela_7, K_ela_8, K_ela_9, K_ela_10, E_g, nb_ela_file,'std',stack_max)

    if num_simu == 1 : # stack 1
        d_G1 =  rf.d_comp(nb_ela_file, line_ela_cis, path, press, analyse, 'shear', num_simu, stack_max, zoom, damage_comp)
        d_K1 =  rf.d_comp(nb_ela_file, line_ela_cis, path, press, analyse, 'bulk', num_simu, stack_max, zoom, damage_comp)

    elif num_simu == 2 : # stack 2
        d_G2 =  rf.d_comp(nb_ela_file, line_ela_cis, path, press, analyse, 'shear', num_simu, stack_max, zoom, damage_comp)
        d_K2 =  rf.d_comp(nb_ela_file, line_ela_cis, path, press, analyse, 'bulk', num_simu, stack_max, zoom, damage_comp)

    elif num_simu == 3 : # stack 3
        d_G3 =  rf.d_comp(nb_ela_file, line_ela_cis, path, press, analyse, 'shear', num_simu, stack_max, zoom, damage_comp)
        d_K3 =  rf.d_comp(nb_ela_file, line_ela_cis, path, press, analyse, 'bulk', num_simu, stack_max, zoom, damage_comp)

    elif num_simu == 4 : # stack 4
        d_G4 =  rf.d_comp(nb_ela_file, line_ela_cis, path, press, analyse, 'shear', num_simu, stack_max, zoom, damage_comp)
        d_K4 =  rf.d_comp(nb_ela_file, line_ela_cis, path, press, analyse, 'bulk', num_simu, stack_max, zoom, damage_comp)

    elif num_simu == 5 : # stack 5
        d_G5 =  rf.d_comp(nb_ela_file, line_ela_cis, path, press, analyse, 'shear', num_simu, stack_max, zoom, damage_comp)
        d_K5 =  rf.d_comp(nb_ela_file, line_ela_cis, path, press, analyse, 'bulk', num_simu, stack_max, zoom, damage_comp)

    elif num_simu == 6 : # stack 6
        d_G6 =  rf.d_comp(nb_ela_file, line_ela_cis, path, press, analyse, 'shear', num_simu, stack_max, zoom, damage_comp)
        d_K6 =  rf.d_comp(nb_ela_file, line_ela_cis, path, press, analyse, 'bulk', num_simu, stack_max, zoom, damage_comp)

    elif num_simu == 7 : # stack 7
        d_G7 =  rf.d_comp(nb_ela_file, line_ela_cis, path, press, analyse, 'shear', num_simu, stack_max, zoom, damage_comp)
        d_K7 =  rf.d_comp(nb_ela_file, line_ela_cis, path, press, analyse, 'bulk', num_simu, stack_max, zoom, damage_comp)

    elif num_simu == 8 : # stack 8
        d_G8 =  rf.d_comp(nb_ela_file, line_ela_cis, path, press, analyse, 'shear', num_simu, stack_max, zoom, damage_comp)
        d_K8 =  rf.d_comp(nb_ela_file, line_ela_cis, path, press, analyse, 'bulk', num_simu, stack_max, zoom, damage_comp)

    elif num_simu == 9 : # stack 9
        d_G9 =  rf.d_comp(nb_ela_file, line_ela_cis, path, press, analyse, 'shear', num_simu, stack_max, zoom, damage_comp)
        d_K9 =  rf.d_comp(nb_ela_file, line_ela_cis, path, press, analyse, 'bulk', num_simu, stack_max, zoom, damage_comp)

    elif num_simu == 10 : # stack 10
        d_G10 =  rf.d_comp(nb_ela_file, line_ela_cis, path, press, analyse, 'shear', num_simu, stack_max, zoom, damage_comp)
        d_K10 =  rf.d_comp(nb_ela_file, line_ela_cis, path, press, analyse, 'bulk', num_simu, stack_max, zoom, damage_comp)
    # end if

    # compute damage evolution of the system
    dam_K = rf_relax.d_stack_relax(dam_K,d_K1,d_K2,d_K3,d_K4,d_K5,d_K6,d_K7,d_K8,d_K9,d_K10,'damage',stack)
    dam_K_std = rf_relax.d_stack_relax(dam_K_std,d_K1,d_K2,d_K3,d_K4,d_K5,d_K6,d_K7,d_K8,d_K9,d_K10,'std',stack)
    dam_G = rf_relax.d_stack_relax(dam_G,d_G1,d_G2,d_G3,d_G4,d_G5,d_G6,d_G7,d_G8,d_G9,d_G10,'damage',stack)
    dam_G_std = rf_relax.d_stack_relax(dam_G_std,d_G1,d_G2,d_G3,d_G4,d_G5,d_G6,d_G7,d_G8,d_G9,d_G10,'std',stack)
# end of i for loop

# apparent regimes
regim, regim_disc = rf.simu_phase(val_sh_1, val_sh_2, val_sh_3, val_sh_4, val_sh_5, val_sh_6, val_sh_7, val_sh_8, val_sh_9, val_sh_10, stack, stack_max, line) # return index
regim_dam_G, regim_dam_K = rf_relax.simu_relax_phase(regim_disc,dam_G,dam_K, stack_max)

# Adimensionnement
if stack >= 1 : # stack 1
    vel_1 = np.array([val_ela_relax_1_1[0,8],val_ela_relax_1_2[0,8],val_ela_relax_1_3[0,8],val_ela_relax_1_4[0,8],val_ela_relax_1_5[0,8],val_ela_relax_1_6[0,8],val_ela_relax_1_7[0,8],val_ela_relax_1_8[0,8],val_ela_relax_1_9[0,8],val_ela_relax_1_10[0,8],val_ela_relax_1_11[0,8],val_ela_relax_1_12[0,8],val_ela_relax_1_13[0,8],val_ela_relax_1_14[0,8],val_ela_relax_1_15[0,8],val_ela_relax_1_16[0,8],val_ela_relax_1_17[0,8],val_ela_relax_1_18[0,8],val_ela_relax_1_19[0,8]])
    plt_ela_relax_1,coeff_1_sh,coeff_1_p = rf_relax.relax_plt(coeff_1_sh,coeff_1_p,E_g,t_n,val_sh_1,nb_ela_file,'val',analyse)
    error_relax_1,error_fit_1_sh,error_fit_1_p = rf_relax.relax_plt(error_fit_1_sh,error_fit_1_p,E_g,t_n,val_sh_1,nb_ela_file,'err',analyse)

    if need_gran == 'yes' :
        granulence[:,0] = rf_relax.gran_matrix(granulence_1_1,granulence_1_2,granulence_1_3,granulence_1_4,granulence_1_5,granulence_1_6,granulence_1_7,granulence_1_8,granulence_1_9,granulence_1_10,granulence_1_11,granulence_1_12,granulence_1_13,granulence_1_14,granulence_1_15,granulence_1_16,granulence_1_17,granulence_1_18,granulence_1_19,nb_ela_file,'granulence',ly,dg_dt,d_ave,rho,1)
        std_gran[:,0] = rf_relax.gran_matrix(granulence_1_1,granulence_1_2,granulence_1_3,granulence_1_4,granulence_1_5,granulence_1_6,granulence_1_7,granulence_1_8,granulence_1_9,granulence_1_10,granulence_1_11,granulence_1_12,granulence_1_13,granulence_1_14,granulence_1_15,granulence_1_16,granulence_1_17,granulence_1_18,granulence_1_19,nb_ela_file,'std_gran',ly,dg_dt,d_ave,rho,1)
    # end if

if stack >= 2 : # stack 2
    vel_2 = np.array([val_ela_relax_2_1[0,8],val_ela_relax_2_2[0,8],val_ela_relax_2_3[0,8],val_ela_relax_2_4[0,8],val_ela_relax_2_5[0,8],val_ela_relax_2_6[0,8],val_ela_relax_2_7[0,8],val_ela_relax_2_8[0,8],val_ela_relax_2_9[0,8],val_ela_relax_2_10[0,8],val_ela_relax_2_11[0,8],val_ela_relax_2_12[0,8],val_ela_relax_2_13[0,8],val_ela_relax_2_14[0,8],val_ela_relax_2_15[0,8],val_ela_relax_2_16[0,8],val_ela_relax_2_17[0,8],val_ela_relax_2_18[0,8],val_ela_relax_2_19[0,8]])
    plt_ela_relax_2,coeff_2_sh,coeff_2_p = rf_relax.relax_plt(coeff_2_sh,coeff_2_p,E_g,t_n,val_sh_2,nb_ela_file,'val',analyse)
    error_relax_2,error_fit_2_sh,error_fit_2_p = rf_relax.relax_plt(error_fit_2_sh,error_fit_2_p,E_g,t_n,val_sh_2,nb_ela_file,'err',analyse)

    if need_gran == 'yes' :
        granulence[:,1] = rf_relax.gran_matrix(granulence_2_1,granulence_2_2,granulence_2_3,granulence_2_4,granulence_2_5,granulence_2_6,granulence_2_7,granulence_2_8,granulence_2_9,granulence_2_10,granulence_2_11,granulence_2_12,granulence_2_13,granulence_2_14,granulence_2_15,granulence_2_16,granulence_2_17,granulence_2_18,granulence_2_19,nb_ela_file,'granulence',ly,dg_dt,d_ave,rho,2)
        std_gran[:,1] = rf_relax.gran_matrix(granulence_2_1,granulence_2_2,granulence_2_3,granulence_2_4,granulence_2_5,granulence_2_6,granulence_2_7,granulence_2_8,granulence_2_9,granulence_2_10,granulence_2_11,granulence_2_12,granulence_2_13,granulence_2_14,granulence_2_15,granulence_2_16,granulence_2_17,granulence_2_18,granulence_2_19,nb_ela_file,'std_gran',ly,dg_dt,d_ave,rho,2)
    # end if

if stack >= 3 : # stack 3
    vel_3 = np.array([val_ela_relax_3_1[0,8],val_ela_relax_3_2[0,8],val_ela_relax_3_3[0,8],val_ela_relax_3_4[0,8],val_ela_relax_3_5[0,8],val_ela_relax_3_6[0,8],val_ela_relax_3_7[0,8],val_ela_relax_3_8[0,8],val_ela_relax_3_9[0,8],val_ela_relax_3_10[0,8],val_ela_relax_3_11[0,8],val_ela_relax_3_12[0,8],val_ela_relax_3_13[0,8],val_ela_relax_3_14[0,8],val_ela_relax_3_15[0,8],val_ela_relax_3_16[0,8],val_ela_relax_3_17[0,8],val_ela_relax_3_18[0,8],val_ela_relax_3_19[0,8]])
    plt_ela_relax_3,coeff_3_sh,coeff_3_p = rf_relax.relax_plt(coeff_3_sh,coeff_3_p,E_g,t_n,val_sh_3,nb_ela_file,'val',analyse)
    error_relax_3,error_fit_3_sh,error_fit_3_p = rf_relax.relax_plt(error_fit_3_sh,error_fit_3_p,E_g,t_n,val_sh_3,nb_ela_file,'err',analyse)

    if need_gran == 'yes' :
        granulence[:,2] = rf_relax.gran_matrix(granulence_3_1,granulence_3_2,granulence_3_3,granulence_3_4,granulence_3_5,granulence_3_6,granulence_3_7,granulence_3_8,granulence_3_9,granulence_3_10,granulence_3_11,granulence_3_12,granulence_3_13,granulence_3_14,granulence_3_15,granulence_3_16,granulence_3_17,granulence_3_18,granulence_3_19,nb_ela_file,'granulence',ly,dg_dt,d_ave,rho,3)
        std_gran[:,2] = rf_relax.gran_matrix(granulence_3_1,granulence_3_2,granulence_3_3,granulence_3_4,granulence_3_5,granulence_3_6,granulence_3_7,granulence_3_8,granulence_3_9,granulence_3_10,granulence_3_11,granulence_3_12,granulence_3_13,granulence_3_14,granulence_3_15,granulence_3_16,granulence_3_17,granulence_3_18,granulence_3_19,nb_ela_file,'std_gran',ly,dg_dt,d_ave,rho,3)
    # end if

if stack >= 4 : # stack 4
    vel_4 = np.array([val_ela_relax_4_1[0,8],val_ela_relax_4_2[0,8],val_ela_relax_4_3[0,8],val_ela_relax_4_4[0,8],val_ela_relax_4_5[0,8],val_ela_relax_4_6[0,8],val_ela_relax_4_7[0,8],val_ela_relax_4_8[0,8],val_ela_relax_4_9[0,8],val_ela_relax_4_10[0,8],val_ela_relax_4_11[0,8],val_ela_relax_4_12[0,8],val_ela_relax_4_13[0,8],val_ela_relax_4_14[0,8],val_ela_relax_4_15[0,8],val_ela_relax_4_16[0,8],val_ela_relax_4_17[0,8],val_ela_relax_4_18[0,8],val_ela_relax_4_19[0,8]])
    plt_ela_relax_4,coeff_4_sh,coeff_4_p = rf_relax.relax_plt(coeff_4_sh,coeff_4_p,E_g,t_n,val_sh_4,nb_ela_file,'val',analyse)
    error_relax_4,error_fit_4_sh,error_fit_4_p = rf_relax.relax_plt(error_fit_4_sh,error_fit_4_p,E_g,t_n,val_sh_4,nb_ela_file,'err',analyse)

    if need_gran == 'yes' :
        granulence[:,3] = rf_relax.gran_matrix(granulence_4_1,granulence_4_2,granulence_4_3,granulence_4_4,granulence_4_5,granulence_4_6,granulence_4_7,granulence_4_8,granulence_4_9,granulence_4_10,granulence_4_11,granulence_4_12,granulence_4_13,granulence_4_14,granulence_4_15,granulence_4_16,granulence_4_17,granulence_4_18,granulence_4_19,nb_ela_file,'granulence',ly,dg_dt,d_ave,rho,4)
        std_gran[:,3] = rf_relax.gran_matrix(granulence_4_1,granulence_4_2,granulence_4_3,granulence_4_4,granulence_4_5,granulence_4_6,granulence_4_7,granulence_4_8,granulence_4_9,granulence_4_10,granulence_4_11,granulence_4_12,granulence_4_13,granulence_4_14,granulence_4_15,granulence_4_16,granulence_4_17,granulence_4_18,granulence_4_19,nb_ela_file,'std_gran',ly,dg_dt,d_ave,rho,4)
    # end if

if stack >= 5 : # stack 5
    vel_5 = np.array([val_ela_relax_5_1[0,8],val_ela_relax_5_2[0,8],val_ela_relax_5_3[0,8],val_ela_relax_5_4[0,8],val_ela_relax_5_5[0,8],val_ela_relax_5_6[0,8],val_ela_relax_5_7[0,8],val_ela_relax_5_8[0,8],val_ela_relax_5_9[0,8],val_ela_relax_5_10[0,8],val_ela_relax_5_11[0,8],val_ela_relax_5_12[0,8],val_ela_relax_5_13[0,8],val_ela_relax_5_14[0,8],val_ela_relax_5_15[0,8],val_ela_relax_5_16[0,8],val_ela_relax_5_17[0,8],val_ela_relax_5_18[0,8],val_ela_relax_5_19[0,8]])
    plt_ela_relax_5,coeff_5_sh,coeff_5_p = rf_relax.relax_plt(coeff_5_sh,coeff_5_p,E_g,t_n,val_sh_5,nb_ela_file,'val',analyse)
    error_relax_5,error_fit_5_sh,error_fit_5_p = rf_relax.relax_plt(error_fit_5_sh,error_fit_5_p,E_g,t_n,val_sh_5,nb_ela_file,'err',analyse)

    if need_gran == 'yes' :
        granulence[:,4] = rf_relax.gran_matrix(granulence_5_1,granulence_5_2,granulence_5_3,granulence_5_4,granulence_5_5,granulence_5_6,granulence_5_7,granulence_5_8,granulence_5_9,granulence_5_10,granulence_5_11,granulence_5_12,granulence_5_13,granulence_5_14,granulence_5_15,granulence_5_16,granulence_5_17,granulence_5_18,granulence_5_19,nb_ela_file,'granulence',ly,dg_dt,d_ave,rho,5)
        std_gran[:,4] = rf_relax.gran_matrix(granulence_5_1,granulence_5_2,granulence_5_3,granulence_5_4,granulence_5_5,granulence_5_6,granulence_5_7,granulence_5_8,granulence_5_9,granulence_5_10,granulence_5_11,granulence_5_12,granulence_5_13,granulence_5_14,granulence_5_15,granulence_5_16,granulence_5_17,granulence_5_18,granulence_5_19,nb_ela_file,'std_gran',ly,dg_dt,d_ave,rho,5)
    # end if

if stack >= 6 : # stack 6
    vel_6 = np.array([val_ela_relax_6_1[0,8],val_ela_relax_6_2[0,8],val_ela_relax_6_3[0,8],val_ela_relax_6_4[0,8],val_ela_relax_6_5[0,8],val_ela_relax_6_6[0,8],val_ela_relax_6_7[0,8],val_ela_relax_6_8[0,8],val_ela_relax_6_9[0,8],val_ela_relax_6_10[0,8],val_ela_relax_6_11[0,8],val_ela_relax_6_12[0,8],val_ela_relax_6_13[0,8],val_ela_relax_6_14[0,8],val_ela_relax_6_15[0,8],val_ela_relax_6_16[0,8],val_ela_relax_6_17[0,8],val_ela_relax_6_18[0,8],val_ela_relax_6_19[0,8]])
    plt_ela_relax_6,coeff_6_sh,coeff_6_p = rf_relax.relax_plt(coeff_6_sh,coeff_6_p,E_g,t_n,val_sh_6,nb_ela_file,'val',analyse)
    error_relax_6,error_fit_6_sh,error_fit_6_p = rf_relax.relax_plt(error_fit_6_sh,error_fit_6_p,E_g,t_n,val_sh_6,nb_ela_file,'err',analyse)

    if need_gran == 'yes' :
        granulence[:,5] = rf_relax.gran_matrix(granulence_6_1,granulence_6_2,granulence_6_3,granulence_6_4,granulence_6_5,granulence_6_6,granulence_6_7,granulence_6_8,granulence_6_9,granulence_6_10,granulence_6_11,granulence_6_12,granulence_6_13,granulence_6_14,granulence_6_15,granulence_6_16,granulence_6_17,granulence_6_18,granulence_6_19,nb_ela_file,'granulence',ly,dg_dt,d_ave,rho,6)
        std_gran[:,5] = rf_relax.gran_matrix(granulence_6_1,granulence_6_2,granulence_6_3,granulence_6_4,granulence_6_5,granulence_6_6,granulence_6_7,granulence_6_8,granulence_6_9,granulence_6_10,granulence_6_11,granulence_6_12,granulence_6_13,granulence_6_14,granulence_6_15,granulence_6_16,granulence_6_17,granulence_6_18,granulence_6_19,nb_ela_file,'std_gran',ly,dg_dt,d_ave,rho,6)
    # end if

if stack >= 7 : # stack 7
    vel_7 = np.array([val_ela_relax_7_1[0,8],val_ela_relax_7_2[0,8],val_ela_relax_7_3[0,8],val_ela_relax_7_4[0,8],val_ela_relax_7_5[0,8],val_ela_relax_7_6[0,8],val_ela_relax_7_7[0,8],val_ela_relax_7_8[0,8],val_ela_relax_7_9[0,8],val_ela_relax_7_10[0,8],val_ela_relax_7_11[0,8],val_ela_relax_7_12[0,8],val_ela_relax_7_13[0,8],val_ela_relax_7_14[0,8],val_ela_relax_7_15[0,8],val_ela_relax_7_16[0,8],val_ela_relax_7_17[0,8],val_ela_relax_7_18[0,8],val_ela_relax_7_19[0,8]])
    plt_ela_relax_7,coeff_7_sh,coeff_7_p = rf_relax.relax_plt(coeff_7_sh,coeff_7_p,E_g,t_n,val_sh_7,nb_ela_file,'val',analyse)
    error_relax_7,error_fit_7_sh,error_fit_7_p = rf_relax.relax_plt(error_fit_7_sh,error_fit_7_p,E_g,t_n,val_sh_7,nb_ela_file,'err',analyse)

    if need_gran == 'yes' :
        granulence[:,6] = rf_relax.gran_matrix(granulence_7_1,granulence_7_2,granulence_7_3,granulence_7_4,granulence_7_5,granulence_7_6,granulence_7_7,granulence_7_8,granulence_7_9,granulence_7_10,granulence_7_11,granulence_7_12,granulence_7_13,granulence_7_14,granulence_7_15,granulence_7_16,granulence_7_17,granulence_7_18,granulence_7_19,nb_ela_file,'granulence',ly,dg_dt,d_ave,rho,7)
        std_gran[:,6] = rf_relax.gran_matrix(granulence_7_1,granulence_7_2,granulence_7_3,granulence_7_4,granulence_7_5,granulence_7_6,granulence_7_7,granulence_7_8,granulence_7_9,granulence_7_10,granulence_7_11,granulence_7_12,granulence_7_13,granulence_7_14,granulence_7_15,granulence_7_16,granulence_7_17,granulence_7_18,granulence_7_19,nb_ela_file,'std_gran',ly,dg_dt,d_ave,rho,7)
    # end if

if stack >= 8 : # stack 8
    vel_8 = np.array([val_ela_relax_8_1[0,8],val_ela_relax_8_2[0,8],val_ela_relax_8_3[0,8],val_ela_relax_8_4[0,8],val_ela_relax_8_5[0,8],val_ela_relax_8_6[0,8],val_ela_relax_8_7[0,8],val_ela_relax_8_8[0,8],val_ela_relax_8_9[0,8],val_ela_relax_8_10[0,8],val_ela_relax_8_11[0,8],val_ela_relax_8_12[0,8],val_ela_relax_8_13[0,8],val_ela_relax_8_14[0,8],val_ela_relax_8_15[0,8],val_ela_relax_8_16[0,8],val_ela_relax_8_17[0,8],val_ela_relax_8_18[0,8],val_ela_relax_8_19[0,8]])
    plt_ela_relax_8,coeff_8_sh,coeff_8_p = rf_relax.relax_plt(coeff_8_sh,coeff_8_p,E_g,t_n,val_sh_8,nb_ela_file,'val',analyse)
    error_relax_8,error_fit_8_sh,error_fit_8_p = rf_relax.relax_plt(error_fit_8_sh,error_fit_8_p,E_g,t_n,val_sh_8,nb_ela_file,'err',analyse)

    if need_gran == 'yes' :
        granulence[:,7] = rf_relax.gran_matrix(granulence_8_1,granulence_8_2,granulence_8_3,granulence_8_4,granulence_8_5,granulence_8_6,granulence_8_7,granulence_8_8,granulence_8_9,granulence_8_10,granulence_8_11,granulence_8_12,granulence_8_13,granulence_8_14,granulence_8_15,granulence_8_16,granulence_8_17,granulence_8_18,granulence_8_19,nb_ela_file,'granulence',ly,dg_dt,d_ave,rho,8)
        std_gran[:,7] = rf_relax.gran_matrix(granulence_8_1,granulence_8_2,granulence_8_3,granulence_8_4,granulence_8_5,granulence_8_6,granulence_8_7,granulence_8_8,granulence_8_9,granulence_8_10,granulence_8_11,granulence_8_12,granulence_8_13,granulence_8_14,granulence_8_15,granulence_8_16,granulence_8_17,granulence_8_18,granulence_8_19,nb_ela_file,'std_gran',ly,dg_dt,d_ave,rho,8)
    # end if

if stack >= 9 : # stack 9
    vel_9 = np.array([val_ela_relax_9_1[0,8],val_ela_relax_9_2[0,8],val_ela_relax_9_3[0,8],val_ela_relax_9_4[0,8],val_ela_relax_9_5[0,8],val_ela_relax_9_6[0,8],val_ela_relax_9_7[0,8],val_ela_relax_9_8[0,8],val_ela_relax_9_9[0,8],val_ela_relax_9_10[0,8],val_ela_relax_9_11[0,8],val_ela_relax_9_12[0,8],val_ela_relax_9_13[0,8],val_ela_relax_9_14[0,8],val_ela_relax_9_15[0,8],val_ela_relax_9_16[0,8],val_ela_relax_9_17[0,8],val_ela_relax_9_18[0,8],val_ela_relax_9_19[0,8]])
    plt_ela_relax_9,coeff_9_sh,coeff_9_p = rf_relax.relax_plt(coeff_9_sh,coeff_9_p,E_g,t_n,val_sh_9,nb_ela_file,'val',analyse)
    error_relax_9,error_fit_9_sh,error_fit_9_p = rf_relax.relax_plt(error_fit_9_sh,error_fit_9_p,E_g,t_n,val_sh_9,nb_ela_file,'err',analyse)

    if need_gran == 'yes' :
        granulence[:,8] = rf_relax.gran_matrix(granulence_9_1,granulence_9_2,granulence_9_3,granulence_9_4,granulence_9_5,granulence_9_6,granulence_9_7,granulence_9_8,granulence_9_9,granulence_9_10,granulence_9_11,granulence_9_12,granulence_9_13,granulence_9_14,granulence_9_15,granulence_9_16,granulence_9_17,granulence_9_18,granulence_9_19,nb_ela_file,'granulence',ly,dg_dt,d_ave,rho,9)
        std_gran[:,8] = rf_relax.gran_matrix(granulence_9_1,granulence_9_2,granulence_9_3,granulence_9_4,granulence_9_5,granulence_9_6,granulence_9_7,granulence_9_8,granulence_9_9,granulence_9_10,granulence_9_11,granulence_9_12,granulence_9_13,granulence_9_14,granulence_9_15,granulence_9_16,granulence_9_17,granulence_9_18,granulence_9_19,nb_ela_file,'std_gran',ly,dg_dt,d_ave,rho,9)
    # end if

if stack >= 10 : # stack 10
    vel_10 = np.array([val_ela_relax_10_1[0,8],val_ela_relax_10_2[0,8],val_ela_relax_10_3[0,8],val_ela_relax_10_4[0,8],val_ela_relax_10_5[0,8],val_ela_relax_10_6[0,8],val_ela_relax_10_7[0,8],val_ela_relax_10_8[0,8],val_ela_relax_10_9[0,8],val_ela_relax_10_10[0,8],val_ela_relax_10_11[0,8],val_ela_relax_10_12[0,8],val_ela_relax_10_13[0,8],val_ela_relax_10_14[0,8],val_ela_relax_10_15[0,8],val_ela_relax_10_16[0,8],val_ela_relax_10_17[0,8],val_ela_relax_10_18[0,8],val_ela_relax_10_19[0,8]])
    plt_ela_relax_10,coeff_10_sh,coeff_10_p = rf_relax.relax_plt(coeff_10_sh,coeff_10_p,E_g,t_n,val_sh_10,nb_ela_file,'val',analyse)
    error_relax_10,error_fit_10_sh,error_fit_10_p = rf_relax.relax_plt(error_fit_10_sh,error_fit_10_p,E_g,t_n,val_sh_10,nb_ela_file,'err',analyse)

    if need_gran == 'yes' :
        granulence[:,9] = rf_relax.gran_matrix(granulence_10_1,granulence_10_2,granulence_10_3,granulence_10_4,granulence_10_5,granulence_10_6,granulence_10_7,granulence_10_8,granulence_10_9,granulence_10_10,granulence_10_11,granulence_10_12,granulence_10_13,granulence_10_14,granulence_10_15,granulence_10_16,granulence_10_17,granulence_10_18,granulence_10_19,nb_ela_file,'granulence',ly,dg_dt,d_ave,rho,10)
        std_gran[:,9] = rf_relax.gran_matrix(granulence_10_1,granulence_10_2,granulence_10_3,granulence_10_4,granulence_10_5,granulence_10_6,granulence_10_7,granulence_10_8,granulence_10_9,granulence_10_10,granulence_10_11,granulence_10_12,granulence_10_13,granulence_10_14,granulence_10_15,granulence_10_16,granulence_10_17,granulence_10_18,granulence_10_19,nb_ela_file,'std_gran',ly,dg_dt,d_ave,rho,10)
    # end if
# end if

# end if

# compute visosity evolution of the system
eta_sh, d_eta_sh = rf_relax.visc(plt_ela_relax_1, plt_ela_relax_2, plt_ela_relax_3, plt_ela_relax_4, plt_ela_relax_5, error_fit_1_sh, error_fit_2_sh, error_fit_3_sh, error_fit_4_sh, error_fit_5_sh, G_ela, dG_ela,'shear')
eta_p, d_eta_p = rf_relax.visc(plt_ela_relax_1, plt_ela_relax_2, plt_ela_relax_3, plt_ela_relax_4, plt_ela_relax_5, error_fit_1_p, error_fit_2_p, error_fit_3_p, error_fit_4_p, error_fit_5_p, K_ela, dK_ela,'pressure')

t_sh = rf_relax.relax_matrix(plt_ela_relax_1,plt_ela_relax_2,plt_ela_relax_3,plt_ela_relax_4,plt_ela_relax_5,'sh relax',stack_max)
t_p =  rf_relax.relax_matrix(plt_ela_relax_1,plt_ela_relax_2,plt_ela_relax_3,plt_ela_relax_4,plt_ela_relax_5,'p relax',stack_max)

beta_sh = rf_relax.relax_matrix(plt_ela_relax_1,plt_ela_relax_2,plt_ela_relax_3,plt_ela_relax_4,plt_ela_relax_5,'sh beta',stack_max)
beta_p = rf_relax.relax_matrix(plt_ela_relax_1,plt_ela_relax_2,plt_ela_relax_3,plt_ela_relax_4,plt_ela_relax_5,'p beta',stack_max)

tau_c = rf_relax.relax_matrix(plt_ela_relax_1,plt_ela_relax_2,plt_ela_relax_3,plt_ela_relax_4,plt_ela_relax_5,'sh stress',stack_max)
p_c =  rf_relax.relax_matrix(plt_ela_relax_1,plt_ela_relax_2,plt_ela_relax_3,plt_ela_relax_4,plt_ela_relax_5,'p stress',stack_max)

d_t_sh = rf_relax.relax_matrix(error_relax_1,error_relax_2,error_relax_3,error_relax_4,error_relax_5,'sh relax',stack_max)
d_t_p =  rf_relax.relax_matrix(error_relax_1,error_relax_2,error_relax_3,error_relax_4,error_relax_5,'p relax',stack_max)

d_beta_sh = rf_relax.relax_matrix(error_relax_1,error_relax_2,error_relax_3,error_relax_4,error_relax_5,'sh beta',stack_max)
d_beta_p = rf_relax.relax_matrix(error_relax_1,error_relax_2,error_relax_3,error_relax_4,error_relax_5,'p beta',stack_max)

d_tau_c = rf_relax.relax_matrix(error_relax_1,error_relax_2,error_relax_3,error_relax_4,error_relax_5,'sh stress',stack_max)
d_p_c =  rf_relax.relax_matrix(error_relax_1,error_relax_2,error_relax_3,error_relax_4,error_relax_5,'p stress',stack_max)

if stack >= 1 : print("\n", "plt_ela_relax = ", "\n", "T_s/E_g P_s/E_g t_sh_relax/t_N t_p_relax/t_N b_sh b_p"), print(plt_ela_relax_1)
if stack >= 2 : print("\n", "plt_ela_relax = ", "\n", "T_s/E_g P_s/E_g t_sh_relax/t_N t_p_relax/t_N b_sh b_p"), print(plt_ela_relax_2)
if stack >= 3 : print("\n", "plt_ela_relax = ", "\n", "T_s/E_g P_s/E_g t_sh_relax/t_N t_p_relax/t_N b_sh b_p"), print(plt_ela_relax_3)
if stack >= 4 : print("\n", "plt_ela_relax = ", "\n", "T_s/E_g P_s/E_g t_sh_relax/t_N t_p_relax/t_N b_sh b_p"), print(plt_ela_relax_4)
if stack >= 5 : print("\n", "plt_ela_relax = ", "\n", "T_s/E_g P_s/E_g t_sh_relax/t_N t_p_relax/t_N b_sh b_p"), print(plt_ela_relax_5)
# end if

print(" \n", "G_ela_relax = ", "\n", "G1/E_g G2/E_g G3/E_g G4/E_g G5/E_g"), print(G_ela)
# enf if

if save_variable == 'yes':
    for num_simu in range(stack):
        np.savetxt(f'{name_file_relax_t_sh}_N_{grain}_{press}_{analyse}.txt', t_sh[:], fmt='%.2e', header = 't*_sh_1 /t_N t*_sh_2 /t_N t*_sh_3 /t_N t*_sh_4 /t_N t*_sh_5 /t_N')
        np.savetxt(f'{name_file_relax_s_sh}_N_{grain}_{press}_{analyse}.txt', tau_c[:], fmt='%.2e', header = 'T_c_1 /E_g T_c_2 /E_g T_c_3 /E_g T_c_4 /E_g T_c_5 /E_g')
        np.savetxt(f'{name_file_relax_b_sh}_N_{grain}_{press}_{analyse}.txt', beta_sh[:], fmt='%.2e', header = 'beta_sh_1 beta_sh_2 beta_sh_3 beta_sh_4 beta_sh_5')
        np.savetxt(f'{name_file_relax_t_p}_N_{grain}_{press}_{analyse}.txt', t_p[:], fmt='%.2e', header = 't*_p_1 /t_N t*_p_2 /t_N t*_p_3 /t_N t*_p_4 /t_N t*_p_5 /t_N')
        np.savetxt(f'{name_file_relax_s_p}_N_{grain}_{press}_{analyse}.txt', p_c[:], fmt='%.2e', header = 'P_c_1 /E_g P_c_2 /E_g P_c_3 /E_g P_c_4 /E_g P_c_5 /E_g')
        np.savetxt(f'{name_file_relax_b_p}_N_{grain}_{press}_{analyse}.txt', beta_p[:], fmt='%.2e', header = 'beta_p_1 beta_p_2 beta_p_3 beta_p_4 beta_p_5')
        if need_gran == 'yes' : np.savetxt(f'{name_file_relax_gran}_N_{grain}_{press}_{analyse}.txt', granulence[:], fmt='%.2e', header = 'theta_1 theta_2 theta_3 theta_4 theta_5')

        np.savetxt(f'std_{name_file_relax_t_sh}_N_{grain}_{press}_{analyse}.txt', d_t_sh[:], fmt='%.2e', header = 'd_t*_sh_1 /t_N d_t*_sh_2 /t_N d_t*_sh_3 /t_N d_t*_sh_4 /t_N d_t*_sh_5 /t_N')
        np.savetxt(f'std_{name_file_relax_s_sh}_N_{grain}_{press}_{analyse}.txt', d_tau_c[:], fmt='%.2e', header = 'd_T_c_1 /E_g d_T_c_2 /E_g d_T_c_3 /E_g d_T_c_4 /E_g d_T_c_5 /E_g')
        np.savetxt(f'std_{name_file_relax_b_sh}_N_{grain}_{press}_{analyse}.txt', d_beta_sh[:], fmt='%.2e', header = 'd_beta_sh_1 d_beta_sh_2 d_beta_sh_3 d_beta_sh_4 d_beta_sh_5')
        np.savetxt(f'std_{name_file_relax_t_p}_N_{grain}_{press}_{analyse}.txt', d_t_p[:], fmt='%.2e', header = 'd_t*_p_1 /t_N d_t*_p_2 /t_N d_t*_p_3 /t_N d_t*_p_4 /t_N d_t*_p_5 /t_N')
        np.savetxt(f'std_{name_file_relax_s_p}_N_{grain}_{press}_{analyse}.txt', d_p_c[:], fmt='%.2e', header = 'd_P_c_1 /E_g d_P_c_2 /E_g d_P_c_3 /E_g d_P_c_4 /E_g d_P_c_5 /E_g')
        np.savetxt(f'std_{name_file_relax_b_p}_N_{grain}_{press}_{analyse}.txt', d_beta_p[:], fmt='%.2e', header = 'd_beta_p_1 d_beta_p_2 d_beta_p_3 d_beta_p_4 d_beta_p_5')
        if need_gran == 'yes' : np.savetxt(f'std_{name_file_relax_gran}_N_{grain}_{press}_{analyse}.txt', std_gran[:], fmt='%.2e', header = 'd_theta_1 d_theta_2 d_theta_3 d_theta_4 d_theta_5')
    # end of i for loop
# end of if

## Graph output #
print('\n','(1/5) Print elastic relaxation plot for a given \u03b3 ? (yes/no)')
print_ela_relax_g = input()
if print_ela_relax_g == 'yes':
    # Relaxation at a given deformation for various I
    # 0.25 %
    g_relax.graph_ela_relax_I(val_ela_relax_1_2,val_ela_relax_2_2,val_ela_relax_3_2,val_ela_relax_4_2,val_ela_relax_5_2,tag1,tag2,tag3,tag4,tag5,colormap_ela,E_g,t_n,d_ave,shear_stress,stack)

    # 5 %
    g_relax.graph_ela_relax_I(val_ela_relax_1_6,val_ela_relax_2_6,val_ela_relax_3_6,val_ela_relax_4_6,val_ela_relax_5_6,tag1,tag2,tag3,tag4,tag5,colormap_ela,E_g,d_ave,t_n,shear_stress,stack)

    # 50 %
    g_relax.graph_ela_relax_I(val_ela_relax_1_14,val_ela_relax_2_14,val_ela_relax_3_14,val_ela_relax_4_14,val_ela_relax_5_14,tag1,tag2,tag3,tag4,tag5,colormap_ela,E_g,t_n,d_ave,shear_stress,stack)

    # 100%
    g_relax.graph_ela_relax_I(val_ela_relax_1_19,val_ela_relax_2_19,val_ela_relax_3_19,val_ela_relax_4_19,val_ela_relax_5_19,tag1,tag2,tag3,tag4,tag5,colormap_ela,E_g,t_n,d_ave,shear_stress,stack)
# end if

print('\n', '(2/5) Print elastic relaxation plot ? (yes/no)')
print_ela_relax = input()
if print_ela_relax == 'yes' :
    if stack >= 1 :
        g_relax.graph_ela_relax(val_ela_relax_1_1,val_ela_relax_1_2,val_ela_relax_1_3,val_ela_relax_1_4,val_ela_relax_1_5,val_ela_relax_1_6,val_ela_relax_1_7,val_ela_relax_1_8,val_ela_relax_1_9,val_ela_relax_1_10,val_ela_relax_1_11,val_ela_relax_1_12,val_ela_relax_1_13,val_ela_relax_1_14,val_ela_relax_1_15,val_ela_relax_1_16,val_ela_relax_1_17,val_ela_relax_1_18,val_ela_relax_1_19,coeff_1_sh,coeff_1_p,colormap_ela,E_g,t_n,d_ave,shear_stress,nb_ela_file)
    if stack >= 2 :
        g_relax.graph_ela_relax(val_ela_relax_2_1,val_ela_relax_2_2,val_ela_relax_2_3,val_ela_relax_2_4,val_ela_relax_2_5,val_ela_relax_2_6,val_ela_relax_2_7,val_ela_relax_2_8,val_ela_relax_2_9,val_ela_relax_2_10,val_ela_relax_2_11,val_ela_relax_2_12,val_ela_relax_2_13,val_ela_relax_2_14,val_ela_relax_2_15,val_ela_relax_2_16,val_ela_relax_2_17,val_ela_relax_2_18,val_ela_relax_2_19,coeff_2_sh,coeff_2_p,colormap_ela,E_g,t_n,d_ave,shear_stress,nb_ela_file)
    if stack >= 3 :
        g_relax.graph_ela_relax(val_ela_relax_3_1,val_ela_relax_3_2,val_ela_relax_3_3,val_ela_relax_3_4,val_ela_relax_3_5,val_ela_relax_3_6,val_ela_relax_3_7,val_ela_relax_3_8,val_ela_relax_3_9,val_ela_relax_3_10,val_ela_relax_3_11,val_ela_relax_3_12,val_ela_relax_3_13,val_ela_relax_3_14,val_ela_relax_3_15,val_ela_relax_3_16,val_ela_relax_3_17,val_ela_relax_3_18,val_ela_relax_3_19,coeff_3_sh,coeff_3_p,colormap_ela,E_g,t_n,d_ave,shear_stress,nb_ela_file)
    if stack >= 4 :
        g_relax.graph_ela_relax(val_ela_relax_4_1,val_ela_relax_4_2,val_ela_relax_4_3,val_ela_relax_4_4,val_ela_relax_4_5,val_ela_relax_4_6,val_ela_relax_4_7,val_ela_relax_4_8,val_ela_relax_4_9,val_ela_relax_4_10,val_ela_relax_4_11,val_ela_relax_4_12,val_ela_relax_4_13,val_ela_relax_4_14,val_ela_relax_4_15,val_ela_relax_4_16,val_ela_relax_4_17,val_ela_relax_4_18,val_ela_relax_4_19,coeff_4_sh,coeff_4_p,colormap_ela,E_g,t_n,d_ave,shear_stress,nb_ela_file)
    if stack >= 5 :
        g_relax.graph_ela_relax(val_ela_relax_5_1,val_ela_relax_5_2,val_ela_relax_5_3,val_ela_relax_5_4,val_ela_relax_5_5,val_ela_relax_5_6,val_ela_relax_5_7,val_ela_relax_5_8,val_ela_relax_5_9,val_ela_relax_5_10,val_ela_relax_5_11,val_ela_relax_5_12,val_ela_relax_5_13,val_ela_relax_5_14,val_ela_relax_5_15,val_ela_relax_5_16,val_ela_relax_5_17,val_ela_relax_5_18,val_ela_relax_5_19,coeff_5_sh,coeff_5_p,colormap_ela,E_g,t_n,d_ave,shear_stress,nb_ela_file)
# end if

print('\n', '(3/5) Print elastic relaxation parameters ? (yes/no)')
print_param = input()
if print_param == 'yes':
    # parameters versus macro/micro variables
    # variable phi and Z opening
    val_1 = rf.file_data(line,path,1,shear_stress,dg_dt[0]) # num_simu 1
    val_2 = rf.file_data(line,path,2,shear_stress,dg_dt[1]) # num_simu 2
    val_3 = rf.file_data(line,path,3,shear_stress,dg_dt[2]) # num_simu 3
    val_4 = rf.file_data(line,path,4,shear_stress,dg_dt[3]) # num_simu 4
    val_5 = rf.file_data(line,path,5,shear_stress,dg_dt[4]) # num_simu 5
    val_6 = rf.file_data(line,path,6,shear_stress,dg_dt[5]) # num_simu 6
    val_7 = rf.file_data(line,path,7,shear_stress,dg_dt[6]) # num_simu 7
    val_8 = rf.file_data(line,path,8,shear_stress,dg_dt[7]) # num_simu 8
    val_9 = rf.file_data(line,path,9,shear_stress,dg_dt[8]) # num_simu 9
    val_10 = rf.file_data(line,path,10,shear_stress,dg_dt[9]) # num_simu 10

    phi = rf_relax.variable_matrix_relax(val_1, val_2, val_3, val_4, val_5, val_6, val_7, val_8, val_9, val_10, nb_ela_file, stack, stack_max, line,'phi')
    z = rf_relax.variable_matrix_relax(val_1, val_2, val_3, val_4, val_5, val_6, val_7, val_8, val_9, val_10, nb_ela_file, stack, stack_max, line, 'z')

    #g_relax.graph_granulence(gamma_0,dam_G,dam_K,granulence,std_gran,regim_disc,regim_dam_G,regim_dam_K,colormap_g_1,colormap_g_2,tag1,tag2,tag3,tag4,tag5,tag6,tag7,tag8,tag9,tag10,stack,stack_max,nb_ela_file,analyse)
    g_relax.graph_relax(plt_ela_relax_1,plt_ela_relax_2,plt_ela_relax_3,plt_ela_relax_4,plt_ela_relax_5,plt_ela_relax_6,plt_ela_relax_7,plt_ela_relax_8,plt_ela_relax_9,plt_ela_relax_10,error_relax_1,error_relax_2,error_relax_3,error_relax_4,error_relax_5,error_relax_6,error_relax_7,error_relax_8,error_relax_9,error_relax_10,gamma_0,regim_disc,colormap_g_1,colormap_g_2,tag1,tag2,tag3,tag4,tag5,tag6,tag7,tag8,tag9,tag10,stack,stack_max,analyse,shear_stress,'gamma_0')
    #g_relax.graph_relax(plt_ela_relax_1,plt_ela_relax_2,plt_ela_relax_3,plt_ela_relax_4,plt_ela_relax_5,error_relax_1,error_relax_2,error_relax_3,error_relax_4,error_relax_5,phi,regim_disc,colormap_g,tag1,tag2,tag3,tag4,tag5,stack,stack_max,analyse,shear_stress,'phi')
    #g_relax.graph_relax(plt_ela_relax_1,plt_ela_relax_2,plt_ela_relax_3,plt_ela_relax_4,plt_ela_relax_5,error_fit_1_sh,error_fit_2_sh,error_fit_3_sh,error_fit_4_sh,error_fit_5_sh,error_fit_1_p,error_fit_2_p,error_fit_3_p,error_fit_4_p,error_fit_5_p,z,t_n,E,colormap_g,tag1,tag2,tag3,tag4,tag5,stack,stack_max,shear_stress,'Z')
    #g_relax.graph_relax(plt_ela_relax_1_run,plt_ela_relax_2_run,plt_ela_relax_3_run,plt_ela_relax_4_run,plt_ela_relax_5_run,error_fit_1_sh,error_fit_2_sh,error_fit_3_sh,error_fit_4_sh,error_fit_5_sh,error_fit_1_p,error_fit_2_p,error_fit_3_p,error_fit_4_p,error_fit_5_p,gamma_0,t_n,E,colormap_g,tag1,tag2,tag3,tag4,tag5,stack,shear_stress,stack_max)
# end of if

print('\n', '(4/5) Print elastic properties vs rheology ? (yes/no)')
print_sh = input()
if print_sh =='yes':
    g_relax.rheo_ela_prop(gamma_0,val_sh_1,val_sh_2,val_sh_3,val_sh_4,val_sh_5,val_sh_6,val_sh_7,val_sh_8,val_sh_9,val_sh_10,plt_ela_relax_1,plt_ela_relax_2,plt_ela_relax_3,plt_ela_relax_4,plt_ela_relax_5,plt_ela_relax_6,plt_ela_relax_7,plt_ela_relax_8,plt_ela_relax_9,plt_ela_relax_10,error_relax_1,error_relax_2,error_relax_3,error_relax_4,error_relax_5,error_relax_6,error_relax_7,error_relax_8,error_relax_9,error_relax_10,stack,stack_max,tag1,tag2,tag3,tag4,tag5,tag6,tag7,tag8,tag9,tag10,colormap_g_1,colormap_g_2,analyse,shear_stress,press)
# end if

print('\n', '(5/5) Print elastic properties versus damage ? (yes/no)')
print_ela_prop = input()
if print_ela_prop == 'yes' :
    # Relaxation time as function of damage
    #g_relax.evo_prop(granulence,plt_ela_relax_1,plt_ela_relax_2,plt_ela_relax_3,plt_ela_relax_4,plt_ela_relax_5,plt_ela_relax_6,plt_ela_relax_7,plt_ela_relax_8,plt_ela_relax_9,plt_ela_relax_10,dG_ela,dam_G,dam_K,dam_G_std,dam_K_std,error_relax_1,error_relax_2,error_relax_3,error_relax_4,error_relax_5,error_relax_6,error_relax_7,error_relax_8,error_relax_9,error_relax_10,regim_dam_G,regim_dam_K,regim_gran,stack,tag1,tag2,tag3,tag4,tag5,tag6,tag7,tag8,tag9,tag10,colormap_g_1,colormap_g_2,stack_max,analyse,shear_stress,'granulence')
    g_relax.evo_prop(gamma_0,plt_ela_relax_1,plt_ela_relax_2,plt_ela_relax_3,plt_ela_relax_4,plt_ela_relax_5,plt_ela_relax_6,plt_ela_relax_7,plt_ela_relax_8,plt_ela_relax_9,plt_ela_relax_10,dG_ela,dam_G,dam_K,dam_G_std,dam_K_std,error_relax_1,error_relax_2,error_relax_3,error_relax_4,error_relax_5,error_relax_6,error_relax_7,error_relax_8,error_relax_9,error_relax_10,regim_dam_G,regim_dam_K,stack,tag1,tag2,tag3,tag4,tag5,tag6,tag7,tag8,tag9,tag10,colormap_g_1,colormap_g_2,stack_max,analyse,shear_stress,'damage')
# end of if
# End