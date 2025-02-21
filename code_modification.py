import numpy as np # load numpy package
import math as mt # load maths package

def restart_set_up(shear):
    # P ~ 5 kPa
    if shear == 1.2E-4:
         N_restart = 62500
    elif shear == 2.5E-5:
        N_restart = 300000
    elif shear == 1.2E-5:
        N_restart = 625000
    elif shear == 2.5E-6:
        N_restart = 3000000
    elif shear == 1.2E-6:
        N_restart = 6250000

    # P ~ 50 kPa
    elif shear == 3.75E-4:
         N_restart = 20000
    elif shear == 7.5E-5:
        N_restart = 100000
    elif shear == 3.75E-5:
        N_restart = 200000
    elif shear == 7.5E-6:
        N_restart = 1000000
    elif shear == 3.75E-6:
        N_restart = 2000000

    # P ~ 100 kPa
    elif shear == 5E-4:
         N_restart = 15000
    elif shear == 1E-4:
        N_restart = 75000
    elif shear == 5E-5:
        N_restart = 150000
    elif shear == 1E-5:
        N_restart = 750000
    elif shear == 5E-6:
        N_restart = 1500000
    # end if

    else :
        N_restart = 200
    # for mu(I) rheology
    return N_restart

def V_s(d,N): # edit the Initialisation LAMMPS text file to add the surface of the grains
    S_grains = 0 # total surface of the grains
    for i in range(N): # scan the N grains of the simulation
        S_grains += np.pi*(d[i]/2)**2 # compute the grain surface for every grain
    print("S_grains = ", S_grains, "\n") # print the total surface of the grains
    return S_grains # return the value of the surface of the grains

def round_N_restart(N_restart,step):
    # Variables
    restart_step = step # increment of the restart files

    # Computation
    div = N_restart // restart_step
    remain = N_restart % restart_step

    if (remain > restart_step / 2) :
        N_file = round_N_restart(N_restart - remain,step)
    else :
        N_file = mt.ceil(div*restart_step)

    return N_file

def LAMMPS_ini_w(path,path_code,rho,l_ini,d_min,d_max,visc,N_max): # modify Initialisation LAMMPS source code file

    # variable store the string to be modified in the text file
    v_lini = "variable L_INI equal"
    v_ng = "variable N_GRAINS equal"
    v_dmin = "variable DMIN equal"
    v_dmax = "variable DMAX equal"
    v_rho = "variable RHO equal"
    v_visc = "variable VISC equal"
    end_file = "### End of initialisation step ###" # identify the end of the LAMMPS source code file

    # open the source LAMMPS text file and create the text file to be edited
    s_ini_file = open(f"{path_code}/in.floes_initialisation.lmp","r")
    new_ini_file = open(f"{path}/in.floes_initialisation.lmp","w+") # modified LAMMPS file copied

    line = "" # value of the line used to modifed the LAMMPS code

    while(end_file not in line): # search for the end of the source code
         # mofication of the ini file
        line = s_ini_file.readline().strip() # read the line of the source code
        if line == "#variable_N_GRAINS#": # add the number of grain in the new file
            line = f"{v_ng} "+f"{N_max}"
        if line == "#variable_LINI#": # add the initial length of the simulation box in the new file
            line = f"{v_lini} "+f"{l_ini}"
        if line == "#variable_D_MIN#": # add the value of the min diam in the new file
            line = f"{v_dmin} "+f"{d_min}"
        if line == "#variable_D_MAX#": # add the value of the max diam in the new file
            line = f"{v_dmax} "+f"{d_max}"
        if line == "#variable_RHO#": # add the density of the grains in the new file
            line = f"{v_rho} "+f"{rho}"
        if line == "#variable_VISC#": # add the value of viscous damping in the new file
            line = f"{v_visc} "+f"{visc}"

        new_ini_file.write(line+"\n") # write in the new file the char of variable line

    s_ini_file.close() # close the source code file
    new_ini_file.close() # close the new file
    return

def LAMMPS_comp_w(path,path_code,phi): # modify Compression LAMMPS source code file
    end_file = "### End of compression step ###" # identify the end of the LAMMPS source code file

    v_phi = "variable S_GRAINS equal" # surface of the grains value of the granular assembly

    # open the source LAMMPS text file and create the text file to be edited
    s_comp_file = open(f"{path_code}/in.floes_compression.lmp","r")
    new_comp_file = open(f"{path}/in.floes_compression.lmp","w+") # modified LAMMPS file copied

    line = "" # value of the line used to modifed the LAMMPS code

    while(end_file not in line): # search for the end of the source code
        # modification of comp file
        line = s_comp_file.readline().strip() # read the line of the source code
        if line == "#variable_S_GRAINS#":  # add the surface of the grains value in the new file
            line = f"{v_phi} "+f"{phi}"

        new_comp_file.write(line+"\n") # write in the new file the char of variable line
    # end of while loop
    s_comp_file.close() # close the source code file
    new_comp_file.close() # close the new file
    return

