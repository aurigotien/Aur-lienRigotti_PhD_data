# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
### !!! The code need to be modify depending of which version of the lammps script your are using !!!
### !!! Line to modify : l.214 / l.217 ; l.271 / l.275 ; l.330 / l.333 ; l.388 / l.392 ; l.427 / l.432

### !!! As this code is made to work on my computer the path for the log.lammps file need to be modified

# Plot the graph from the log.lammps file
# Beginning

import matplotlib.pyplot as plt
import numpy as np

## Fonctions

def sep_fichier(log,f1,f2,f3,f_ela_comp_1,f_ela_comp_2,f_ela_comp_3,f_ela_comp_4,f_ela_comp_5,f_ela_comp_6,f_ela_comp_7,f_ela_comp_8,f_ela_cis_1,f_ela_cis_2,f_ela_cis_3,f_ela_cis_4,f_ela_cis_5,f_ela_cis_6,f_ela_cis_7,f_ela_cis_8):
    ## Function variable
    # 0 -> nothing is write
    # i -> write in the file no i
    # 20-> end of the program 
    ecriture = 0 # defining if something is write or not
    bloc = 0 # filter num data + head of the data column
    bloc_ela_comp = 1 # write in files comp_ela
    bloc_ela_cis = 1 # write in files cis_ela
    
    iteration = 0 # loop while counter
    it_max = 4230 # max iteration of while loop
    
    # limit of the blocs
    dbt_comp = str('## End of compression ##')
    fin_comp = str('### End of compression step ###')
    dbt_relax = str('## End of relaxation ##')
    fin_relax = str('### End of relaxation step ###')
    dbt_cis = str('## End of shearing ##')
    fin_cis = str('### End of shearing step ###')
    
    dbt_ela_comp = str('## End of elastic compression ##')
    fin_ela_comp = str('### End of elastic compression step ###')
    dbt_ela_cis = str('## End of elastic shearing ##')
    fin_ela_cis = str('### End of elastic shearing step ###')
    
    bloc_sup = 'Per MPI rank memory'
    bloc_inf = 'Loop time'
    
    ## Split log.lammps in 21 files
    while ecriture == 20 or iteration < it_max:
        ligne = log.readline().strip()
        #if buffer == None :
            #raise EOFerror
        
        # stop writting in files
        if ligne == fin_comp or ligne == fin_relax or ligne == fin_cis :
            ecriture = 0
        
        # stop writting in ela_ files
        if ligne == fin_ela_comp :
            ecriture = 0
            bloc_ela_comp = bloc_ela_comp +1
        
        if ligne == fin_ela_cis :
            ecriture = 0
            bloc_ela_cis = bloc_ela_cis +1
        
        # end of program
        if ligne == fin_ela_cis and ecriture == 19 :
            ecriture = 20
    
        # filter numeric datas + head of the data columns
        if ecriture != 0 and ecriture != 20 :  # if ecriture == 1....19
            if bloc_sup in ligne :
                bloc = 1 # write in the file 'compression'
            elif bloc_inf in ligne :
                bloc = 0 # stop writting

        # wrtie in file
        # data comp, relax and cis
        if bloc_sup not in ligne :
        # write in files comp, relax abd cis
            if ecriture == 1 and bloc == 1:
                f1.write(ligne+'\n')
            elif ecriture == 2 and bloc == 1 :
                f2.write(ligne+'\n')
            elif ecriture == 3 and bloc == 1:
                f3.write(ligne+'\n')
                
         # write in files ela_comp and ela_cis
         # elastic compression
            if ecriture == 4 and bloc == 1:
                f_ela_comp_1.write(ligne+'\n')
            elif ecriture == 5 and bloc == 1:
                f_ela_comp_2.write(ligne+'\n')
            elif ecriture == 6 and bloc == 1:
                f_ela_comp_3.write(ligne+'\n')
            elif ecriture == 7 and bloc == 1:
                f_ela_comp_4.write(ligne+'\n')
            elif ecriture == 8 and bloc == 1:
                f_ela_comp_5.write(ligne+'\n')
            elif ecriture == 9 and bloc == 1:
                f_ela_comp_6.write(ligne+'\n')
            elif ecriture == 10 and bloc == 1:
                f_ela_comp_7.write(ligne+'\n')
            elif ecriture == 11 and bloc == 1:
                f_ela_comp_8.write(ligne+'\n')
                
         # elastic shearing
            if ecriture == 12 and bloc == 1:
                f_ela_cis_1.write(ligne+'\n')
            elif ecriture == 13 and bloc == 1:
                f_ela_cis_2.write(ligne+'\n')
            elif ecriture == 14 and bloc == 1:
                f_ela_cis_3.write(ligne+'\n')
            elif ecriture == 15 and bloc == 1:
                f_ela_cis_4.write(ligne+'\n')
            elif ecriture == 16 and bloc == 1:
                f_ela_cis_5.write(ligne+'\n')
            elif ecriture == 17 and bloc == 1:
                f_ela_cis_6.write(ligne+'\n')
            elif ecriture == 18 and bloc == 1:
                f_ela_cis_7.write(ligne+'\n')
            elif ecriture == 19 and bloc == 1:
                f_ela_cis_8.write(ligne+'\n')
                
        # search for the beginning of the datas      
            if ecriture == 0 :
                # data comp, relax et cis
                if ligne == dbt_comp:
                    ecriture = 1
                elif ligne == dbt_relax:
                    ecriture = 2
                elif ligne == dbt_cis:
                    ecriture = 3
                    
                # elastc datas
                # elastic compression
                elif ligne == dbt_ela_comp :
                    if bloc_ela_comp == 1 :
                        ecriture = 4
                    elif bloc_ela_comp == 2 :
                        ecriture = 5
                    elif bloc_ela_comp == 3 :
                        ecriture = 6
                    elif bloc_ela_comp == 4 :
                        ecriture = 7
                    elif bloc_ela_comp == 5 :
                        ecriture = 8
                    elif bloc_ela_comp == 6 :
                        ecriture = 9
                    elif bloc_ela_comp == 7 :
                        ecriture = 10
                    elif bloc_ela_comp == 8 :
                        ecriture = 11
                
                # elastic shearing
                elif ligne == dbt_ela_cis :
                    if bloc_ela_cis == 1 :
                        ecriture = 12
                    elif bloc_ela_cis == 2 :
                        ecriture = 13
                    elif bloc_ela_cis == 3 :
                        ecriture = 14
                    elif bloc_ela_cis == 4 :
                        ecriture = 15
                    elif bloc_ela_cis == 5 :
                        ecriture = 16
                    elif bloc_ela_cis == 6 :
                        ecriture = 17
                    elif bloc_ela_cis == 7 :
                        ecriture = 18
                    elif bloc_ela_cis == 8 :
                        ecriture = 19
        
        iteration = iteration + 1
        
        if iteration == it_max:
            print('forced stop of the program')
            
    return    

