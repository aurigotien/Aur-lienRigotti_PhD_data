### !!! The code need to be modify depending of which version of the lammps script your are using !!!
### !!! As this code is made to work on my computer the path for the log.lammps file need to be modified

# Plot the graph from the log.lammps file
# Beginning

import numpy as np
import stack_files as rf
import stack_graph as g

### Needed anaylsis ----------------------------------------------------------- ###

# Modulus to compute
### Problem variable ---------------------------------------------------------- ###

## Scalar variables ----------------------------------------------------------- ##

# Number of stacks used
stack_max = 10 # maximum of stacks usable
stack = 4
nb_ela_file = 19 # number of elastic shearing/compression files

preparation = 'no_fric' # fric or fric_1 or no_fric
shear_stress = 'shear' # shear or deviatoric
analyse = 'strain' # analyse (strain or pressure)
stress = 'size' # = P_90kPa, P_50kPa, P_5kPa, P_50_90_kPa, P_5_50_90_kPa, I_cste or size
damage_compute = 'idealise' # val_0 (take module val at onset of shear) or idealise (take the highest, save ini mod)

zoom = 0 # number of data line to cut in elastic files

if preparation == 'no_fric' and (stress == 'P_5kPa' or stress == 'P_50kPa' or stress == 'P_90kPa') :
    stacks_file = f'stacks/strain_pressure/prep_{preparation}/{stress}'
    if stress == 'P_5kPa': press = 'P_5000'
    if stress == 'P_50kPa': press = 'P_50000'
    if stress == 'P_90kPa': press = 'P_90000'
elif preparation == 'fric' and stress == 'P_50kPa' :
    stacks_file = f'stacks/strain_pressure/prep_{preparation}/{stress}'
    if stress == 'P_50kPa': press = 'P_50000'
elif stress == 'I_cste' :
    stacks_file = f'stacks_read/plot_with_I/{stress}'
    if stress == 'P_50kPa': press = 'P_50000'
elif stress == 'P_50_90_kPa':
    stacks_file = f'stacks_read/{stress}'
    press = 'P_50000_90000'
elif stress == 'P_50_90_kPa_I':
    stacks_file = f'stacks_read/{stress}'
    press = 'P_50000_90000'
elif stress == 'P_5_50_90_kPa':
    stacks_file = f'stacks_read/{stress}'
    press = 'P_5000_50000_90000'
elif preparation == 'fric_1' and stress == 'P_50kPa' :
    preparation = 'fric'
    stacks_file = f'stacks_read/prep_{preparation}/{stress}'
    if stress == 'P_50kPa': press = 'P_50000_no_f_f'
elif stress == 'size' :
    stacks_file = f'stacks/{stress}'
    press = 'P_50000'
# end if

# Save the matrix of the measured variables
save_variable = 'no'
save_ref_mod = 'no'
no_grain = 'N_10000'
name_file = f'plt_{no_grain}_{press}'
name_file_sh = f'tau_{no_grain}_{press}'
name_file_phi = f'phi_{no_grain}_{press}'
name_file_z = f'z_{no_grain}_{press}'
name_file_pression = f'pressure_{no_grain}_{press}'
name_file_ela = f'{no_grain}_{press}_ela'

# Tag for the graph
tag1,tag2,tag3,tag4,tag5,tag6,tag7,tag8,tag9,tag10 = rf.plot_tag(analyse, stress, preparation)

# Size effect
"""
tag1 = 'N = 1,000 grains' # tag for stack 1 graph output
tag2 = 'N = 5,000 grains' # tag for stack 2 graph output
tag3 = 'N = 10,000 grains' # tag for stack 3 graph output
tag4 = 'N = 20,000 grains' # tag for stack 4 graph output
tag5 = '' # tag for stack 5 graph output
#"""

# graph type
dg_dt, colormap_g_1, colormap_g_2 = rf.applied_shear(analyse, preparation, stress)

### Needed anaylsis ----------------------------------------------------------- ###
# Output of the program
print('Sample preparation data extraction ? (yes/no)')
need_prep = input()

print('Simple shear test data extraction ? (yes/no)')
need_sh = input()

print('Elastic propeties test data extraction ? (yes/no)')
need_ela = input()

print('Evolution of damage ? (yes/no)')
need_d = input()

### Problem variable ---------------------------------------------------------- ###

# Caracter chain
# Choose to print or not the needed cruves
print_relax = ''
print_sh = ''
print_rheo = ''
print_ela_comp = ''
print_ela_cis = ''
print_ela_prop = ''
print_dam = ''

# Scalar
line = 1000 # number of line of cis file
line_relax = 100 # number of line of relax file
col_relax = 11 # number of column of relax file
col_cis = 18 # number of column of cis file (step/atoms/Z/phi/Lx/Ly/angle of box/Sxx/Syy/Sxy)
col_ela_cis = 8 # number of column in elastic oscillatory test files
col_ela_comp = 8
line_ela_comp = 401 # number of line of ela_comp file
line_ela_cis = 401 # number of line of ela_cis file

# Adimensional parameters
E = 5E8 # material (sea ice) young modulus (Pa)
t_n = 5E-2 # grain normal oscillation time (s)
d_ave = 100 # grain average diameter (m)

## Matrix initialisation ------------------------------------------------------ ##

# Store the final values of shear strain, shear stress and mean stress E_xy_f, T_f and P_f
fin_val = np.zeros((4,10))

# store the value of plateau of stress + std
plt = np.zeros((stack_max,16))
d = np.zeros((nb_ela_file,stack_max))

# Store the values of data_relax.txt #
val_relax1 = np.zeros((line,col_relax)) # stack 1
val_relax2 = np.zeros((line,col_relax)) # stack 2
val_relax3 = np.zeros((line,col_relax)) # stack 3
val_relax4 = np.zeros((line,col_relax)) # stack 4
val_relax5 = np.zeros((line,col_relax)) # stack 5
val_relax6 = np.zeros((line,col_relax)) # stack 6
val_relax7 = np.zeros((line,col_relax)) # stack 7
val_relax8 = np.zeros((line,col_relax)) # stack 8
val_relax9 = np.zeros((line,col_relax)) # stack 9
val_relax10 = np.zeros((line,col_relax)) # stack 10

# Store the values of data_precomp.txt #
val_precomp1 = np.zeros((line,col_relax)) # stack 1
val_precomp2 = np.zeros((line,col_relax)) # stack 2
val_precomp3 = np.zeros((line,col_relax)) # stack 3
val_precomp4 = np.zeros((line,col_relax)) # stack 4
val_precomp5 = np.zeros((line,col_relax)) # stack 5
val_precomp6 = np.zeros((line,col_relax)) # stack 6
val_precomp7 = np.zeros((line,col_relax)) # stack 7
val_precomp8 = np.zeros((line,col_relax)) # stack 8
val_precomp9 = np.zeros((line,col_relax)) # stack 9
val_precomp10 = np.zeros((line,col_relax)) # stack 10

# Store the values of data_cis.txt #
val_1 = np.zeros((line,col_cis)) # stack 1
val_2 = np.zeros((line,col_cis)) # stack 2
val_3 = np.zeros((line,col_cis)) # stack 3
val_4 = np.zeros((line,col_cis)) # stack 4
val_5 = np.zeros((line,col_cis)) # stack 5
val_6 = np.zeros((line,col_cis)) # stack 6
val_7 = np.zeros((line,col_cis)) # stack 7
val_8 = np.zeros((line,col_cis)) # stack 8
val_9 = np.zeros((line,col_cis)) # stack 9
val_10 = np.zeros((line,col_cis)) # stack 10