def LAMMPS_relax_w(path,path_code,phi): # modify Relaxation LAMMPS source code file
    end_file = "### End of relaxation step ###" # identify the end of the LAMMPS source code file

    v_phi = "variable S_GRAINS equal" # surface of the grains value of the granular assembly

    # open the source LAMMPS text file and create the text file to be edited
    s_relax_file = open(f"{path_code}/in.floes_relaxation.lmp","r")
    new_relax_file = open(f"{path}/in.floes_relaxation.lmp","w+") # modified LAMMPS file copied

    line = "" # value of the line used to modifed the LAMMPS code

    while(end_file not in line): # search for the end of the source code
        # modification of relaxation file
        line = s_relax_file.readline().strip()
        if line == "#variable_S_GRAINS#": # add the surface of the grains value in the new file
            line = f"{v_phi} "+f"{phi}"
        new_relax_file.write(line+"\n") # write in the new file the char of variable line
    # end of while loop

    s_relax_file.close() # close the source code file
    new_relax_file.close() # close the new file
    return

def LAMMPS_precomp_w(path,path_code,phi,comp): # modify Relaxation LAMMPS source code file
    end_file = "### End of precompression step ###" # identify the end of the LAMMPS source code file

    v_phi = "variable S_GRAINS equal" # surface of the grains value of the granular assembly
    v_pre_comp = "variable COMP equal"

    # open the source LAMMPS text file and create the text file to be edited
    s_precomp_file = open(f"{path_code}/in.floes_precomp.lmp","r")
    new_precomp_file = open(f"{path}/in.floes_precomp.lmp","w+") # modified LAMMPS file copied

    line = "" # value of the line used to modifed the LAMMPS code

    while(end_file not in line): # search for the end of the source code
        # modification of relaxation file
        line = s_precomp_file.readline().strip()
        if line == "#variable_S_GRAINS#": # add the surface of the grains value in the new file
            line = f"{v_phi} "+f"{phi}"
        if line == "#variable_PRE_COMP#":
            line = f"{v_pre_comp} "+f"{comp}"
        new_precomp_file.write(line+"\n") # write in the new file the char of variable line
    # end of while loop

    s_precomp_file.close() # close the source code file
    new_precomp_file.close() # close the new file
    return

def LAMMPS_shear_w(path,path_code,phi,dt,e_sh,shear,comp,N_restart): # modify Shearing LAMMPS source code file

    # Variable for velocity files
    N_step = round(e_sh /(shear*dt)) # compute the rounded and truncated step of time
    vel_file = round(N_step/12) # create 13 velocity files
    file_restart = N_restart

    end_file = "### End of shearing step ###" # identify the end of the LAMMPS source code file

    v_phi = "variable S_GRAINS equal" # surface of the grains value of the granular assembly
    v_dt = "variable DT equal" # discretization time
    v_e_sh = "variable E_SH equal" # final shear strain
    v_shear = "variable SHEAR equal" # imposed shear rate
    v_comp = "variable COMP equal" # imposed pressure
    v_vel_file = "variable V_FILE equal" # create the 13 restart files
    v_file = "variable FILE equal" # create the restart files for elastic properties computation

    # open the source LAMMPS text file and create the text file to be edited
    s_sh_file = open(f"{path_code}/in.floes_shearing.lmp","r")
    new_sh_file = open(f"{path}/in.floes_shearing.lmp","w+") # modified LAMMPS file copied

    line = "" # value of the line used to modifed the LAMMPS code

    while(end_file not in line): # search for the end of the source code
        # modification of shear file
        line = s_sh_file.readline().strip()
        if line == "#variable_S_GRAINS#": # add the surface of the grains value in the new file
            line = f"{v_phi} "+f"{phi}"
        if line == "#variable_DT#":
            line = f"{v_dt} " +f"{dt}"
        if line == "#variable_E_SH#":
            line = f"{v_e_sh} " +f"{e_sh}"
        if line == "#variable_SHEAR#":
            line = f"{v_shear} " +f"{shear}"
        if line == "#variable_COMP#":
            line = f"{v_comp} "+f"{comp}"
        if line == "#variable_V_FILE#":
            line = f"{v_vel_file} "+f"{vel_file}"
        if line == "#variable_FILE#":
            line = f"{v_file} " +f"{file_restart}"
        new_sh_file.write(line+"\n") # write in the new file the char of variable line
    # end of while loop

    s_sh_file.close() # close the source code file
    new_sh_file.close()
    return