def graph_comp(data): # plot for the compression step
    
    data.readline() # read data file line by line
    valeur = np.loadtxt(data) # data of the line into the variable 'valeur'
    
    time = (valeur[:,0] - valeur[0,0])*1E-5 # absciss of the curve
    vol = (valeur[:,7]*valeur[:,8]) # computation of the volume (1/packing fraction)
    
    # Coordination number 
    plt.figure(figsize= (10, 5)) # scale of the plot
    plt.plot(time, valeur[:,2], color = 'black', label = 'z') # creare the plot
    plt.title('Coordination number z versus time t - Biaxial compression') # title of the plot
    plt.xlabel('Time t (s)') # x label
    plt.ylabel('Coordination number z') # y label
    plt.legend() # plot the legend 
    plt.savefig('comp_z_vs_time.png') # save the plot into a file 
    plt.show()
    
    # Packing fraction 
    plt.figure(figsize= (10, 5))
    plt.plot(time, valeur[:,3], color = 'black', label = 'z')
    plt.title('Packing fraction versus time t - Biaxial compression')
    plt.xlabel('Time t (s)')
    plt.ylabel('Packing fraction')
    plt.legend()
    plt.savefig('comp_dens_vs_time.png')
    plt.show()

    # Stress 
    plt.figure(figsize= (10, 5))
    
    # !!! put line as a comment if using version v3 or v4 !!!
    plt.plot(time, valeur[:,12]/vol, color = 'red', label = 'p') 
    
    # !!! put lines as a coment if using version v5 or more !!!
    #plt.plot(time, valeur[:,9]/vol, color = 'red', label = 'sigma xx')
    #plt.plot(time, valeur[:,10]/vol, color = 'blue', label = 'sigma yy')
    
    plt.plot(time, valeur[:,11]/vol, color = 'green', label = 'sigma xy')
    
    plt.title('Mean stress p and shear stress xy versus time t - Biaxial compression')
    plt.xlabel('Time t (s)')
    plt.ylabel('Stress xx yy xy (Pa)')
    plt.legend()
    plt.savefig('comp_sigma_vs_time.png')
    plt.show()
    return

