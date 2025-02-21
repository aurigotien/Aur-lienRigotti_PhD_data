## Call all the function defined in the files : ##
## code_modification, random_algo, traitement_log, stack ##

import numpy as np
import math as mt

import random_algo as ini_grain
import code_modification as w_lmp

#import traitement_log as trt

## Variables ##
path = "" # path to find rand_config.lj file
stacks = "stacks"
no_simu = 30 # number of simulations : 30

N = 100 # 10000 # number of grains
rho = 900 # density rho
visc = 0 # viscosity of the simulation to damp dyn effect => max working = 2.5E4 Pa.m.s

#phi_ini = 0.25 => phi ~ 0.82
phi_ini = 0.23 # emprical value to reach phi = aimed packing fraction at the end of the compression

dt = 1E-4 # discretization time for simple shear and relaxations
dt_ela = 1E-6 # discretization time for ela oscil
e_sh = 0.3 # final shear strain

# variable to modify between simulations
num_simu = 114 # number of the stack file to run
shear = 7.5E-6 # imposed shear rate (s^-1)
comp = 5.07E4 # imposed pressure (Pa)
N_restart = round(e_sh /(shear*dt)) # initialise the restart step

# set the restart step
N_restart = w_lmp.restart_set_up(shear) # step of restart for the elastic test test

# Properties
d_m = 100 # moy diam
d_max = round((7/6)*d_m,0) # max diam
d_min = round((5/6)*d_m,0) # min diam
S_m = (mt.pi*(d_m/2)**2)*N # average surface of the N_grains

L = int((S_m/phi_ini)**(1/2)) # length and heigth of the simulation box

v_w = np.zeros(6) # vector velocity and momentum of the grains
diam = np.zeros(N) # vector of the diam of all the grains
x_y = np.zeros((N,3)) # vector with the coordinates x, y, z of the grains

# opening of the fie to copy and edit #
for i in range(no_simu): # scan the N files of a single stack of simulation
    # Path for Computer simulation / OAR simulation
    # Computer simulation
    #"""
    path = f"/home/rigottia/Nextcloud/Documents/{stacks}/simu_{num_simu}/run_{i+1}/simulation"
    path_code = f"/home/rigottia/Nextcloud/Documents/{stacks}/code_copy/prep_simu_{num_simu}/lammps_copy"
    #"""

    # OAR simulation
    """
    path = f"/data/failles/rigottia/Documents/{stacks}/simu_{num_simu}/run_{i+1}/simulation"
    path_code = f"/data/failles/rigottia/Documents/{stacks}/code_copy/prep_simu_{num_simu}/lammps_copy"
    #"""

    # GRICAD simulation
    """
    path = f"/bettik/rigottia/Documents/{stacks}/simu_{num_simu}/run_{i+1}/simulation"
    path_code = f"/bettik/rigottia/Documents/{stacks}/code_copy/prep_simu_{num_simu}/lammps_copy"
    #"""

    print(path) # print the path use
    #os.remove(f"{path}/rand_config.lj") # delete the file rand_config to create a new one
    grains = open(f"{path}/rand_config.lj","w+") # open and create a file rand_config.lj to write position, diameter and velocity of grains

## Beginning ##
# Create a file where the atoms will be mapped
    diam = ini_grain.file_edit(grains,v_w,L,x_y,diam,d_min,d_max,rho,N) # creat a table of grains of random size
    grains.close() # closure of the opened grain file

    print("End of source file copy and edition")
    w_lmp.LAMMPS_files(path,path_code,visc,rho,L,d_min,d_max,diam,N,N_restart,dt,dt_ela,e_sh,shear,comp) # modify thev LAMMPS code and copy it
# end of for loop

## End ##