def LAMMPS_ela_comp_w(path,path_code,visc,phi,dt): # modify Elastic Compression LAMMPS source code file
    end_file = "### End of elastic compression step ###" # identify the end of the LAMMPS source code file

    v_phi = "variable S_GRAINS equal" # surface of the grains value of the granular assembly
    v_visc = "variable VISC equal" # viscous damping value
    v_dt = "variable DT equal" # discretization time

    # open the source LAMMPS text file and create the text file to be edited
    s_ela_comp_file = open(f"{path_code}/in.floes_ela_comp.lmp","r")
    new_ela_comp_file = open(f"{path}/in.floes_ela_comp.lmp","w+") # modified LAMMPS file copied

    line = "" # value of the line used to modifed the LAMMPS code

    while(end_file not in line): # search for the end of the source code
        # modification of ela comp file
        line = s_ela_comp_file.readline().strip()
        if line == "#variable_S_GRAINS#":  # add the surface of the grains value in the new file
            line = f"{v_phi} "+f"{phi}"
        if line == "#variable_VISC#":  # add the viscous damping value in the new file
            line = f"{v_visc} "+f"{visc}"
        if line == "#variable_DT#":
            line = f"{v_dt} " +f"{dt}"
        new_ela_comp_file.write(line+"\n") # write in the new file the char of variable line
    # end of while loop

    s_ela_comp_file.close() # close the source code file
    new_ela_comp_file.close() # close the new file
    return

def LAMMPS_ela_shear_w(path,path_code,visc,phi,dt): # modify Elastic Shearing LAMMPS source code file
    end_file = "### End of elastic shearing step ###" # identify the end of the LAMMPS source code file

    v_phi = "variable S_GRAINS equal" # surface of the grains value of the granular assembly
    v_visc = "variable VISC equal" # viscous damping value
    v_dt = "variable DT equal" # discretization time

    # open the source LAMMPS text file and create the text file to be edited
    s_ela_sh_file = open(f"{path_code}/in.floes_ela_cis.lmp","r")
    new_ela_sh_file = open(f"{path}/in.floes_ela_cis.lmp","w+") # modified LAMMPS file copied

    line = "" # value of the line used to modifed the LAMMPS code

    while(end_file not in line): # search for the end of the source code
        # modification of ela shear file
        line = s_ela_sh_file.readline().strip()
        if line == "#variable_S_GRAINS#": # add the surface of the grains value in the new file
            line = f"{v_phi} "+f"{phi}"
        if line == "#variable_VISC#": # add the viscous damping value in the new file
            line = f"{v_visc} "+f"{visc}"
        if line == "#variable_DT#":
            line = f"{v_dt} " +f"{dt}"
        new_ela_sh_file.write(line+"\n") # write in the new file the char of variable line
    # end of while loop

    s_ela_sh_file.close() # close the source code file
    new_ela_sh_file.close() # close the new file
    return

def LAMMPS_ela_relax_w(path,path_code,phi,dt): # modify Elastic Shearing LAMMPS source code file
    end_file = "### End of elastic relaxation step ###" # identify the end of the LAMMPS source code file

    v_phi = "variable S_GRAINS equal" # surface of the grains value of the granular assembly
    v_dt = "variable DT equal" # discretvi ization time

    # open the source LAMMPS text file and create the text file to be edited
    s_ela_relax_file = open(f"{path_code}/in.floes_ela_relax.lmp","r")
    new_ela_relax_file = open(f"{path}/in.floes_ela_relax.lmp","w+") # modified LAMMPS file copied

    line = "" # value of the line used to modifed the LAMMPS code

    while(end_file not in line): # search for the end of the source code
        # modification of ela shear file
        line = s_ela_relax_file.readline().strip()
        if line == "#variable_S_GRAINS#": # add the surface of the grains value in the new file
            line = f"{v_phi} "+f"{phi}"
        if line == "#variable_DT#":
            line = f"{v_dt} " +f"{dt}"
        new_ela_relax_file.write(line+"\n") # write in the new file the char of variable line
    # end of while loop

    s_ela_relax_file.close() # close the source code file
    new_ela_relax_file.close() # close the new file
    return

def LAMMPS_ela_granu_0_w(path,path_code,phi,dt): # modify Elastic Shearing LAMMPS source code file
    end_file = "### End of granulence computation ###" # identify the end of the LAMMPS source code file

    v_phi = "variable S_GRAINS equal" # surface of the grains value of the granular assembly
    v_dt = "variable DT equal" # discretvi ization time

    # open the source LAMMPS text file and create the text file to be edited
    s_ela_granu_0_file = open(f"{path_code}/in.floes_granulence_0.lmp","r")
    new_ela_granu_0_file = open(f"{path}/in.floes_granulence_0.lmp","w+") # modified LAMMPS file copied

    line = "" # value of the line used to modifed the LAMMPS code

    while(end_file not in line): # search for the end of the source code
        # modification of ela shear file
        line = s_ela_granu_0_file.readline().strip()
        if line == "#variable_S_GRAINS#": # add the surface of the grains value in the new file
            line = f"{v_phi} "+f"{phi}"
        if line == "#variable_DT#":
            line = f"{v_dt} " +f"{dt}"
        new_ela_granu_0_file.write(line+"\n") # write in the new file the char of variable line
    # end of while loop

    s_ela_granu_0_file.close() # close the source code file
    new_ela_granu_0_file.close() # close the new file
    return