def graph_relax(data): # plot for the relaxation step
    
    data.readline()
    valeur = np.loadtxt(data)
    
    time = (valeur[:,0] - valeur[0,0])*1E-5
    vol = (valeur[:,7]*valeur[:,8])
    
    # Coordination number 
    plt.figure(figsize= (10, 5))
    plt.plot(time, valeur[:,2], label = 'z')
    plt.title('Coordination number z versus time t - Relaxation')
    plt.xlabel('Time t (s)')
    plt.ylabel('Coordination number z')
    plt.legend()
    plt.savefig('relax_z_vs_time.png')
    plt.show()
    
    # Packing fraction 
    plt.figure(figsize= (10, 5))
    plt.plot(time, valeur[:,3], color = 'black', label = 'z')
    plt.title('Packing fraction versus time t - Relaxation')
    plt.xlabel('Time t (s)')
    plt.ylabel('Packing fraction')
    plt.legend()
    plt.savefig('relax_dens_vs_time.png')
    plt.show()
    
    # Kinetic energy 
    plt.figure(figsize= (10, 5))
    plt.plot(time, valeur[:,9], label = 'energie cinetique')
    plt.title('Kinetic energy Ec versus time t - Relaxation')
    plt.xlabel('Time t (s)')
    plt.ylabel('Kinetic energy Ec (J)')
    plt.legend()
    plt.savefig('relax_nrjcin_vs_time.png')
    plt.show()

    # Stress
    plt.figure(figsize= (10, 5))
    
    # !!! put line as a comment if using version v3 or v4 !!!
    plt.plot(time, valeur[:,13]/vol, color = 'red', label = 'p')
    plt.plot(time, valeur[:,12]/vol, color = 'green', label = 'sigma xy')
    
    # !!! put lines as a coment if using version v5 or more !!!
    #plt.plot(time, valeur[:,10]/vol, color = 'green', label = 'sigma xx')
    #plt.plot(time, valeur[:,11]/vol, color = 'green', label = 'sigma yy')
    #plt.plot(time, valeur[:,12]/vol, color = 'green', label = 'sigma xy')
    
    plt.title('Mean stress p and shear stress xy versus time t - Relaxation')
    plt.xlabel('Time t')
    plt.ylabel('Stress xx yy xy (Pa)')
    plt.legend()
    plt.savefig('relax_sigma_vs_time.png')
    plt.show()
    return