# granulence matrix
granulence = np.zeros((nb_ela_file,stack_max))
std_granulence = np.zeros((nb_ela_file,stack_max))

# store the values of phi evolution and std(phi)
phi = np.zeros((nb_ela_file,stack_max))
std_phi = np.zeros((nb_ela_file,stack_max))

# Store the values of elastic properties + uncertainty
mod1_ela = np.zeros((nb_ela_file,stack_max))
mod2_ela = np.zeros((nb_ela_file,stack_max))
dmod1_ela = np.zeros((nb_ela_file,stack_max))
dmod2_ela = np.zeros((nb_ela_file,stack_max))

# Store the values for each stacks of the shear modulus and the bulk modulus #
# stack 1
# stoer elastic properties value and associated std
mod1_ela_1 = np.zeros((nb_ela_file,2)) # bulk modulus or young modulus
mod2_ela_1 = np.zeros((nb_ela_file,2)) # shear modulus

# stack 2
mod1_ela_2 = np.zeros((nb_ela_file,2)) # bulk modulus or young modulus
mod2_ela_2 = np.zeros((nb_ela_file,2)) # shear modulus

# stack 3
mod1_ela_3 = np.zeros((nb_ela_file,2)) # bulk modulus or young modulus
mod2_ela_3 = np.zeros((nb_ela_file,2)) # shear modulus

# stack 4
mod1_ela_4 = np.zeros((nb_ela_file,2)) # bulk modulus or young modulus
mod2_ela_4 = np.zeros((nb_ela_file,2)) # shear modulus

# stack 5
mod1_ela_5 = np.zeros((nb_ela_file,2)) # bulk modulus or young modulus
mod2_ela_5 = np.zeros((nb_ela_file,2)) # shear modulus

# stack 6
mod1_ela_6 = np.zeros((nb_ela_file,2)) # bulk modulus or young modulus
mod2_ela_6 = np.zeros((nb_ela_file,2)) # shear modulus

# stack 7
mod1_ela_7 = np.zeros((nb_ela_file,2)) # bulk modulus or young modulus
mod2_ela_7 = np.zeros((nb_ela_file,2)) # shear modulus

# stack 8
mod1_ela_8 = np.zeros((nb_ela_file,2)) # bulk modulus or young modulus
mod2_ela_8 = np.zeros((nb_ela_file,2)) # shear modulus

# stack 9
mod1_ela_9 = np.zeros((nb_ela_file,2)) # bulk modulus or young modulus
mod2_ela_9 = np.zeros((nb_ela_file,2)) # shear modulus

# stack 10
mod1_ela_10 = np.zeros((nb_ela_file,2)) # bulk modulus or young modulus
mod2_ela_10 = np.zeros((nb_ela_file,2)) # shear modulus

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

# Creation of variable to store ela_comp_N.txt/ela_cis_N.txt files values #
if need_ela == 'yes':
    gamma_0 = np.zeros((nb_ela_file,stack))

    # stack 1
    val_ela_comp_1_1 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_1_2 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_1_3 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_1_4 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_1_5 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_1_6 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_1_7 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_1_8 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_1_9 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_1_10 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_1_11 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_1_12 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_1_13 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_1_14 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_1_15 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_1_16 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_1_17 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_1_18 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_1_19 = np.zeros((line_ela_comp,col_ela_comp))

    val_ela_cis_1_1 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_1_2 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_1_3 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_1_4 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_1_5 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_1_6 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_1_7 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_1_8 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_1_9 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_1_10 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_1_11 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_1_12 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_1_13 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_1_14 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_1_15 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_1_16 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_1_17 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_1_18 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_1_19 = np.zeros((line_ela_cis,col_ela_cis))

    # stack 2
    val_ela_comp_2_1 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_2_2 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_2_3 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_2_4 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_2_5 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_2_6 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_2_7 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_2_8 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_2_9 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_2_10 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_2_11 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_2_12 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_2_13 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_2_14 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_2_15 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_2_16 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_2_17 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_2_18 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_2_19 = np.zeros((line_ela_comp,col_ela_comp))

    val_ela_cis_2_1 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_2_2  = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_2_3 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_2_4 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_2_5 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_2_6 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_2_7 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_2_8 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_2_9 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_2_10 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_2_11 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_2_12 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_2_13 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_2_14 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_2_15 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_2_16 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_2_17 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_2_18 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_2_19 = np.zeros((line_ela_cis,col_ela_cis))

    # stack 3
    val_ela_comp_3_1 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_3_2 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_3_3 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_3_4 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_3_5 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_3_6 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_3_7 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_3_8 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_3_9 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_3_10 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_3_11 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_3_12 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_3_13 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_3_14 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_3_15 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_3_16 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_3_17 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_3_18 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_3_19 = np.zeros((line_ela_comp,col_ela_comp))

    val_ela_cis_3_1 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_3_2 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_3_3 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_3_4 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_3_5 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_3_6 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_3_7 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_3_8 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_3_9 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_3_10 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_3_11 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_3_12 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_3_13 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_3_14 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_3_15 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_3_16 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_3_17 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_3_18 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_3_19 = np.zeros((line_ela_cis,col_ela_cis))

    # stack 4
    val_ela_comp_4_1 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_4_2 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_4_3 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_4_4 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_4_5 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_4_6 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_4_7 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_4_8 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_4_9 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_4_10 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_4_11 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_4_12 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_4_13 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_4_14 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_4_15 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_4_16 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_4_17 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_4_18 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_4_19 = np.zeros((line_ela_comp,col_ela_comp))

    val_ela_cis_4_1 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_4_2 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_4_3 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_4_4 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_4_5 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_4_6 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_4_7 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_4_8 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_4_9 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_4_10 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_4_11 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_4_12 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_4_13 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_4_14 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_4_15 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_4_16 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_4_17 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_4_18 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_4_19 = np.zeros((line_ela_cis,col_ela_cis))

    # stack 5
    val_ela_comp_5_1 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_5_2 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_5_3 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_5_4 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_5_5 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_5_6 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_5_7 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_5_8 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_5_9 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_5_10 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_5_11 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_5_12 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_5_13 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_5_14 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_5_15 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_5_16 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_5_17 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_5_18 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_5_19 = np.zeros((line_ela_comp,col_ela_comp))

    val_ela_cis_5_1 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_5_2 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_5_3 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_5_4 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_5_5 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_5_6 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_5_7 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_5_8 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_5_9 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_5_10 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_5_11 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_5_12 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_5_13 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_5_14 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_5_15 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_5_16 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_5_17 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_5_18 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_5_19 = np.zeros((line_ela_cis,col_ela_cis))

    # stack 6
    val_ela_comp_6_1 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_6_2 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_6_3 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_6_4 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_6_5 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_6_6 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_6_7 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_6_8 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_6_9 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_6_10 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_6_11 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_6_12 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_6_13 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_6_14 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_6_15 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_6_16 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_6_17 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_6_18 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_6_19 = np.zeros((line_ela_comp,col_ela_comp))

    val_ela_cis_6_1 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_6_2 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_6_3 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_6_4 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_6_5 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_6_6 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_6_7 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_6_8 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_6_9 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_6_10 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_6_11 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_6_12 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_6_13 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_6_14 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_6_15 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_6_16 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_6_17 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_6_18 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_6_19 = np.zeros((line_ela_cis,col_ela_cis))

    # stack 7
    val_ela_comp_7_1 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_7_2 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_7_3 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_7_4 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_7_5 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_7_6 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_7_7 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_7_8 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_7_9 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_7_10 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_7_11 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_7_12 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_7_13 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_7_14 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_7_15 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_7_16 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_7_17 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_7_18 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_7_19 = np.zeros((line_ela_comp,col_ela_comp))

    val_ela_cis_7_1 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_7_2  = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_7_3 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_7_4 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_7_5 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_7_6 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_7_7 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_7_8 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_7_9 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_7_10 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_7_11 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_7_12 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_7_13 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_7_14 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_7_15 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_7_16 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_7_17 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_7_18 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_7_19 = np.zeros((line_ela_cis,col_ela_cis))

    # stack 8
    val_ela_comp_8_1 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_8_2 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_8_3 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_8_4 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_8_5 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_8_6 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_8_7 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_8_8 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_8_9 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_8_10 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_8_11 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_8_12 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_8_13 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_8_14 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_8_15 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_8_16 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_8_17 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_8_18 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_8_19 = np.zeros((line_ela_comp,col_ela_comp))

    val_ela_cis_8_1 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_8_2 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_8_3 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_8_4 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_8_5 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_8_6 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_8_7 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_8_8 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_8_9 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_8_10 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_8_11 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_8_12 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_8_13 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_8_14 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_8_15 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_8_16 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_8_17 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_8_18 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_8_19 = np.zeros((line_ela_cis,col_ela_cis))

    # stack 9
    val_ela_comp_9_1 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_9_2 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_9_3 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_9_4 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_9_5 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_9_6 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_9_7 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_9_8 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_9_9 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_9_10 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_9_11 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_9_12 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_9_13 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_9_14 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_9_15 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_9_16 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_9_17 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_9_18 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_9_19 = np.zeros((line_ela_comp,col_ela_comp))

    val_ela_cis_9_1 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_9_2 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_9_3 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_9_4 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_9_5 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_9_6 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_9_7 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_9_8 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_9_9 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_9_10 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_9_11 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_9_12 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_9_13 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_9_14 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_9_15 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_9_16 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_9_17 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_9_18 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_9_19 = np.zeros((line_ela_cis,col_ela_cis))

    # stack 10
    val_ela_comp_10_1 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_10_2 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_10_3 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_10_4 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_10_5 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_10_6 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_10_7 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_10_8 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_10_9 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_10_10 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_10_11 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_10_12 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_10_13 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_10_14 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_10_15 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_10_16 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_10_17 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_10_18 = np.zeros((line_ela_comp,col_ela_comp))
    val_ela_comp_10_19 = np.zeros((line_ela_comp,col_ela_comp))

    val_ela_cis_10_1 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_10_2 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_10_3 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_10_4 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_10_5 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_10_6 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_10_7 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_10_8 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_10_9 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_10_10 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_10_11 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_10_12 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_10_13 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_10_14 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_10_15 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_10_16 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_10_17 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_10_18 = np.zeros((line_ela_cis,col_ela_cis))
    val_ela_cis_10_19 = np.zeros((line_ela_cis,col_ela_cis))