def LAMMPS_ela_granu_w(path,path_code,phi,dt,shear): # modify Elastic Shearing LAMMPS source code file
    end_file = "### End of granulence computation ###" # identify the end of the LAMMPS source code file

    v_phi = "variable S_GRAINS equal" # surface of the grains value of the granular assembly
    v_dt = "variable DT equal" # discretvi ization time
    v_shear = "variable SHEAR equal" # imposed shear rate

    # open the source LAMMPS text file and create the text file to be edited
    s_ela_granu_file = open(f"{path_code}/in.floes_granulence.lmp","r")
    new_ela_granu_file = open(f"{path}/in.floes_granulence.lmp","w+") # modified LAMMPS file copied

    line = "" # value of the line used to modifed the LAMMPS code

    while(end_file not in line): # search for the end of the source code
        # modification of ela shear file
        line = s_ela_granu_file.readline().strip()
        if line == "#variable_S_GRAINS#": # add the surface of the grains value in the new file
            line = f"{v_phi} "+f"{phi}"
        if line == "#variable_DT#":
            line = f"{v_dt} " +f"{dt}"
        if line == "#variable_SHEAR#":
            line = f"{v_shear} " +f"{shear}"
        new_ela_granu_file.write(line+"\n") # write in the new file the char of variable line
    # end of while loop

    s_ela_granu_file.close() # close the source code file
    new_ela_granu_file.close() # close the new file
    return