def graph_cis(data): # plot for the shearing step
    
    data.readline()
    valeur = np.loadtxt(data)
    
    # Variables 
    shear_rate = 0.005 # shear rate of the simulation
    time_step = 1E-5
    ela_pla = 15 # limit between elastic and plastic respons
    vol = (valeur[:,6] * valeur[:,7]) # computation of the volume (1/packing fraction)
    cis = shear_rate * (valeur[:,0] - valeur[0,0]) * time_step # constrained shearing
    
    # Courbe de tendance cisaillement vs taux de deformation Trend curve shear stress vs constrained shearing
    mod_ela = np.polyfit(cis[:ela_pla], valeur[:ela_pla,10]/vol[:ela_pla], 1) 
    mod_visc = np.polyfit(cis[ela_pla:], valeur[ela_pla:,10]/vol[ela_pla:], 1)
    val_ela = mod_ela[0]*cis[:ela_pla] + mod_ela[1]
    val_visc = mod_visc[0]*cis[ela_pla:] + mod_visc[1]
    
    eq_ela = ('f(x) = ', mod_ela[0],'*x + ', mod_ela[1])
    eq_pla = ('f(x) = ', mod_visc[0],'*x + ', mod_visc[1])
    
    # Coordination number
    plt.figure(figsize= (10, 5))
    plt.plot(cis, valeur[:,4], label = 'z')
    plt.title('Coordination number versus constrained shearing')
    plt.xlabel('Constrain shearing (%)')
    plt.ylabel('Coordination Number z')
    plt.legend()
    plt.savefig('cis_z_vs_cis.png')
    plt.show()
    
    # Packing fraction
    plt.figure(figsize= (10, 5))
    plt.plot(cis, valeur[:,5], label = 'z')
    plt.title('Packing fraction versus constrained shearing')
    plt.xlabel('Constrained shearing (%)')
    plt.ylabel('Packing Fraction')
    plt.legend()
    plt.savefig('cis_dens_vs_cis.png')
    plt.show()
    
    # Normal stress 
    plt.figure(figsize= (10, 5))
    
    # !!! put line as a comment if using version v3 or v4 !!!
    plt.plot(cis, valeur[:,11]/vol, color = 'pink', label = 'p')
    
    # !!! put lines as a coment if using version v5 or more !!!
    #plt.plot(cis, valeur[:,8]/vol, color = 'red', label = 'sigma xx')
    #plt.plot(cis, valeur[:,9]/vol, color = 'blue', label = 'sigma yy')
    
    plt.title('Stress tensor component xx and yy, and stress invariant p versus constrained shearing')
    plt.xlabel('Constrained shearing (%)')
    plt.ylabel('Stress (Pa)')
    plt.legend()
    plt.savefig('cis_sigma_vs_txcis.png')
    plt.show()
    
    # Shear stress
    plt.figure(figsize= (10, 5))
    plt.plot(cis, valeur[:,10]/vol, label = 'sigma xy')
    plt.plot(cis[:ela_pla], val_ela, color = 'red', label = eq_ela)
    plt.plot(cis[ela_pla:], val_visc, color = 'blue', label = eq_pla)
    plt.title('Stress tensor shear xy versus constrained shearing')
    plt.xlabel('Constrained shearing (%)')
    plt.ylabel('Stress tensor shear (Pa)')
    plt.legend()
    plt.savefig('cis_cis_vs_txcis.png')
    plt.show()
    return

def graph_ela_comp(data): # plot for the elastic compression 
    
    data.readline()
    valeur = np.loadtxt(data)
    
    time = (valeur[:,0] - valeur[0,0])
    vol = (valeur[:,7]*valeur[:,8])
    
    # Stress
    plt.figure(figsize= (10, 5))
    
    # !!! put line as a comment if using version v3 or v4 !!!
    plt.plot(time, valeur[:,12]/vol, color = 'black', label = 'p')
    
    # !!! put lines as a coment if using version v5 or more !!!
    #plt.plot(time, valeur[:,9]/vol, color = 'red', label = 'sigma xx')
    #plt.plot(time, valeur[:,10]/vol, color ='blue', label = 'sigma yy')
    
    plt.title('Stress tensor p versus time t - elastic compression')
    plt.xlabel('Time t (s)')
    plt.ylabel('Stress xx yy xy (Pa)')
    plt.legend()
    plt.savefig('ela_comp_sigma_vs_time.png')
    plt.show()
    return