# end of if

# Initialise the damage matrix
dam_G = np.zeros((nb_ela_file,stack_max)) # store the shear modulus damage of all the stacks
dam_G_std = np.zeros((nb_ela_file,stack_max))# store the std of shear modulus damage of all the stacks

dam_K = np.zeros((nb_ela_file,stack_max)) # store the bulk modulus damage of all the stacks
dam_K_std = np.zeros((nb_ela_file,stack_max))# store the std of bulk modulus damage of all the stacks

    ## Extraction of the data file and plot the curves ##
# Sort the log.lammps file
for num_simu in range(1,stack+1): # number of num_simu of simulation
    path = f"/home/rigottia/Nextcloud/Documents/{stacks_file}/simu_{num_simu}"
    if need_prep == 'yes' :
        # Simple shear test data extraction #
        if num_simu == 1 : # stack 1
            val_relax1 = rf.file_data_relax(line_relax,path,num_simu)
            val_precomp1 = rf.file_data_pre_comp(path, num_simu)
        if num_simu == 2 : # stack 2
            val_relax2 = rf.file_data_relax(line_relax,path,num_simu)
            val_precomp2 = rf.file_data_pre_comp(path, num_simu)
        if num_simu == 3 : # stack 3
            val_relax3 = rf.file_data_relax(line_relax,path,num_simu)
            val_precomp3 = rf.file_data_pre_comp(path, num_simu)
        if num_simu == 4 : # stack 4
            val_relax4 = rf.file_data_relax(line_relax,path,num_simu)
            val_precomp4 = rf.file_data_pre_comp(path, num_simu)
        if num_simu == 5 : # stack 5
            val_relax5 = rf.file_data_relax(line_relax,path,num_simu)
            val_precomp5 = rf.file_data_pre_comp(path, num_simu)
        if num_simu == 6 : # stack 6
            val_relax6 = rf.file_data_relax(line_relax,path,num_simu)
            val_precomp6 = rf.file_data_pre_comp(path, num_simu)
        if num_simu == 7 : # stack 7
            val_relax7 = rf.file_data_relax(line_relax,path,num_simu)
            val_precomp7 = rf.file_data_pre_comp(path, num_simu)
        if num_simu == 8 : # stack 8
            val_relax8 = rf.file_data_relax(line_relax,path,num_simu)
            val_precomp8 = rf.file_data_pre_comp(path, num_simu)
        if num_simu == 9 : # stack 9
            val_relax9 = rf.file_data_relax(line_relax,path,num_simu)
            val_precomp9 = rf.file_data_pre_comp(path, num_simu)
        if num_simu == 10 : # stack 10
            val_relax10 = rf.file_data_relax(line_relax,path,num_simu)
            val_precomp10 = rf.file_data_pre_comp(path, num_simu)
        # end if
    # end if

    if need_sh == 'yes' :
        print("\n", "num_simu = ", num_simu, "\n")
        # Simple shear test data extraction #
        if num_simu == 1 : # stack 1
            val_1 = rf.file_data(line,path,num_simu,shear_stress,dg_dt[num_simu-1]) # num_simu 1
            fin_val[:,num_simu-1] = rf.final_value(val_1)

        elif num_simu == 2 : # stack 2
            val_2 = rf.file_data(line,path,num_simu,shear_stress,dg_dt[num_simu-1]) # num_simu 2
            fin_val[:,num_simu-1] = rf.final_value(val_2)

        elif num_simu == 3 : # stack 3
            val_3 = rf.file_data(line,path,num_simu,shear_stress,dg_dt[num_simu-1]) # num_simu 3
            fin_val[:,num_simu-1] = rf.final_value(val_3)

        elif num_simu == 4 : # stack 4
            val_4 = rf.file_data(line,path,num_simu,shear_stress,dg_dt[num_simu-1]) # num_simu 4
            fin_val[:,num_simu-1] = rf.final_value(val_4)

        elif num_simu == 5 : # stack 5
            val_5 = rf.file_data(line,path,num_simu,shear_stress,dg_dt[num_simu-1]) # num_simu 5
            fin_val[:,num_simu-1] = rf.final_value(val_5)

        elif num_simu == 6 : # stack 6
            val_6 = rf.file_data(line,path,num_simu,shear_stress,dg_dt[num_simu-1]) # num_simu 1
            fin_val[:,num_simu-1] = rf.final_value(val_6)

        elif num_simu == 7 : # stack 7
            val_7 = rf.file_data(line,path,num_simu,shear_stress,dg_dt[num_simu-1]) # num_simu 2
            fin_val[:,num_simu-1] = rf.final_value(val_7)

        elif num_simu == 8 : # stack 8
            val_8 = rf.file_data(line,path,num_simu,shear_stress,dg_dt[num_simu-1]) # num_simu 3
            fin_val[:,num_simu-1] = rf.final_value(val_8)

        elif num_simu == 9 : # stack 9
            val_9 = rf.file_data(line,path,num_simu,shear_stress,dg_dt[num_simu-1]) # num_simu 4
            fin_val[:,num_simu-1] = rf.final_value(val_9)

        elif num_simu == 10 : # stack 10
            val_10 = rf.file_data(line,path,num_simu,shear_stress,dg_dt[num_simu-1]) # num_simu 5
            fin_val[:,num_simu-1] = rf.final_value(val_10)
        # end if
    # end if

    # Biaxial oscillatory compression/ shear strain oscillatory test  data extraction #
    if need_ela == 'yes' :
        if need_sh != 'yes':
            print("\n", "num_simu = ", num_simu, "\n")
        # end if

        for no_ela_file in range(nb_ela_file): # counter of the no of the ela file
            print("ela_file = ", no_ela_file+1)
            if num_simu == 1 :
                if no_ela_file == 0 :
                    val_ela_comp_1_1 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_1_1 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    # Extract elastic bulk and shear modulus / young  modulus, poisson coefficient and shearm modulus
                    mod1_ela_1[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_1[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 1 :
                    val_ela_comp_1_2 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_1_2 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_1[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_1[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 2 :
                    val_ela_comp_1_3 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_1_3 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_1[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_1[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 3 :
                    val_ela_comp_1_4 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_1_4 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_1[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_1[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 4 :
                    val_ela_comp_1_5 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_1_5 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_1[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_1[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 5 :
                    val_ela_comp_1_6 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_1_6 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_1[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_1[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 6 :
                    val_ela_comp_1_7 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_1_7 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_1[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_1[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 7 :
                    val_ela_comp_1_8 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_1_8 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_1[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_1[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 8 :
                    val_ela_comp_1_9 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_1_9 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_1[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_1[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 9 :
                    val_ela_comp_1_10 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_1_10 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_1[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_1[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 10 :
                    val_ela_comp_1_11 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_1_11 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_1[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_1[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 11 :
                    val_ela_comp_1_12 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_1_12 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_1[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_1[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 12 :
                    val_ela_comp_1_13 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_1_13 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_1[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_1[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 13 :
                    val_ela_comp_1_14 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_1_14 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_1[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_1[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 14 :
                    val_ela_comp_1_15 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_1_15 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_1[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_1[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 15 :
                    val_ela_comp_1_16 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_1_16 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_1[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_1[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 16 :
                    val_ela_comp_1_17 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_1_17 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_1[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_1[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 17 :
                    val_ela_comp_1_18 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_1_18 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_1[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_1[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 18 :
                    val_ela_comp_1_19 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_1_19 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_1[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_1[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

            elif num_simu == 2 :
                if no_ela_file == 0 :
                    val_ela_comp_2_1 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_2_1 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    # Extract elastic bulk and shear modulus / young  modulus, poisson coefficient and shearm modulus
                    mod1_ela_2[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_2[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 1 :
                    val_ela_comp_2_2 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_2_2 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_2[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_2[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 2 :
                    val_ela_comp_2_3 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_2_3 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_2[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_2[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 3 :
                    val_ela_comp_2_4 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_2_4 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_2[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_2[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 4 :
                    val_ela_comp_2_5 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_2_5 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_2[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_2[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 5 :
                    val_ela_comp_2_6 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_2_6 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_2[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_2[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 6 :
                    val_ela_comp_2_7 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_2_7 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_2[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_2[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 7 :
                    val_ela_comp_2_8 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_2_8 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_2[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_2[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 8 :
                    val_ela_comp_2_9 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_2_9 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_2[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_2[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 9 :
                    val_ela_comp_2_10 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_2_10 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_2[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_2[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 10 :
                    val_ela_comp_2_11 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_2_11 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_2[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_2[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 11 :
                    val_ela_comp_2_12 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_2_12 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_2[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_2[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 12 :
                    val_ela_comp_2_13 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_2_13 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_2[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_2[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 13 :
                    val_ela_comp_2_14 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_2_14 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_2[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_2[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 14 :
                    val_ela_comp_2_15 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_2_15 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_2[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_2[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 15 :
                    val_ela_comp_2_16 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_2_16 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_2[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_2[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 16 :
                    val_ela_comp_2_17 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_2_17 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_2[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_2[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 17 :
                    val_ela_comp_2_18 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_2_18 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_2[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_2[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 18 :
                    val_ela_comp_2_19 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_2_19 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_2[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_2[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

            elif num_simu == 3 :
                if no_ela_file == 0 :
                    val_ela_comp_3_1 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_3_1 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    # Extract elastic bulk and shear modulus / young  modulus, poisson coefficient and shearm modulus
                    mod1_ela_3[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_3[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 1 :
                    val_ela_comp_3_2 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_3_2 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_3[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_3[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 2 :
                    val_ela_comp_3_3 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_3_3 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_3[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_3[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 3 :
                    val_ela_comp_3_4 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_3_4 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_3[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_3[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 4 :
                    val_ela_comp_3_5 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_3_5 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_3[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_3[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 5 :
                    val_ela_comp_3_6 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_3_6 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_3[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_3[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 6 :
                    val_ela_comp_3_7 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_3_7 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_3[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_3[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 7 :
                    val_ela_comp_3_8 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_3_8 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_3[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_3[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 8 :
                    val_ela_comp_3_9 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_3_9 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_3[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_3[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 9 :
                    val_ela_comp_3_10 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_3_10 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_3[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_3[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 10 :
                    val_ela_comp_3_11 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_3_11 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_3[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_3[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 11 :
                    val_ela_comp_3_12 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_3_12 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_3[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_3[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 12 :
                    val_ela_comp_3_13 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_3_13 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_3[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_3[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 13 :
                    val_ela_comp_3_14 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_3_14 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_3[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_3[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 14 :
                    val_ela_comp_3_15 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_3_15 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_3[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_3[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 15 :
                    val_ela_comp_3_16 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_3_16 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_3[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_3[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 16 :
                    val_ela_comp_3_17 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_3_17 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_3[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_3[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 17 :
                    val_ela_comp_3_18 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_3_18 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_3[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_3[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 18 :
                    val_ela_comp_3_19 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_3_19 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_3[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_3[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

            elif num_simu == 4 :
                if no_ela_file == 0 :
                    val_ela_comp_4_1 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_4_1 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    # Extract elastic bulk and shear modulus / young  modulus, poisson coefficient and shearm modulus
                    mod1_ela_4[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_4[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 1 :
                    val_ela_comp_4_2 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_4_2 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_4[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_4[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 2 :
                    val_ela_comp_4_3 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_4_3 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_4[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_4[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 3 :
                    val_ela_comp_4_4 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_4_4 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_4[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_4[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 4 :
                    val_ela_comp_4_5 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_4_5 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_4[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_4[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 5 :
                    val_ela_comp_4_6 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_4_6 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_4[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_4[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 6 :
                    val_ela_comp_4_7 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_4_7 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_4[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_4[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 7 :
                    val_ela_comp_4_8 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_4_8 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_4[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_4[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 8 :
                    val_ela_comp_4_9 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_4_9 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_4[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_4[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 9 :
                    val_ela_comp_4_10 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_4_10 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_4[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_4[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 10 :
                    val_ela_comp_4_11 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_4_11 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_4[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_4[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 11 :
                    val_ela_comp_4_12 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_4_12 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_4[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_4[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 12 :
                    val_ela_comp_4_13 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_4_13 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_4[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_4[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 13 :
                    val_ela_comp_4_14 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_4_14 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_4[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_4[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 14 :
                    val_ela_comp_4_15 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_4_15 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_4[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_4[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 15 :
                    val_ela_comp_4_16 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_4_16 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_4[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_4[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 16 :
                    val_ela_comp_4_17 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_4_17 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_4[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_4[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 17 :
                    val_ela_comp_4_18 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_4_18 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_4[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_4[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 18 :
                    val_ela_comp_4_19 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_4_19 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_4[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_4[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

            elif num_simu == 5 :
                if no_ela_file == 0 :
                    val_ela_comp_5_1 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_5_1 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    # Extract elastic bulk and shear modulus / young  modulus, poisson coefficient and shearm modulus
                    mod1_ela_5[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_5[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 1 :
                    val_ela_comp_5_2 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_5_2 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_5[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_5[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 2 :
                    val_ela_comp_5_3 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_5_3 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_5[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_5[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 3 :
                    val_ela_comp_5_4 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_5_4 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_5[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_5[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 4 :
                    val_ela_comp_5_5 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_5_5 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_5[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_5[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 5 :
                    val_ela_comp_5_6 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_5_6 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_5[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_5[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 6 :
                    val_ela_comp_5_7 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_5_7 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_5[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_5[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 7 :
                    val_ela_comp_5_8 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_5_8 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_5[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_5[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 8 :
                    val_ela_comp_5_9 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_5_9 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_5[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_5[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 9 :
                    val_ela_comp_5_10 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_5_10 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_5[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_5[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 10 :
                    val_ela_comp_5_11 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_5_11 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_5[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_5[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 11 :
                    val_ela_comp_5_12 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_5_12 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_5[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_5[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 12 :
                    val_ela_comp_5_13 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_5_13 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_5[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_5[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 13 :
                    val_ela_comp_5_14 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_5_14 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_5[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_5[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 14 :
                    val_ela_comp_5_15 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_5_15 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_5[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_5[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 15 :
                    val_ela_comp_5_16 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_5_16 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_5[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_5[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 16 :
                    val_ela_comp_5_17 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_5_17 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_5[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_5[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 17 :
                    val_ela_comp_5_18 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_5_18 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_5[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_5[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 18 :
                    val_ela_comp_5_19 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_5_19 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_5[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_5[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

            elif num_simu == 6 :
                if no_ela_file == 0 :
                    val_ela_comp_6_1 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_6_1 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    # Extract elastic bulk and shear modulus / young  modulus, poisson coefficient and shearm modulus
                    mod1_ela_6[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_6[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 1 :
                    val_ela_comp_6_2 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_6_2 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_6[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_6[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 2 :
                    val_ela_comp_6_3 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_6_3 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_6[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_6[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 3 :
                    val_ela_comp_6_4 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_6_4 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_6[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_6[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 4 :
                    val_ela_comp_6_5 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_6_5 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_6[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_6[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 5 :
                    val_ela_comp_6_6 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_6_6 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_6[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_6[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 6 :
                    val_ela_comp_6_7 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_6_7 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_6[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_6[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 7 :
                    val_ela_comp_6_8 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_6_8 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_6[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_6[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 8 :
                    val_ela_comp_6_9 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_6_9 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_6[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_6[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 9 :
                    val_ela_comp_6_10 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_6_10 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_6[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_6[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 10 :
                    val_ela_comp_6_11 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_6_11 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_6[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_6[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 11 :
                    val_ela_comp_6_12 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_6_12 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_6[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_6[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 12 :
                    val_ela_comp_6_13 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_6_13 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_6[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_6[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 13 :
                    val_ela_comp_6_14 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_6_14 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_6[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_6[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 14 :
                    val_ela_comp_6_15 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_6_15 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_6[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_6[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 15 :
                    val_ela_comp_6_16 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_6_16 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_6[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_6[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 16 :
                    val_ela_comp_6_17 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_6_17 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_6[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_6[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 17 :
                    val_ela_comp_6_18 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_6_18 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_6[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_6[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 18 :
                    val_ela_comp_6_19 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_6_19 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_6[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_6[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

            elif num_simu == 7 :
                if no_ela_file == 0 :
                    val_ela_comp_7_1 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_7_1 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    # Extract elastic bulk and shear modulus / young  modulus, poisson coefficient and shearm modulus
                    mod1_ela_7[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_7[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 1 :
                    val_ela_comp_7_2 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_7_2 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_7[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_7[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 2 :
                    val_ela_comp_7_3 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_7_3 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_7[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_7[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 3 :
                    val_ela_comp_7_4 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_7_4 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_7[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_7[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 4 :
                    val_ela_comp_7_5 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_7_5 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_7[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_7[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 5 :
                    val_ela_comp_7_6 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_7_6 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_7[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_7[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 6 :
                    val_ela_comp_7_7 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_7_7 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_7[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_7[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 7 :
                    val_ela_comp_7_8 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_7_8 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_7[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_7[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 8 :
                    val_ela_comp_7_9 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_7_9 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_7[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_7[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 9 :
                    val_ela_comp_7_10 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_7_10 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_7[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_7[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 10 :
                    val_ela_comp_7_11 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_7_11 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_7[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_7[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 11 :
                    val_ela_comp_7_12 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_7_12 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_7[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_7[no_ela_file,:], gamma_0[no_ela_file,num_simu-1] = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 12 :
                    val_ela_comp_7_13 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_7_13 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_7[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_7[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 13 :
                    val_ela_comp_7_14 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_7_14 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_7[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_7[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 14 :
                    val_ela_comp_7_15 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_7_15 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_7[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_7[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 15 :
                    val_ela_comp_7_16 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_7_16 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_7[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_7[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 16 :
                    val_ela_comp_7_17 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_7_17 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_7[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_7[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 17 :
                    val_ela_comp_7_18 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_7_18 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_7[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_7[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 18 :
                    val_ela_comp_7_19 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_7_19 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_7[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_7[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

            elif num_simu == 8 :
                if no_ela_file == 0 :
                    val_ela_comp_8_1 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_8_1 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    # Extract elastic bulk and shear modulus / young  modulus, poisson coefficient and shearm modulus
                    mod1_ela_8[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_8[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 1 :
                    val_ela_comp_8_2 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_8_2 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_8[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_8[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 2 :
                    val_ela_comp_8_3 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_8_3 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_8[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_8[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 3 :
                    val_ela_comp_8_4 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_8_4 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_8[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_8[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 4 :
                    val_ela_comp_8_5 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_8_5 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_8[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_8[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 5 :
                    val_ela_comp_8_6 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_8_6 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_8[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_8[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 6 :
                    val_ela_comp_8_7 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_8_7 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_8[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_8[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 7 :
                    val_ela_comp_8_8 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_8_8 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_8[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_8[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 8 :
                    val_ela_comp_8_9 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_8_9 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_8[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_8[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 9 :
                    val_ela_comp_8_10 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_8_10 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_8[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_8[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 10 :
                    val_ela_comp_8_11 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_8_11 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_8[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_8[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 11 :
                    val_ela_comp_8_12 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_8_12 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_8[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_8[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 12 :
                    val_ela_comp_8_13 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_8_13 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_8[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_8[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 13 :
                    val_ela_comp_8_14 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_8_14 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_8[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_8[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 14 :
                    val_ela_comp_8_15 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_8_15 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_8[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_8[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 15 :
                    val_ela_comp_8_16 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_8_16 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_8[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_8[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 16 :
                    val_ela_comp_8_17 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_8_17 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_8[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_8[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 17 :
                    val_ela_comp_8_18 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_8_18 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_8[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_8[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 18 :
                    val_ela_comp_8_19 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_8_19 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_8[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_8[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

            elif num_simu == 9 :
                if no_ela_file == 0 :
                    val_ela_comp_9_1 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_9_1 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    # Extract elastic bulk and shear modulus / young  modulus, poisson coefficient and shearm modulus
                    mod1_ela_9[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_9[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 1 :
                    val_ela_comp_9_2 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_9_2 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_9[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_9[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 2 :
                    val_ela_comp_9_3 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_9_3 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_9[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_9[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 3 :
                    val_ela_comp_9_4 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_9_4 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_9[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_9[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 4 :
                    val_ela_comp_9_5 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_9_5 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_9[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_9[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 5 :
                    val_ela_comp_9_6 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_9_6 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_9[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_9[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 6 :
                    val_ela_comp_9_7 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_9_7 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_9[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_9[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 7 :
                    val_ela_comp_9_8 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_9_8 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_9[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_9[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 8 :
                    val_ela_comp_9_9 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_9_9 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_9[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_9[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 9 :
                    val_ela_comp_9_10 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_9_10 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_9[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_9[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 10 :
                    val_ela_comp_9_11 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_9_11 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_9[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_9[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 11 :
                    val_ela_comp_9_12 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_9_12 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_9[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_9[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 12 :
                    val_ela_comp_9_13 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_9_13 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_9[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_9[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 13 :
                    val_ela_comp_9_14 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_9_14 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_9[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_9[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 14 :
                    val_ela_comp_9_15 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_9_15 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_9[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_9[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 15 :
                    val_ela_comp_9_16 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_9_16 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_9[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_9[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 16 :
                    val_ela_comp_9_17 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_9_17 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_9[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_9[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 17 :
                    val_ela_comp_9_18 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_9_18 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_9[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_9[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 18 :
                    val_ela_comp_9_19 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_9_19 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_9[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_9[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

            elif num_simu == 10 :
                if no_ela_file == 0 :
                    val_ela_comp_10_1 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_60_1 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    # Extract elastic bulk and shear modulus / young  modulus, poisson coefficient and shearm modulus
                    mod1_ela_10[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_10[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 1 :
                    val_ela_comp_10_2 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_60_2 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_10[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_10[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 2 :
                    val_ela_comp_10_3 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_60_3 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_10[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_10[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 3 :
                    val_ela_comp_10_4 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_60_4 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_10[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_10[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 4 :
                    val_ela_comp_10_5 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_60_5 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_10[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_10[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 5 :
                    val_ela_comp_10_6 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_60_6 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_10[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_10[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 6 :
                    val_ela_comp_10_7 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_60_7 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_10[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_10[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 7 :
                    val_ela_comp_10_8 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_60_8 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_10[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_10[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 8 :
                    val_ela_comp_10_9 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_60_9 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_10[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_10[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 9 :
                    val_ela_comp_10_10 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_60_10 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_10[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_10[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 10 :
                    val_ela_comp_10_11 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_60_11 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_10[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_10[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 11 :
                    val_ela_comp_10_12 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_60_12 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_10[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_10[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 12 :
                    val_ela_comp_10_13 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_60_13 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_10[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_10[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 13 :
                    val_ela_comp_10_14 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_60_14 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_10[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_10[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 14 :
                    val_ela_comp_10_15 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_60_15 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_10[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_10[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 15 :
                    val_ela_comp_10_16 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_60_16 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_10[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_10[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 16 :
                    val_ela_comp_10_17 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_60_17 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_10[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_10[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 17 :
                    val_ela_comp_10_18 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_60_18 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_10[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_10[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

                elif no_ela_file == 18 :
                    val_ela_comp_10_19 = rf.file_ela_comp_data(no_ela_file+1,line_ela_comp,path)
                    val_ela_cis_60_19 = rf.file_ela_cis_data(no_ela_file+1,line_ela_cis,path)

                    mod1_ela_10[no_ela_file,:] = rf.file_K_data(no_ela_file+1,line_ela_comp,path,zoom)
                    mod2_ela_10[no_ela_file,:] , gamma_0[no_ela_file,num_simu-1]  = rf.file_G_data(no_ela_file+1,line_ela_cis,dg_dt[num_simu-1],path,zoom)

    if need_d == 'yes':
        # Bulk modulus
        mod1_ela = rf.ela_matrix(mod1_ela_1, mod1_ela_2, mod1_ela_3, mod1_ela_4, mod1_ela_5, mod1_ela_6, mod1_ela_7, mod1_ela_8, mod1_ela_9, mod1_ela_10, nb_ela_file,'elastic modulus',stack_max)
        dmod1_ela = rf.ela_matrix(mod1_ela_1, mod1_ela_2, mod1_ela_3, mod1_ela_4, mod1_ela_5, mod1_ela_6, mod1_ela_7, mod1_ela_8, mod1_ela_9, mod1_ela_10, nb_ela_file,'std',stack_max)

        # Shear modulus
        mod2_ela = rf.ela_matrix(mod2_ela_1, mod2_ela_2, mod2_ela_3, mod2_ela_4, mod2_ela_5, mod2_ela_6, mod2_ela_7, mod2_ela_8, mod2_ela_9, mod2_ela_10, nb_ela_file,'elastic modulus',stack_max)
        dmod2_ela = rf.ela_matrix(mod2_ela_1, mod2_ela_2, mod2_ela_3, mod2_ela_4, mod2_ela_5, mod2_ela_6, mod2_ela_7, mod2_ela_8, mod2_ela_9, mod2_ela_10, nb_ela_file,'std',stack_max)

        if num_simu == 1 : # stack 1
            d_G1 =  rf.d_comp(nb_ela_file, line_ela_cis, path, press, analyse, 'shear', num_simu, stack_max, zoom, damage_compute)
            d_K1 =  rf.d_comp(nb_ela_file, line_ela_cis, path, press, analyse, 'bulk', num_simu, stack_max, zoom, damage_compute)

        elif num_simu == 2 : # stack 2
            d_G2 =  rf.d_comp(nb_ela_file, line_ela_cis, path, press, analyse, 'shear', num_simu, stack_max,zoom, damage_compute)
            d_K2 =  rf.d_comp(nb_ela_file, line_ela_cis, path, press, analyse, 'bulk', num_simu, stack_max,zoom, damage_compute)

        elif num_simu == 3 : # stack 3
            d_G3 =  rf.d_comp(nb_ela_file, line_ela_cis, path, press, analyse, 'shear', num_simu, stack_max, zoom, damage_compute)
            d_K3 =  rf.d_comp(nb_ela_file, line_ela_cis, path, press, analyse, 'bulk', num_simu, stack_max, zoom, damage_compute)

        elif num_simu == 4 : # stack 4
            d_G4 =  rf.d_comp(nb_ela_file, line_ela_cis, path, press, analyse, 'shear', num_simu, stack_max, zoom, damage_compute)
            d_K4 =  rf.d_comp(nb_ela_file, line_ela_cis, path, press, analyse, 'bulk', num_simu, stack_max, zoom, damage_compute)

        elif num_simu == 5 : # stack 5
            d_G5 =  rf.d_comp(nb_ela_file, line_ela_cis, path, press, analyse, 'shear', num_simu, stack_max, zoom, damage_compute)
            d_K5 =  rf.d_comp(nb_ela_file, line_ela_cis, path, press, analyse, 'bulk', num_simu, stack_max, zoom, damage_compute)

        elif num_simu == 6 : # stack 6
            d_G6 =  rf.d_comp(nb_ela_file, line_ela_cis, path, press, analyse, 'shear', num_simu, stack_max, zoom, damage_compute)
            d_K6 =  rf.d_comp(nb_ela_file, line_ela_cis, path, press, analyse, 'bulk', num_simu, stack_max, zoom, damage_compute)

        elif num_simu == 7 : # stack 7
            d_G7 =  rf.d_comp(nb_ela_file, line_ela_cis, path, press, analyse, 'shear', num_simu, stack_max, zoom, damage_compute)
            d_K7 =  rf.d_comp(nb_ela_file, line_ela_cis, path, press, analyse, 'bulk', num_simu, stack_max, zoom, damage_compute)

        elif num_simu == 8 : # stack 8
            d_G8 =  rf.d_comp(nb_ela_file, line_ela_cis, path, press, analyse, 'shear', num_simu, stack_max, zoom, damage_compute)
            d_K8 =  rf.d_comp(nb_ela_file, line_ela_cis, path, press, analyse, 'bulk', num_simu, stack_max, zoom, damage_compute)

        elif num_simu == 9 : # stack 9
            d_G9 =  rf.d_comp(nb_ela_file, line_ela_cis, path, press, analyse, 'shear', num_simu, stack_max, zoom, damage_compute)
            d_K9 =  rf.d_comp(nb_ela_file, line_ela_cis, path, press, analyse, 'bulk', num_simu, stack_max, zoom, damage_compute)

        elif num_simu == 10 : # stack 10
            d_G10 =  rf.d_comp(nb_ela_file, line_ela_cis, path, press, analyse, 'shear', num_simu, stack_max, zoom, damage_compute)
            d_K10 =  rf.d_comp(nb_ela_file, line_ela_cis, path, press, analyse, 'bulk', num_simu, stack_max, zoom, damage_compute)
        # end if

        dam_K = rf.d_stack(dam_K,d_K1,d_K2,d_K3,d_K4,d_K5,'damage')
        dam_K_std = rf.d_stack(dam_K_std,d_K1,d_K2,d_K3,d_K4,d_K5,'std')
        dam_G = rf.d_stack(dam_G,d_G1,d_G2,d_G3,d_G4,d_G5,'damage')
        dam_G_std = rf.d_stack(dam_G_std,d_G1,d_G2,d_G3,d_G4,d_G5,'std')
    # end if

    # Plateau values extraction
    if num_simu == 1 :
        plt[num_simu-1,:] = rf.sh_plt(val_1,mod2_ela[:,num_simu-1,],dmod2_ela[:,num_simu-1],d_G1,d_G2,d_G3,d_G4,d_G5,d_K1,d_K2,d_K3,d_K4,d_K5,num_simu,16,line)

    if num_simu == 2 :
        plt[num_simu-1,:] = rf.sh_plt(val_2,mod2_ela[:,num_simu-1],dmod2_ela[:,num_simu-1],d_G1,d_G2,d_G3,d_G4,d_G5,d_K1,d_K2,d_K3,d_K4,d_K5,num_simu,16,line)

    if num_simu == 3 :
        plt[num_simu-1,:] = rf.sh_plt(val_3,mod2_ela[:,num_simu-1],dmod2_ela[:,num_simu-1],d_G1,d_G2,d_G3,d_G4,d_G5,d_K1,d_K2,d_K3,d_K4,d_K5,num_simu,16,line)

    if num_simu == 4 :
        plt[num_simu-1,:] = rf.sh_plt(val_4,mod2_ela[:,num_simu-1],dmod2_ela[:,num_simu-1],d_G1,d_G2,d_G3,d_G4,d_G5,d_K1,d_K2,d_K3,d_K4,d_K5,num_simu,16,line)

    if num_simu == 5 :
        plt[num_simu-1,:] = rf.sh_plt(val_5,mod2_ela[:,num_simu-1],dmod2_ela[:,num_simu-1],d_G1,d_G2,d_G3,d_G4,d_G5,d_K1,d_K2,d_K3,d_K4,d_K5,num_simu,16,line)
    # end if
# end of for loop #

# Search index of the rheological regims
regimes, regimes_disc = rf.simu_phase(val_1, val_2, val_3, val_4, val_5, val_6, val_7, val_8, val_9, val_10, stack, stack_max, line)

# Elastic properties matrix
mod1_ela = rf.adim_ela(mod1_ela, dmod1_ela, val_1, val_2, val_3, val_4, val_5, val_6, val_7, val_8, val_9, val_10, stack, analyse, E, 'ela',stack_max)
mod2_ela = rf.adim_ela(mod2_ela, dmod2_ela, val_1, val_2, val_3, val_4, val_5, val_6, val_7, val_8, val_9, val_10, stack, analyse, E, 'ela',stack_max)

dmod1_ela = rf.adim_ela(mod1_ela, dmod1_ela, val_1, val_2, val_3, val_4, val_5, val_6, val_7, val_8, val_9, val_10, stack, analyse, E, 'std',stack_max)
dmod2_ela = rf.adim_ela(mod1_ela, dmod2_ela, val_1, val_2, val_3, val_4, val_5, val_6, val_7, val_8, val_9, val_10, stack, analyse, E, 'std',stack_max)

# Simple shear matrix
val_1,val_2,val_3,val_4,val_5,val_6,val_7,val_8,val_9,val_10 = rf.adim_cis(val_1, val_2, val_3, val_4, val_5, val_6, val_7, val_8, val_9, val_10, analyse, E)

# Output of data treatment
if need_sh == 'yes':
    print("\n", "Variable measured", "\n", "[\u03c4 std(\u03c4) P std(P) \u03d5 std(\u03d5) Z std(Z) Z_min std(Z_min) \u03c4_max std(\u03c4_max) d(G) std(d_G) d(K) std(d_K)]" )
    print(plt[:])
    print("\n", "fin_val measured", "\n", "\u03b3    \u03b5_vol    \u03c4    P")
    print(fin_val[:,:])
    print("\n")
# end if

if need_d == 'yes' :
    print("G = ", mod2_ela, "\n")
    print("\n", "K = ", mod1_ela, "\n")
# end if

# save the matrix of variable measured
if save_variable == 'yes':
    S_xy = rf.variable_matrix(val_1, val_2, val_3, val_4, val_5, nb_ela_file, stack, stack_max, line, preparation, stress, 's_xy')
    std_S_xy = rf.variable_matrix(val_1, val_2, val_3, val_4, val_5, nb_ela_file, stack, stack_max, line, preparation, stress, 'std_s_xy')
    pression = rf.variable_matrix(val_1, val_2, val_3, val_4, val_5, nb_ela_file, stack, stack_max, line, preparation, stress, 'press')
    std_press =rf.variable_matrix(val_1, val_2, val_3, val_4, val_5, nb_ela_file, stack, stack_max, line, preparation, stress, 'std_press')
    phi = rf.variable_matrix(val_1, val_2, val_3, val_4, val_5, nb_ela_file, stack, stack_max, line, preparation, stress, 'phi')
    std_phi = rf.variable_matrix(val_1, val_2, val_3, val_4, val_5, nb_ela_file, stack, stack_max, line, preparation, stress, 'std_phi')
    z = rf.variable_matrix(val_1, val_2, val_3, val_4, val_5, nb_ela_file, stack, stack_max, line, preparation, stress, 'z')
    std_z = rf.variable_matrix(val_1, val_2, val_3, val_4, val_5, nb_ela_file, stack, stack_max, line, preparation, stress, 'std_z')

    # save variable for global plot in rheo_plot
    """
    np.savetxt(f'{name_file}_{analyse}.txt', plt[:], fmt='%.2e',header = '\u03c4 std(\u03c4) P std(P) \u03d5 std(\u03d5) Z std(Z) Z_min std(Z_min) \u03c4_max std(\u03c4_max) d(G) std(d_G) d(K) std(d_K)')
    np.savetxt(f'{name_file_phi}_{analyse}.txt', phi[:,:], fmt='%.2e',header = '\u03d5_1 \u03d5_2 \u03d5_3 \u03d5_4 \u03d5_5')
    np.savetxt(f'{name_file_phi}_{analyse}_std.txt', std_phi[:,:], fmt='%.2e',header = 'std(\u03d5_1) std(\u03d5_2) std(\u03d5_3) std(\u03d5_4) std(\u03d5_5)')
    np.savetxt(f'{name_file_z}_{analyse}.txt', z[:,:], fmt ='%.2e',header = 'Z_1 Z_2 Z_3 Z_4 Z_5')
    np.savetxt(f'{name_file_z}_{analyse}_std.txt', std_z[:,:], fmt ='%.2e',header = 'std(Z_1) std(Z_2) std(Z_3) std(Z_4) std(Z_5)')
    """
    np.savetxt(f'{name_file_sh}_{analyse}.txt', S_xy[:,:], fmt ='%.2e',header = 'tau_1 tau_2 tau_3 tau_4 tau_5')
    np.savetxt(f'{name_file_sh}_{analyse}_std.txt', std_S_xy[:,:], fmt ='%.2e',header = 'std(tau_1) std(tau_2) std(tau_3) std(tau_4) std(tau_5)')
    """
    np.savetxt(f'{name_file_pression}_{analyse}.txt', pression[:,:], fmt ='%.2e',header = 'P_1 P_2 P_3 P_4 P_5')
    np.savetxt(f'{name_file_pression}_{analyse}_std.txt', std_press[:,:], fmt ='%.2e',header = 'std(P_1) std(P_2) std(P_3) std(P_4) std(P_5)')

    np.savetxt(f'G_{name_file_ela}_{analyse}.txt', mod2_ela[:], fmt='%.2e', header = 'G_1 (Pa) G_2 (Pa) G_3 (Pa) G_4 (Pa) G_5 (Pa)')
    np.savetxt(f'std(G)_{name_file_ela}_{analyse}.txt', dmod2_ela[:], fmt='%.2e', header = 'std(G_1) (Pa) std(G_2) (Pa) std(G_3) (Pa) std(G_4) (Pa) std(G_5) (Pa)(Pa)')
    np.savetxt(f'K_{name_file_ela}_{analyse}.txt', mod1_ela[:], fmt='%.2e', header = 'K_1 (Pa) K_2 (Pa) K_3 (Pa) K_4 (Pa) K_5 (Pa)')
    np.savetxt(f'std(K)_{name_file_ela}_{analyse}.txt', dmod2_ela[:], fmt='%.2e', header = 'std(K_1) (Pa) std(K_2) (Pa) std(K_3) (Pa) std(K_4) (Pa) std(K_5) (Pa)')

    np.savetxt(f'dam_G_{name_file_ela}_{analyse}.txt', dam_G[:], fmt='%.2e', header = 'd_G_1 d_G_2 d_G_3 d_G_4 d_G_5')
    np.savetxt(f'std(dam_G)_{name_file_ela}_{analyse}.txt', dam_G_std[:], fmt='%.2e', header = 'std(d_G_1) std(d_G_1) std(d_G_2) std(d_G_3) std(d_G_4) std(d_G_5)')
    np.savetxt(f'dam_K_{name_file_ela}_{analyse}.txt', dam_K[:], fmt='%.2e', header = 'd_K_1 d_K_2 d_K_3 d_K_4 d_K_5 d_K_6 d_K_7 d_K_8')
    np.savetxt(f'std(dam_K)_{name_file_ela}_{analyse}.txt', dam_K_std[:], fmt='%.2e', header = 'std(d_K_1) std(d_K_2) std(d_K_3) std(d_K_4) std(d_K_5)')
    """
# end if

if save_ref_mod == 'yes': """
    # save elastic modulii reference state
    np.savetxt(f'G0_{press}_{analyse}.txt', mod2_ela[0], fmt='%.2e', header = 'G0_1 (Pa) G0_2 (Pa) G0_3 (Pa) G0_4 (Pa) G0_5 (Pa)')
    np.savetxt(f'dG0_{press}_{analyse}.txt', dmod2_ela[0], fmt='%.2e', header = 'dG0_1 (Pa) dG0_2 (Pa) dG0_3 (Pa) dG0_4 (Pa) dG0_5 (Pa)')
    np.savetxt(f'K0_{press}_{analyse}.txt', mod1_ela[0], fmt='%.2e', header = 'K0_1 (Pa) K0_2 (Pa) K0_3 (Pa) K0_4 (Pa) K0_5 (Pa)')
    np.savetxt(f'dK0_{press}_{analyse}.txt', dmod1_ela[0], fmt='%.2e', header = 'dK0_1 (Pa) dK0_2 (Pa) dK0_3 (Pa) dK0_4 (Pa) dK0_5 (Pa)')
# end if """

# Values adimensionnement
# !!! creation of the graph !!!
# Shear strain vs shear stress curve + coordination number and packing fraction
if need_prep == 'yes' :
    print('\n', 'Print relaxation plot ? (yes/no)')
    print_relax = input()

    if print_relax == 'yes':
        g.graph_relax(val_relax1,val_relax2,val_relax3,val_relax4,val_relax5,val_relax6,val_relax7,val_relax8,val_relax9,val_relax10,E,t_n,stack,tag1,tag2,tag3,tag4,tag5,tag6,tag7,tag8,tag9,tag10,colormap_g_1,colormap_g_2,analyse)
        g.graph_pre_comp(val_precomp1,val_precomp2,val_precomp3,val_precomp4,val_precomp5,val_precomp6,val_precomp7,val_precomp8,val_precomp9,val_precomp10,E,t_n,stack,tag1,tag2,tag3,tag4,tag5,tag6,tag7,tag8,tag9,tag10,colormap_g_1,colormap_g_2,analyse)
    # end if
# end if

if need_sh == 'yes' :
    print('\n', 'Print shearing plot ? (yes/no)')
    print_sh = input()

    if print_sh == 'yes':
        g.graph_cis(val_1,val_2,val_3,val_4,val_5,val_6,val_7,val_8,val_9,val_10,regimes,t_n,stack,tag1,tag2,tag3,tag4,tag5,tag6,tag7,tag8,tag9,tag10,fin_val,colormap_g_1,colormap_g_2,analyse) # simple shear test
    # end if
# end if

# Oscillatory biaxial compression + oscillatory shearing
if need_ela == 'yes':
    # graph for the oscillatory biaxial compression
    if need_d == 'yes':
        # bulk and shear modulus evolution
        print('\n', 'Print elastic properties plot ? (yes/no)')
        print_ela_prop = input()

        if print_ela_prop == 'yes':
            g.ela_prop_graph(mod1_ela,mod2_ela,dmod1_ela,dmod2_ela,regimes_disc,gamma_0,t_n,stack,tag1,tag2,tag3,tag4,tag5,tag6,tag7,tag8,tag9,tag10,fin_val,colormap_g_1,colormap_g_2,analyse)

        # damage curve
        print('\n', 'Print damage plot ? (yes/no)')
        print_dam = input()

        if print_dam == 'yes':
            g.dam(d_G1,d_G2,d_G3,d_G4,d_G5,d_G6,d_G7,d_G8,d_G9,d_G10,regimes_disc,gamma_0,stack,tag1,tag2,tag3,tag4,tag5,tag6,tag7,tag8,tag9,tag10,fin_val,colormap_g_1,colormap_g_2,'G',analyse)
            g.dam(d_K1,d_K2,d_K3,d_K4,d_K5,d_K6,d_K7,d_K8,d_K9,d_K10,regimes_disc,gamma_0,stack,tag1,tag2,tag3,tag4,tag5,tag6,tag7,tag8,tag9,tag10,fin_val,colormap_g_1,colormap_g_2,'K',analyse)
        # end if
    # end if
# end if

# End