def LAMMPS_simu_w(path,path_code,dt,e_sh,shear,N_restart): # copy Simulation LAMMPS source code file

    step = N_restart # increment of the restart file

    end_file = "### End of simulation ###" # identify the end of the LAMMPS source code file
    v_restart = "read_restart endo.restart."

    N_step = round(e_sh /(shear*dt)) # compute the rounded and truncated step of time
    restart_save = step

    # open the source LAMMPS text file and create the text file to be edited
    s_simu_file = open(f"{path_code}/in.floes_simulation.lmp","r")
    new_simu_file = open(f"{path}/in.floes_simulation.lmp","w+") # modified LAMMPS file copied

    line = "" # value of the line used to modify the LAMMPS code

    while(end_file not in line):
        # modification of simulation file
        line = s_simu_file.readline().strip()

        if line =="# Elastic compression modulus":
            restart_save = step

        if line == "#read_restart_2#":
            no_restart = round_N_restart(2.5E-3*N_step,step)
            if no_restart <= restart_save or no_restart == 0 : # prevent to have 2 similar restart
                no_restart = restart_save + step
            restart_save = no_restart # save the value of the precedent restart
            line = f"{v_restart}"+f"{no_restart}"

        if line == "#read_restart_3#":
            no_restart = round_N_restart(5E-3*N_step,step)
            if no_restart <= restart_save or no_restart == 0 : # prevent to have 2 similar restart
                no_restart = restart_save + step
            restart_save = no_restart # save the value of the precedent restart
            line = f"{v_restart}"+f"{no_restart}"

        if line == "#read_restart_4#":
            no_restart = round_N_restart(7.5E-3*N_step,step)
            if no_restart <= restart_save or no_restart == 0 : # prevent to have 2 similar restart
                no_restart = restart_save + step
            restart_save = no_restart # save the value of the precedent restart
            line = f"{v_restart}"+f"{no_restart}"

        if line == "#read_restart_5#":
            no_restart = round_N_restart(2.5E-2*N_step,step)
            if no_restart <= restart_save or no_restart == 0 : # prevent to have 2 similar restart
                no_restart = restart_save + step
            restart_save = no_restart # save the value of the precedent restart
            line = f"{v_restart}"+f"{no_restart}"

        if line == "#read_restart_6#":
            no_restart = round_N_restart(5E-2*N_step,step)
            if no_restart <= restart_save or no_restart == 0 : # prevent to have 2 similar restart
                no_restart = restart_save + step
            restart_save = no_restart # save the value of the precedent restart
            line = f"{v_restart}"+f"{no_restart}"

        if line == "#read_restart_7#":
            no_restart = round_N_restart(7.5E-2*N_step,step)
            if no_restart <= restart_save or no_restart == 0 : # prevent to have 2 similar restart
                no_restart = restart_save + step
            restart_save = no_restart # save the value of the precedent restart
            line = f"{v_restart}"+f"{no_restart}"

        if line == "#read_restart_8#":
            no_restart = round_N_restart(1E-1*N_step,step)
            if no_restart <= restart_save or no_restart == 0 : # prevent to have 2 similar restart
                no_restart = restart_save + step
            restart_save = no_restart # save the value of the precedent restart
            line = f"{v_restart}"+f"{no_restart}"

        if line == "#read_restart_9#":
            no_restart = round_N_restart(1.5E-1*N_step,step)
            if no_restart <= restart_save or no_restart == 0 : # prevent to have 2 similar restart
                no_restart = restart_save + step
            restart_save = no_restart # save the value of the precedent restart
            line = f"{v_restart}"+f"{no_restart}"

        if line == "#read_restart_10#":
            no_restart = round_N_restart(2E-1*N_step,step)
            if no_restart <= restart_save or no_restart == 0 : # prevent to have 2 similar restart
                no_restart = restart_save + step
            restart_save = no_restart # save the value of the precedent restart
            line = f"{v_restart}"+f"{no_restart}"

        if line == "#read_restart_11#":
            no_restart = round_N_restart(2.5E-1*N_step,step)
            if no_restart <= restart_save or no_restart == 0 : # prevent to have 2 similar restart
                no_restart = restart_save + step
            restart_save = no_restart # save the value of the precedent restart
            line = f"{v_restart}"+f"{no_restart}"

        if line == "#read_restart_12#":
            no_restart = round_N_restart(3E-1*N_step,step)
            if no_restart <= restart_save or no_restart == 0 : # prevent to have 2 similar restart
                no_restart = restart_save + step
            restart_save = no_restart # save the value of the precedent restart
            line = f"{v_restart}"+f"{no_restart}"

        if line == "#read_restart_13#":
            no_restart = round_N_restart(4E-1*N_step,step)
            if no_restart <= restart_save or no_restart == 0 : # prevent to have 2 similar restart
                no_restart = restart_save + step
            restart_save = no_restart # save the value of the precedent restart
            line = f"{v_restart}"+f"{no_restart}"

        if line == "#read_restart_14#":
            no_restart = round_N_restart(5E-1*N_step,step)
            if no_restart <= restart_save  or no_restart == 0 : # prevent to have 2 similar restart
                no_restart = restart_save + step
            restart_save = no_restart # save the value of the precedent restart
            line = f"{v_restart}"+f"{no_restart}"

        if line == "#read_restart_15#":
            no_restart = round_N_restart(6E-1*N_step,step)
            if no_restart <= restart_save or no_restart == 0 : # prevent to have 2 similar restart
                no_restart = restart_save + step
            restart_save = no_restart # save the value of the precedent restart
            line = f"{v_restart}"+f"{no_restart}"

        if line == "#read_restart_16#":
            no_restart = round_N_restart(7E-1*N_step,step)
            if no_restart <= restart_save or no_restart == 0  : # prevent to have 2 similar restart
                no_restart = restart_save + step
            restart_save = no_restart # save the value of the precedent restart
            line = f"{v_restart}"+f"{no_restart}"

        if line == "#read_restart_17#":
            no_restart = round_N_restart(8E-1*N_step,step)
            if no_restart <= restart_save or no_restart == 0 : # prevent to have 2 similar restart
                no_restart = restart_save + step
            restart_save = no_restart # save the value of the precedent restart
            line = f"{v_restart}"+f"{no_restart}"

        if line == "#read_restart_18#":
            no_restart = round_N_restart(9E-1*N_step,step)
            if no_restart <= restart_save or no_restart == 0 : # prevent to have 2 similar restart
                no_restart = restart_save + step
            restart_save = no_restart # save the value of the precedent restart
            line = f"{v_restart}"+f"{no_restart}"

        if line == "#read_restart_19#":
            no_restart = round_N_restart(1.0*N_step,step)
            if no_restart <= restart_save or no_restart == 0 : # prevent to have 2 similar restart
                no_restart = restart_save + step
            restart_save = no_restart # save the value of the precedent restart
            line = f"{v_restart}"+f"{no_restart}"

        if line =="# Elastic shearing":
            restart_save = step

        new_simu_file.write(line+"\n") # copy in the new file the char of variable line
    # end of while loop

    s_simu_file.close() # close the source file
    new_simu_file.close # close the new file
    return