def graph_ela_cis(data): # plot for the elastic shearing 
    
    data.readline()
    valeur = np.loadtxt(data)
    
    # Variables 
    #vol = (valeur[:,6]*valeur[:,7]) # computation of the volume (1/packing fraction)
    defo = ((valeur[:,6]*valeur[:,7] - valeur[0,6]*valeur[0,7]) / (valeur[0,6]*valeur[0,7]))
    time = ((valeur[:,0] - 2.5E6)*1E-5) # constrained shear
    
    # Shear stress
    plt.figure(figsize= (10, 5))
    #plt.plot(time, valeur[:,10]/vol, label = 'sigma xy')
    plt.plot(time, defo, label = 'contrained shearing')
    plt.title('Stress tensor shear xy versus constrained shearing - elastic shearing')
    plt.xlabel('Constrained shearing (%)')
    plt.ylabel('Stress tensor shear (Pa)')
    plt.legend()
    plt.savefig('ela_cis_cis_vs_txcis.png')
    plt.show()
    return

## Extraction of the data file and plot the curves

# Sort the log.lammps file 
# Opening of the files

# !!! Opening of the log.lammps file !!!
# !!! You need to edit the path to open the right source file in the right place !!!

fichier_source = open('/Users/aurelienrigotti/Nextcloud/Documents/Simulations/periodique/log.lammps','r')
#fichier_source = open('/Users/aurelienrigotti/Nextcloud/Documents/Simulations/Versions_anterieur/Simulations_v3/log.lammps', 'r')
compression = open('/Users/aurelienrigotti/Nextcloud/Sorties_graphiques/donnees_a_editer/datas/data_comp.txt','w+')
relaxation = open('/Users/aurelienrigotti/Nextcloud/Sorties_graphiques/donnees_a_editer/datas/data_relax.txt','w+')
cisaillement = open('/Users/aurelienrigotti/Nextcloud/Sorties_graphiques/donnees_a_editer/datas/data_cis.txt','w+')

# Opening of the files for elastic data
ela_comp_1 = open('/Users/aurelienrigotti/Nextcloud/Sorties_graphiques/donnees_a_editer/data_ela/data_ela_1/data_ela_comp_1.txt','w+')
ela_comp_2 = open('/Users/aurelienrigotti/Nextcloud/Sorties_graphiques/donnees_a_editer/data_ela/data_ela_2/data_ela_comp_2.txt','w+')
ela_comp_3 = open('/Users/aurelienrigotti/Nextcloud/Sorties_graphiques/donnees_a_editer/data_ela/data_ela_3/data_ela_comp_3.txt','w+')
ela_comp_4 = open('/Users/aurelienrigotti/Nextcloud/Sorties_graphiques/donnees_a_editer/data_ela/data_ela_4/data_ela_comp_4.txt','w+')
ela_comp_5 = open('/Users/aurelienrigotti/Nextcloud/Sorties_graphiques/donnees_a_editer/data_ela/data_ela_5/data_ela_comp_5.txt','w+')
ela_comp_6 = open('/Users/aurelienrigotti/Nextcloud/Sorties_graphiques/donnees_a_editer/data_ela/data_ela_6/data_ela_comp_6.txt','w+')
ela_comp_7 = open('/Users/aurelienrigotti/Nextcloud/Sorties_graphiques/donnees_a_editer/data_ela/data_ela_7/data_ela_comp_7.txt','w+')
ela_comp_8 = open('/Users/aurelienrigotti/Nextcloud/Sorties_graphiques/donnees_a_editer/data_ela/data_ela_8/data_ela_comp_8.txt','w+')

