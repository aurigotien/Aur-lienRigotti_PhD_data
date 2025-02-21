# Modules
#import matplotlib.pyplot as plt
import numpy as np # load numpy package
import random as r # load random package

# Create N random grains in a LxL 2D box 
 
## Functions ## 
def position(X_data,d_grain,dmax,L,N): # give a random coordinate for the position vector X between 0 and L + provide overlap
    l_d = L # distance between the new grain and all the other grains
    l_d_min = l_d # save of the variable l_d for min research algo
    l_min = 0 # minimum distance between 2 grains
    X_ovlp = np.zeros((N,3)) # file to prevent the overlap between grains
    
    for grn in range(N):
        #print(X_data[grn][:])
        X_data[grn][0] = r.uniform(0,L) # use uniform law to give random position X and Y for the new grain
        X_data[grn][1] = r.uniform(0,L)
        if grn == 0: # save the position of the 1st grain
            X_ovlp = X_data  # store the grain coordinate
        # end of if 
        elif grn > 0: # rest of the grains
             for i in range(grn): # scan all the grains
                    l_d = ((abs(X_data[grn][0]-X_ovlp[i][0])**2)+(abs(X_data[grn][1]-X_ovlp[i][1])**2))**((1/2)) # distance btw grains
                    l_min = (d_grain[grn] + d_grain[i])/2 # minimal distance between the grain to prevent overlap
                    if l_d < l_d_min :  # search the minimum distance between the new grains and the other grains
                        l_d_min = l_d
                    # end of if 
                    while l_d_min < l_min : # search a position without overlapping between the grains
                        X_data[grn][0] = r.uniform(0+dmax,L-dmax) # attribution of the X position
                        X_data[grn][1] = r.uniform(0+dmax,L-dmax) # attribution of the Y position
                        l_d = ((abs(X_data[grn][0]-X_ovlp[i][0])**2)+(abs(X_data[grn][1]-X_ovlp[i][1])**2))**((1/2)) # new distance btw grain and neighbor
                        l_d_min = l_d # store the new distance between new grain and the neighbor
                    # end of while loop
             # end of while loop
             X_ovlp = X_data # store the position of the new grain
        # enf of if
    # end of for loop  
    return X_data # file with the position of all the grains

def poly_dispersity(d_min, d_max, N): # give a random diameter for particle
# don"t follow any distribution law
    d = np.ones(N)*d_min
    N_max = int(N/2)
    
    for i in range(N_max): # scan half of the grains created
        d[i] = d_max # gives to half of the grains the d_max diam

    return d # file with the diameter of all the created grains

def header(file,N): # create a header for the rand_config.lj file to be readable by LAMMPS command "include"
    # header of the file
    file.write("LAMMPS atoms coordinates file"+"\n") # line 0
    file.write("\n"+ f"{N}" +" "+"atoms"+"\n") # line 1
    file.write("\n"+"2 atom types"+"\n") # line 2
    return

def vel(file,v,N_max): # add small random velocity to the grains ie thermal agitation
    file.write("\n") # jump the line
    file.write("\n"+"Velocities # sphere"+"\n") # velocity header to be readable by LAMMPS
    
    for it in range(N_max): # scan all the atomes in the simulation box
        for i in range(len(v)): # scan the 6 line of the vector V = (Vx Vy Vz Wx Wy Wz)
            v[i] = r.gauss(-10**(-6),10**(-6)) # gaussian distribution centered to 0 
            
        v[2] = 0 # set Vz = 0 (2D simulation)
        v[4] = 0 # set Wyz = 0 (2D simulation)
        v[5] = 0 # set Wxz = 0 (2D simulation)
        
        # write the velocity of the grain i in the file 
        line = f"{it+1} "+f"{v[0]} "+f"{v[1]} "+f"{v[2]} "+f"{v[3]} "+f"{v[4]} "+f"{v[5]}"
        if it == 0: # line 1 : jump the line, write the line, jump to the next line
            file.write("\n"+line+"\n")
        elif it > 0 and it < N_max-1: # line 2 to N-1 : write the line, jump to the next line 
            file.write(line+"\n")
        elif it == N_max-1: # line N : write the line, no jump
            file.write(line)
    return

def atoms(file,L,X,d,d_min,d_max,rho,N_max): # create grain with random diameter in a file
    nb_g = np.zeros((N_max,2)) # compute the number of grain of each size
    
    d = poly_dispersity(d_min,d_max,N_max) # store in matrix d the value of the diameter of the grains
    Y = position(X,d,d_max,L,N_max) # store in matrix Y the position of the grains
    
    #print("positions calculés")
    file.write("\n"+"Atoms # sphere"+"\n") # give the number of grains use in the simulation
    for it in range(N_max): # create the N grains and set diam, mass and ID (1 to N)
        x_grain = Y[it][0] # store the x position of the grain 
        y_grain = Y[it][1] # store the y position of the grain
        z_grain = Y[it][2] # store the z position of the grain = 0
        
        # atom type 1 d = dmin, atom type 2 d=dmax
        if d[it] == d_min : 
            at_type = 1 # attribute type 1 for grains with diameter d = dmin
        elif d[it] == d_max :
            at_type = 2 # attribute type 2 for grains with diameter d = dmax
            
        # line i : the no of iteration, atome type, diameter of grain, density of grain, x position, y position, z position 
        line = f"{it+1} "+f"{at_type} " + f"{d[it]} "+f"{rho} "+f"{x_grain} "+f"{y_grain} "+f"{z_grain}"
        
        if it == 0: # line 1 : jump to next line, write the line, jump to next line
            file.write("\n"+line+"\n")
        elif it > 0 and it < N_max-1: # line 2 to N-1 : write the line, jump to next line
            file.write(line+"\n")
        elif it == N_max-1: # line N : write the line, no jump to next line 
            file.write(line)       
        # end of if loop 
        
        for i in range (N_max): # scan all the grain in the simulation box
            if d[it] == d_min: 
                nb_g[i,0] += 1 # count the number of grain of d = dmin
            elif d[it] == d_max:
                nb_g[i,1] += 1 # count the number of grain of d = dmax
        # end of if loop
    # end of for loop
    print("N_min = ", nb_g[0]) # print the number of grain of d = dmin
    print("N_max =", nb_g[1]) # print the number of grain of d = dmax
    return d # return the matrix d with the diameter and position of the grains

def file_edit(file,v,L,X,d,d_min,d_max,rho,N_max):
    header(file,N_max) # create the header of the file
    d = atoms(file,L,X,d,d_min,d_max,rho,N_max) # write the diameter, position and type of the grains in the file 
    vel(file,v,N_max) # write the random velocity of the grains
    return d # return the matrix d with the diameter and position of the grains