def LAMMPS_simu_relax_w(path,path_code,dt,e_sh,shear,N_restart): # copy Simulation LAMMPS source code file

    step = N_restart # increment of the restart file

    end_file = "### End of relaxation simulation ###" # identify the end of the LAMMPS source code file
    v_restart = "read_restart endo.restart."

    N_step = round(e_sh /(shear*dt)) # compute the rounded and truncated step of time
    restart_save = step

    # open the source LAMMPS text file and create the text file to be edited
    s_simu_relax_file = open(f"{path_code}/in.floes_simu_relax.lmp","r")
    new_simu_relax_file = open(f"{path}/in.floes_simu_relax.lmp","w+") # modified LAMMPS file copied

    line = "" # value of the line used to modify the LAMMPS code

    while(end_file not in line):
        # modification of simulation file
        line = s_simu_relax_file.readline().strip()

        if line == "#read_restart_2#":
            no_restart = round_N_restart(2.5E-3*N_step,step)
            if no_restart <= restart_save or no_restart == 0 : # prevent to have 2 similar restart
                no_restart = restart_save + step
            restart_save = no_restart # save the value of the precedent restart
            line = f"{v_restart}"+f"{no_restart}"

        if line == "#read_restart_3#":
            no_restart = round_N_restart(5E-3*N_step,step)
            if no_restart <= restart_save or no_restart == 0 : # prevent to have 2 similar restart
                no_restart = restart_save + step
            restart_save = no_restart # save the value of the precedent restart
            line = f"{v_restart}"+f"{no_restart}"

        if line == "#read_restart_4#":
            no_restart = round_N_restart(7.5E-3*N_step,step)
            if no_restart <= restart_save or no_restart == 0 : # prevent to have 2 similar restart
                no_restart = restart_save + step
            restart_save = no_restart # save the value of the precedent restart
            line = f"{v_restart}"+f"{no_restart}"

        if line == "#read_restart_5#":
            no_restart = round_N_restart(2.5E-2*N_step,step)
            if no_restart <= restart_save or no_restart == 0 : # prevent to have 2 similar restart
                no_restart = restart_save + step
            restart_save = no_restart # save the value of the precedent restart
            line = f"{v_restart}"+f"{no_restart}"

        if line == "#read_restart_6#":
            no_restart = round_N_restart(5E-2*N_step,step)
            if no_restart <= restart_save or no_restart == 0 : # prevent to have 2 similar restart
                no_restart = restart_save + step
            restart_save = no_restart # save the value of the precedent restart
            line = f"{v_restart}"+f"{no_restart}"

        if line == "#read_restart_7#":
            no_restart = round_N_restart(7.5E-2*N_step,step)
            if no_restart <= restart_save or no_restart == 0 : # prevent to have 2 similar restart
                no_restart = restart_save + step
            restart_save = no_restart # save the value of the precedent restart
            line = f"{v_restart}"+f"{no_restart}"

        if line == "#read_restart_8#":
            no_restart = round_N_restart(1E-1*N_step,step)
            if no_restart <= restart_save or no_restart == 0 : # prevent to have 2 similar restart
                no_restart = restart_save + step
            restart_save = no_restart # save the value of the precedent restart
            line = f"{v_restart}"+f"{no_restart}"

        if line == "#read_restart_9#":
            no_restart = round_N_restart(1.5E-1*N_step,step)
            if no_restart <= restart_save or no_restart == 0 : # prevent to have 2 similar restart
                no_restart = restart_save + step
            restart_save = no_restart # save the value of the precedent restart
            line = f"{v_restart}"+f"{no_restart}"

        if line == "#read_restart_10#":
            no_restart = round_N_restart(2E-1*N_step,step)
            if no_restart <= restart_save or no_restart == 0 : # prevent to have 2 similar restart
                no_restart = restart_save + step
            restart_save = no_restart # save the value of the precedent restart
            line = f"{v_restart}"+f"{no_restart}"

        if line == "#read_restart_11#":
            no_restart = round_N_restart(2.5E-1*N_step,step)
            if no_restart <= restart_save or no_restart == 0 : # prevent to have 2 similar restart
                no_restart = restart_save + step
            restart_save = no_restart # save the value of the precedent restart
            line = f"{v_restart}"+f"{no_restart}"

        if line == "#read_restart_12#":
            no_restart = round_N_restart(3E-1*N_step,step)
            if no_restart <= restart_save or no_restart == 0 : # prevent to have 2 similar restart
                no_restart = restart_save + step
            restart_save = no_restart # save the value of the precedent restart
            line = f"{v_restart}"+f"{no_restart}"

        if line == "#read_restart_13#":
            no_restart = round_N_restart(4E-1*N_step,step)
            if no_restart <= restart_save or no_restart == 0 : # prevent to have 2 similar restart
                no_restart = restart_save + step
            restart_save = no_restart # save the value of the precedent restart
            line = f"{v_restart}"+f"{no_restart}"

        if line == "#read_restart_14#":
            no_restart = round_N_restart(5E-1*N_step,step)
            if no_restart <= restart_save  or no_restart == 0 : # prevent to have 2 similar restart
                no_restart = restart_save + step
            restart_save = no_restart # save the value of the precedent restart
            line = f"{v_restart}"+f"{no_restart}"

        if line == "#read_restart_15#":
            no_restart = round_N_restart(6E-1*N_step,step)
            if no_restart <= restart_save or no_restart == 0 : # prevent to have 2 similar restart
                no_restart = restart_save + step
            restart_save = no_restart # save the value of the precedent restart
            line = f"{v_restart}"+f"{no_restart}"

        if line == "#read_restart_16#":
            no_restart = round_N_restart(7E-1*N_step,step)
            if no_restart <= restart_save or no_restart == 0  : # prevent to have 2 similar restart
                no_restart = restart_save + step
            restart_save = no_restart # save the value of the precedent restart
            line = f"{v_restart}"+f"{no_restart}"

        if line == "#read_restart_17#":
            no_restart = round_N_restart(8E-1*N_step,step)
            if no_restart <= restart_save or no_restart == 0 : # prevent to have 2 similar restart
                no_restart = restart_save + step
            restart_save = no_restart # save the value of the precedent restart
            line = f"{v_restart}"+f"{no_restart}"

        if line == "#read_restart_18#":
            no_restart = round_N_restart(9E-1*N_step,step)
            if no_restart <= restart_save or no_restart == 0 : # prevent to have 2 similar restart
                no_restart = restart_save + step
            restart_save = no_restart # save the value of the precedent restart
            line = f"{v_restart}"+f"{no_restart}"

        if line == "#read_restart_19#":
            no_restart = round_N_restart(1.0*N_step,step)
            if no_restart <= restart_save or no_restart == 0 : # prevent to have 2 similar restart
                no_restart = restart_save + step
            restart_save = no_restart # save the value of the precedent restart
            line = f"{v_restart}"+f"{no_restart}"

        if line =="# Elastic shearing":
            restart_save = step

        new_simu_relax_file.write(line+"\n") # copy in the new file the char of variable line
    # end of while loop

    s_simu_relax_file.close() # close the source file
    new_simu_relax_file.close # close the new file
    return