ela_cis_1 = open('/Users/aurelienrigotti/Nextcloud/Sorties_graphiques/donnees_a_editer/data_ela/data_ela_1/data_ela_cis_1.txt','w+')
ela_cis_2 = open('/Users/aurelienrigotti/Nextcloud/Sorties_graphiques/donnees_a_editer/data_ela/data_ela_2/data_ela_cis_2.txt','w+')
ela_cis_3 = open('/Users/aurelienrigotti/Nextcloud/Sorties_graphiques/donnees_a_editer/data_ela/data_ela_3/data_ela_cis_3.txt','w+')
ela_cis_4 = open('/Users/aurelienrigotti/Nextcloud/Sorties_graphiques/donnees_a_editer/data_ela/data_ela_4/data_ela_cis_4.txt','w+')
ela_cis_5 = open('/Users/aurelienrigotti/Nextcloud/Sorties_graphiques/donnees_a_editer/data_ela/data_ela_5/data_ela_cis_5.txt','w+')
ela_cis_6 = open('/Users/aurelienrigotti/Nextcloud/Sorties_graphiques/donnees_a_editer/data_ela/data_ela_6/data_ela_cis_6.txt','w+')
ela_cis_7 = open('/Users/aurelienrigotti/Nextcloud/Sorties_graphiques/donnees_a_editer/data_ela/data_ela_7/data_ela_cis_7.txt','w+')
ela_cis_8 = open('/Users/aurelienrigotti/Nextcloud/Sorties_graphiques/donnees_a_editer/data_ela/data_ela_8/data_ela_cis_8.txt','w+')

# Traitement of the files
sep_fichier(fichier_source,compression,relaxation,cisaillement,ela_comp_1,ela_comp_2,ela_comp_3,ela_comp_4,ela_comp_5,ela_comp_6,ela_comp_7,ela_comp_8,ela_cis_1,ela_cis_2,ela_cis_3,ela_cis_4,ela_cis_5,ela_cis_6,ela_cis_7,ela_cis_8)

# Closure of the data files
fichier_source.close()
compression.close()
relaxation.close()
cisaillement.close()

# Elastic compression datas
ela_comp_1.close()
ela_comp_2.close()
ela_comp_3.close()
ela_comp_4.close()
ela_comp_5.close()
ela_comp_6.close()
ela_comp_7.close()
ela_comp_8.close()
# Elastic shearing datas
ela_cis_1.close()
ela_cis_2.close()
ela_cis_3.close()
ela_cis_4.close()
ela_cis_5.close()
ela_cis_6.close()
ela_cis_7.close()
ela_cis_8.close()

# Evolution of the mechanical properties graphs
# Opening of the files
compression = open('/Users/aurelienrigotti/Nextcloud/Sorties_graphiques/donnees_a_editer/datas/data_comp.txt','r')
relaxation = open('/Users/aurelienrigotti/Nextcloud/Sorties_graphiques/donnees_a_editer/datas/data_relax.txt','r')
cisaillement = open('/Users/aurelienrigotti/Nextcloud/Sorties_graphiques/donnees_a_editer/datas/data_cis.txt','r')