def LAMMPS_simu_granu_w(path,path_code,dt,e_sh,shear,N_restart): # copy Simulation LAMMPS source code file
    step = N_restart # increment of the restart file

    end_file = "### End of granulence simulation ###" # identify the end of the LAMMPS source code file
    v_restart = "read_restart endo.restart."

    N_step = round(e_sh /(shear*dt)) # compute the rounded and truncated step of time
    restart_save = step

    # open the source LAMMPS text file and create the text file to be edited
    s_simu_granu_file = open(f"{path_code}/in.floes_simu_granu.lmp","r")
    new_simu_granu_file = open(f"{path}/in.floes_simu_granu.lmp","w+") # modified LAMMPS file copied

    line = "" # value of the line used to modify the LAMMPS code

    while(end_file not in line):
        # modification of simulation file
        line = s_simu_granu_file.readline().strip()

        if line == "#read_restart_2#":
            no_restart = round_N_restart(2.5E-3*N_step,step)
            if no_restart <= restart_save or no_restart == 0 : # prevent to have 2 similar restart
                no_restart = restart_save + step
            restart_save = no_restart # save the value of the precedent restart
            line = f"{v_restart}"+f"{no_restart}"

        if line == "#read_restart_3#":
            no_restart = round_N_restart(5E-3*N_step,step)
            if no_restart <= restart_save or no_restart == 0 : # prevent to have 2 similar restart
                no_restart = restart_save + step
            restart_save = no_restart # save the value of the precedent restart
            line = f"{v_restart}"+f"{no_restart}"

        if line == "#read_restart_4#":
            no_restart = round_N_restart(7.5E-3*N_step,step)
            if no_restart <= restart_save or no_restart == 0 : # prevent to have 2 similar restart
                no_restart = restart_save + step
            restart_save = no_restart # save the value of the precedent restart
            line = f"{v_restart}"+f"{no_restart}"

        if line == "#read_restart_5#":
            no_restart = round_N_restart(2.5E-2*N_step,step)
            if no_restart <= restart_save or no_restart == 0 : # prevent to have 2 similar restart
                no_restart = restart_save + step
            restart_save = no_restart # save the value of the precedent restart
            line = f"{v_restart}"+f"{no_restart}"

        if line == "#read_restart_6#":
            no_restart = round_N_restart(5E-2*N_step,step)
            if no_restart <= restart_save or no_restart == 0 : # prevent to have 2 similar restart
                no_restart = restart_save + step
            restart_save = no_restart # save the value of the precedent restart
            line = f"{v_restart}"+f"{no_restart}"

        if line == "#read_restart_7#":
            no_restart = round_N_restart(7.5E-2*N_step,step)
            if no_restart <= restart_save or no_restart == 0 : # prevent to have 2 similar restart
                no_restart = restart_save + step
            restart_save = no_restart # save the value of the precedent restart
            line = f"{v_restart}"+f"{no_restart}"

        if line == "#read_restart_8#":
            no_restart = round_N_restart(1E-1*N_step,step)
            if no_restart <= restart_save or no_restart == 0 : # prevent to have 2 similar restart
                no_restart = restart_save + step
            restart_save = no_restart # save the value of the precedent restart
            line = f"{v_restart}"+f"{no_restart}"

        if line == "#read_restart_9#":
            no_restart = round_N_restart(1.5E-1*N_step,step)
            if no_restart <= restart_save or no_restart == 0 : # prevent to have 2 similar restart
                no_restart = restart_save + step
            restart_save = no_restart # save the value of the precedent restart
            line = f"{v_restart}"+f"{no_restart}"

        if line == "#read_restart_10#":
            no_restart = round_N_restart(2E-1*N_step,step)
            if no_restart <= restart_save or no_restart == 0 : # prevent to have 2 similar restart
                no_restart = restart_save + step
            restart_save = no_restart # save the value of the precedent restart
            line = f"{v_restart}"+f"{no_restart}"

        if line == "#read_restart_11#":
            no_restart = round_N_restart(2.5E-1*N_step,step)
            if no_restart <= restart_save or no_restart == 0 : # prevent to have 2 similar restart
                no_restart = restart_save + step
            restart_save = no_restart # save the value of the precedent restart
            line = f"{v_restart}"+f"{no_restart}"

        if line == "#read_restart_12#":
            no_restart = round_N_restart(3E-1*N_step,step)
            if no_restart <= restart_save or no_restart == 0 : # prevent to have 2 similar restart
                no_restart = restart_save + step
            restart_save = no_restart # save the value of the precedent restart
            line = f"{v_restart}"+f"{no_restart}"

        if line == "#read_restart_13#":
            no_restart = round_N_restart(4E-1*N_step,step)
            if no_restart <= restart_save or no_restart == 0 : # prevent to have 2 similar restart
                no_restart = restart_save + step
            restart_save = no_restart # save the value of the precedent restart
            line = f"{v_restart}"+f"{no_restart}"

        if line == "#read_restart_14#":
            no_restart = round_N_restart(5E-1*N_step,step)
            if no_restart <= restart_save  or no_restart == 0 : # prevent to have 2 similar restart
                no_restart = restart_save + step
            restart_save = no_restart # save the value of the precedent restart
            line = f"{v_restart}"+f"{no_restart}"

        if line == "#read_restart_15#":
            no_restart = round_N_restart(6E-1*N_step,step)
            if no_restart <= restart_save or no_restart == 0 : # prevent to have 2 similar restart
                no_restart = restart_save + step
            restart_save = no_restart # save the value of the precedent restart
            line = f"{v_restart}"+f"{no_restart}"

        if line == "#read_restart_16#":
            no_restart = round_N_restart(7E-1*N_step,step)
            if no_restart <= restart_save or no_restart == 0  : # prevent to have 2 similar restart
                no_restart = restart_save + step
            restart_save = no_restart # save the value of the precedent restart
            line = f"{v_restart}"+f"{no_restart}"

        if line == "#read_restart_17#":
            no_restart = round_N_restart(8E-1*N_step,step)
            if no_restart <= restart_save or no_restart == 0 : # prevent to have 2 similar restart
                no_restart = restart_save + step
            restart_save = no_restart # save the value of the precedent restart
            line = f"{v_restart}"+f"{no_restart}"

        if line == "#read_restart_18#":
            no_restart = round_N_restart(9E-1*N_step,step)
            if no_restart <= restart_save or no_restart == 0 : # prevent to have 2 similar restart
                no_restart = restart_save + step
            restart_save = no_restart # save the value of the precedent restart
            line = f"{v_restart}"+f"{no_restart}"

        if line == "#read_restart_19#":
            no_restart = round_N_restart(1.0*N_step,step)
            if no_restart <= restart_save or no_restart == 0 : # prevent to have 2 similar restart
                no_restart = restart_save + step
            restart_save = no_restart # save the value of the precedent restart
            line = f"{v_restart}"+f"{no_restart}"

        if line =="# Elastic shearing":
            restart_save = step

        new_simu_granu_file.write(line+"\n") # copy in the new file the char of variable line
    # end of while loop

    s_simu_granu_file.close() # close the source file
    new_simu_granu_file.close # close the new file
    return

def LAMMPS_files(path,path_code,visc,rho,l_ini,d_min,d_max,diam,N_max,N_restart,dt,dt_ela,e_sh,shear,comp): # call the underneath function to copy and modify the source code file
    phi = V_s(diam,N_max) # packing fraction of the granular assembly
    LAMMPS_ini_w(path,path_code,rho,l_ini,d_min,d_max,visc,N_max) # modify and copy Initialisation file
    LAMMPS_comp_w(path,path_code,phi) # modify and copy Compression file
    LAMMPS_relax_w(path,path_code,phi) # modify and copy Relaxation file
    LAMMPS_precomp_w(path,path_code,phi,comp) # modify and copy precompression file
    LAMMPS_shear_w(path,path_code,phi,dt,e_sh,shear,comp,N_restart) # modify and copy Shearing file
    LAMMPS_ela_comp_w(path,path_code,visc,phi,dt_ela) # modify and copy Elastic Compression file
    LAMMPS_ela_shear_w(path,path_code,visc,phi,dt_ela) # modify and copy Elastic Shearing file
    LAMMPS_ela_relax_w(path, path_code, phi, dt) # modify and copy Elastic Relaxation file
    LAMMPS_ela_granu_0_w(path, path_code, phi, dt) # modify and copy graulence_0 file
    LAMMPS_ela_granu_w(path, path_code, phi, dt, shear) # modify and copy granulence file
    LAMMPS_simu_w(path,path_code,dt,e_sh,shear,N_restart) # copy Simulation file
    LAMMPS_simu_relax_w(path,path_code,dt,e_sh,shear,N_restart) # copy Simulation_relax file
    LAMMPS_simu_granu_w(path,path_code,dt,e_sh,shear,N_restart) # copy Simulation_gran file
    return