# Opening of the elastic data files
ela_comp_1 = open('/Users/aurelienrigotti/Nextcloud/Sorties_graphiques/donnees_a_editer/data_ela/data_ela_1/data_ela_comp_1.txt','r')
ela_comp_2 = open('/Users/aurelienrigotti/Nextcloud/Sorties_graphiques/donnees_a_editer/data_ela/data_ela_2/data_ela_comp_2.txt','r')
ela_comp_3 = open('/Users/aurelienrigotti/Nextcloud/Sorties_graphiques/donnees_a_editer/data_ela/data_ela_3/data_ela_comp_3.txt','r')
ela_comp_4 = open('/Users/aurelienrigotti/Nextcloud/Sorties_graphiques/donnees_a_editer/data_ela/data_ela_4/data_ela_comp_4.txt','r')
ela_comp_5 = open('/Users/aurelienrigotti/Nextcloud/Sorties_graphiques/donnees_a_editer/data_ela/data_ela_5/data_ela_comp_5.txt','r')
ela_comp_6 = open('/Users/aurelienrigotti/Nextcloud/Sorties_graphiques/donnees_a_editer/data_ela/data_ela_6/data_ela_comp_6.txt','r')
ela_comp_7 = open('/Users/aurelienrigotti/Nextcloud/Sorties_graphiques/donnees_a_editer/data_ela/data_ela_7/data_ela_comp_7.txt','r')
ela_comp_8 = open('/Users/aurelienrigotti/Nextcloud/Sorties_graphiques/donnees_a_editer/data_ela/data_ela_8/data_ela_comp_8.txt','r')

ela_cis_1 = open('/Users/aurelienrigotti/Nextcloud/Sorties_graphiques/donnees_a_editer/data_ela/data_ela_1/data_ela_cis_1.txt','r')
ela_cis_2 = open('/Users/aurelienrigotti/Nextcloud/Sorties_graphiques/donnees_a_editer/data_ela/data_ela_2/data_ela_cis_2.txt','r')
ela_cis_3 = open('/Users/aurelienrigotti/Nextcloud/Sorties_graphiques/donnees_a_editer/data_ela/data_ela_3/data_ela_cis_3.txt','r')
ela_cis_4 = open('/Users/aurelienrigotti/Nextcloud/Sorties_graphiques/donnees_a_editer/data_ela/data_ela_4/data_ela_cis_4.txt','r')
ela_cis_5 = open('/Users/aurelienrigotti/Nextcloud/Sorties_graphiques/donnees_a_editer/data_ela/data_ela_5/data_ela_cis_5.txt','r')
ela_cis_6 = open('/Users/aurelienrigotti/Nextcloud/Sorties_graphiques/donnees_a_editer/data_ela/data_ela_6/data_ela_cis_6.txt','r')
ela_cis_7 = open('/Users/aurelienrigotti/Nextcloud/Sorties_graphiques/donnees_a_editer/data_ela/data_ela_7/data_ela_cis_7.txt','r')
ela_cis_8 = open('/Users/aurelienrigotti/Nextcloud/Sorties_graphiques/donnees_a_editer/data_ela/data_ela_8/data_ela_cis_8.txt','r')

# Graph creation
graph_comp(compression)
graph_relax(relaxation)
graph_cis(cisaillement)

graph_ela_comp(ela_comp_1)
graph_ela_comp(ela_comp_2)
graph_ela_comp(ela_comp_3)
graph_ela_comp(ela_comp_4)
graph_ela_comp(ela_comp_5)
graph_ela_comp(ela_comp_6)
graph_ela_comp(ela_comp_7)
graph_ela_comp(ela_comp_8)

graph_ela_cis(ela_cis_1)
graph_ela_cis(ela_cis_2)
graph_ela_cis(ela_cis_3)
graph_ela_cis(ela_cis_4)
graph_ela_cis(ela_cis_5)
graph_ela_cis(ela_cis_6)
graph_ela_cis(ela_cis_7)
graph_ela_cis(ela_cis_8)

# Closure of the files   
fichier_source.close()
compression.close()
relaxation.close()
cisaillement.close()

# Elastic compression data files
ela_comp_1.close()
ela_comp_2.close()
ela_comp_3.close()
ela_comp_4.close()
ela_comp_5.close()
ela_comp_6.close()
ela_comp_7.close()
ela_comp_8.close()
# Elastic shearing data files
ela_cis_1.close()
ela_cis_2.close()
ela_cis_3.close()
ela_cis_4.close()
ela_cis_5.close()
ela_cis_6.close()
ela_cis_7.close()
ela_cis_8.close()

# End