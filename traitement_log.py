### !!! The code need to be modify depending of which version of the lammps script your are using !!!
### !!! Line to modify : l.214 / l.217 ; l.271 / l.275 ; l.330 / l.333 ; l.388 / l.392 ; l.427 / l.432

### !!! As this code is made to work on my computer the path for the log.lammps file need to be modified

# Plot the graph from the log.lammps file
# Beginning

import log_extraction as ext # load functions of extraction of the LAMMPS log file
import log_extr_relax as ext_relax # load functions of extraction of the LAMMPS log file
import graph as g # load the function to create the graphs

#  variables
choice = "yes" # if choice = no , no plot created

# variable = sh (to treat relax + shear)
# variable = sh_ela (treat relax + shear + ela_comp + ela_sh)
# variable = ela (treat ela_comp + ela_sh)
# variable = relax (treat relaxation)
# variable = gran (treat granulence)
traitement = 'sh_ela'

stack_file = 'stacks/strain_pressure/prep_no_fric/P_5kPa'
#stack_file = 'stacks_read/P_50kPa'

N = 30 # number of file to extract
num_simu = 4 # number of the stack of simulation to extract
#no_line_cis = 1001 # number of the lines
line_to_add = 0 # number of line to add in cis file

# Adimensional parameters
E = 5E8 # material (sea ice) young modulus (Pa)
t_n = 7E-2 # grain normal oscillation time (s)
d_ave = 100 # grain average diameter (m)

# matrix initialisation

# Sort the log.lammps file
# Opening of the files
# !!! Opening of the log.lammps file !!!
# !!! You need to edit the path to open the right source file in the right place !!!

if traitement == 'sh' or traitement == 'sh_ela' or traitement == 'ela' :
    for no_run in range(N): # do 30 iteration to extract the 30 simu file for 1 stack of simulation
        path  = f"/home/rigottia/Nextcloud/Documents/{stack_file}/simu_{num_simu}/run_{no_run+1}"

        fichier_source = open(f"{path}/simulation/log_sh.lammps","r") # source file for the lammps log extraction

        if traitement == 'sh' or traitement == 'sh_ela':
            compression = open(f"{path}/extr_data/data/data_comp.txt","w+") # create and write in the file data_comp
            relaxation = open(f"{path}/extr_data/data/data_relax.txt","w+") # create and write in the file data_relax
            pre_comp = open(f"{path}/extr_data/data/data_pre_comp.txt","w+") # create and write in the file data_pre_comp
            cisaillement = open(f"{path}/extr_data/data/data_cis.txt","w+") # create and write in the file data_cis

            # Open and write in files data_ela_comp for elastic data
            ela_comp_1 = open(f"{path}/extr_data/data_ela/data_ela_1/data_ela_comp_1.txt","r")
            ela_comp_2 = open(f"{path}/extr_data/data_ela/data_ela_2/data_ela_comp_2.txt","r")
            ela_comp_3 = open(f"{path}/extr_data/data_ela/data_ela_3/data_ela_comp_3.txt","r")
            ela_comp_4 = open(f"{path}/extr_data/data_ela/data_ela_4/data_ela_comp_4.txt","r")
            ela_comp_5 = open(f"{path}/extr_data/data_ela/data_ela_5/data_ela_comp_5.txt","r")
            ela_comp_6 = open(f"{path}/extr_data/data_ela/data_ela_6/data_ela_comp_6.txt","r")
            ela_comp_7 = open(f"{path}/extr_data/data_ela/data_ela_7/data_ela_comp_7.txt","r")
            ela_comp_8 = open(f"{path}/extr_data/data_ela/data_ela_8/data_ela_comp_8.txt","r")
            ela_comp_9 = open(f"{path}/extr_data/data_ela/data_ela_9/data_ela_comp_9.txt","r")
            ela_comp_10 = open(f"{path}/extr_data/data_ela/data_ela_10/data_ela_comp_10.txt","r")
            ela_comp_11 = open(f"{path}/extr_data/data_ela/data_ela_11/data_ela_comp_11.txt","r")
            ela_comp_12 = open(f"{path}/extr_data/data_ela/data_ela_12/data_ela_comp_12.txt","r")
            ela_comp_13 = open(f"{path}/extr_data/data_ela/data_ela_13/data_ela_comp_13.txt","r")
            ela_comp_14 = open(f"{path}/extr_data/data_ela/data_ela_14/data_ela_comp_14.txt","r")
            ela_comp_15 = open(f"{path}/extr_data/data_ela/data_ela_15/data_ela_comp_15.txt","r")
            ela_comp_16 = open(f"{path}/extr_data/data_ela/data_ela_16/data_ela_comp_16.txt","r")
            ela_comp_17 = open(f"{path}/extr_data/data_ela/data_ela_17/data_ela_comp_17.txt","r")
            ela_comp_18 = open(f"{path}/extr_data/data_ela/data_ela_18/data_ela_comp_18.txt","r")
            ela_comp_19 = open(f"{path}/extr_data/data_ela/data_ela_19/data_ela_comp_19.txt","r")

            # Open and write in the file data_ela_cis for elastic data
            ela_cis_1 = open(f"{path}/extr_data/data_ela/data_ela_1/data_ela_cis_1.txt","r")
            ela_cis_2 = open(f"{path}/extr_data/data_ela/data_ela_2/data_ela_cis_2.txt","r")
            ela_cis_3 = open(f"{path}/extr_data/data_ela/data_ela_3/data_ela_cis_3.txt","r")
            ela_cis_4 = open(f"{path}/extr_data/data_ela/data_ela_4/data_ela_cis_4.txt","r")
            ela_cis_5 = open(f"{path}/extr_data/data_ela/data_ela_5/data_ela_cis_5.txt","r")
            ela_cis_6 = open(f"{path}/extr_data/data_ela/data_ela_6/data_ela_cis_6.txt","r")
            ela_cis_7 = open(f"{path}/extr_data/data_ela/data_ela_7/data_ela_cis_7.txt","r")
            ela_cis_8 = open(f"{path}/extr_data/data_ela/data_ela_8/data_ela_cis_8.txt","r")
            ela_cis_9 = open(f"{path}/extr_data/data_ela/data_ela_9/data_ela_cis_9.txt","r")
            ela_cis_10 = open(f"{path}/extr_data/data_ela/data_ela_10/data_ela_cis_10.txt","r")
            ela_cis_11 = open(f"{path}/extr_data/data_ela/data_ela_11/data_ela_cis_11.txt","r")
            ela_cis_12 = open(f"{path}/extr_data/data_ela/data_ela_12/data_ela_cis_12.txt","r")
            ela_cis_13 = open(f"{path}/extr_data/data_ela/data_ela_13/data_ela_cis_13.txt","r")
            ela_cis_14 = open(f"{path}/extr_data/data_ela/data_ela_14/data_ela_cis_14.txt","r")
            ela_cis_15 = open(f"{path}/extr_data/data_ela/data_ela_15/data_ela_cis_15.txt","r")
            ela_cis_16 = open(f"{path}/extr_data/data_ela/data_ela_16/data_ela_cis_16.txt","r")
            ela_cis_17 = open(f"{path}/extr_data/data_ela/data_ela_17/data_ela_cis_17.txt","r")
            ela_cis_18 = open(f"{path}/extr_data/data_ela/data_ela_18/data_ela_cis_18.txt","r")
            ela_cis_19 = open(f"{path}/extr_data/data_ela/data_ela_19/data_ela_cis_19.txt","r")
        # end if

        if traitement == 'ela':
            compression = open(f"{path}/extr_data/data/data_comp.txt","r") # create and write in the file data_comp
            relaxation = open(f"{path}/extr_data/data/data_relax.txt","r") # create and write in the file data_relax
            pre_comp = open(f"{path}/extr_data/data/data_pre_comp.txt","r") # create and write in the file data_pre_comp
            cisaillement = open(f"{path}/extr_data/data/data_cis.txt","r") # create and write in the file data_cis

            # Open and write in files data_ela_comp for elastic data
            ela_comp_1 = open(f"{path}/extr_data/data_ela/data_ela_1/data_ela_comp_1.txt","w+")
            ela_comp_2 = open(f"{path}/extr_data/data_ela/data_ela_2/data_ela_comp_2.txt","w+")
            ela_comp_3 = open(f"{path}/extr_data/data_ela/data_ela_3/data_ela_comp_3.txt","w+")
            ela_comp_4 = open(f"{path}/extr_data/data_ela/data_ela_4/data_ela_comp_4.txt","w+")
            ela_comp_5 = open(f"{path}/extr_data/data_ela/data_ela_5/data_ela_comp_5.txt","w+")
            ela_comp_6 = open(f"{path}/extr_data/data_ela/data_ela_6/data_ela_comp_6.txt","w+")
            ela_comp_7 = open(f"{path}/extr_data/data_ela/data_ela_7/data_ela_comp_7.txt","w+")
            ela_comp_8 = open(f"{path}/extr_data/data_ela/data_ela_8/data_ela_comp_8.txt","w+")
            ela_comp_9 = open(f"{path}/extr_data/data_ela/data_ela_9/data_ela_comp_9.txt","w+")
            ela_comp_10 = open(f"{path}/extr_data/data_ela/data_ela_10/data_ela_comp_10.txt","w+")
            ela_comp_11 = open(f"{path}/extr_data/data_ela/data_ela_11/data_ela_comp_11.txt","w+")
            ela_comp_12 = open(f"{path}/extr_data/data_ela/data_ela_12/data_ela_comp_12.txt","w+")
            ela_comp_13 = open(f"{path}/extr_data/data_ela/data_ela_13/data_ela_comp_13.txt","w+")
            ela_comp_14 = open(f"{path}/extr_data/data_ela/data_ela_14/data_ela_comp_14.txt","w+")
            ela_comp_15 = open(f"{path}/extr_data/data_ela/data_ela_15/data_ela_comp_15.txt","w+")
            ela_comp_16 = open(f"{path}/extr_data/data_ela/data_ela_16/data_ela_comp_16.txt","w+")
            ela_comp_17 = open(f"{path}/extr_data/data_ela/data_ela_17/data_ela_comp_17.txt","w+")
            ela_comp_18 = open(f"{path}/extr_data/data_ela/data_ela_18/data_ela_comp_18.txt","w+")
            ela_comp_19 = open(f"{path}/extr_data/data_ela/data_ela_19/data_ela_comp_19.txt","w+")

            # Open and write in the file data_ela_cis for elastic data
            ela_cis_1 = open(f"{path}/extr_data/data_ela/data_ela_1/data_ela_cis_1.txt","w+")
            ela_cis_2 = open(f"{path}/extr_data/data_ela/data_ela_2/data_ela_cis_2.txt","w+")
            ela_cis_3 = open(f"{path}/extr_data/data_ela/data_ela_3/data_ela_cis_3.txt","w+")
            ela_cis_4 = open(f"{path}/extr_data/data_ela/data_ela_4/data_ela_cis_4.txt","w+")
            ela_cis_5 = open(f"{path}/extr_data/data_ela/data_ela_5/data_ela_cis_5.txt","w+")
            ela_cis_6 = open(f"{path}/extr_data/data_ela/data_ela_6/data_ela_cis_6.txt","w+")
            ela_cis_7 = open(f"{path}/extr_data/data_ela/data_ela_7/data_ela_cis_7.txt","w+")
            ela_cis_8 = open(f"{path}/extr_data/data_ela/data_ela_8/data_ela_cis_8.txt","w+")
            ela_cis_9 = open(f"{path}/extr_data/data_ela/data_ela_9/data_ela_cis_9.txt","w+")
            ela_cis_10 = open(f"{path}/extr_data/data_ela/data_ela_10/data_ela_cis_10.txt","w+")
            ela_cis_11 = open(f"{path}/extr_data/data_ela/data_ela_11/data_ela_cis_11.txt","w+")
            ela_cis_12 = open(f"{path}/extr_data/data_ela/data_ela_12/data_ela_cis_12.txt","w+")
            ela_cis_13 = open(f"{path}/extr_data/data_ela/data_ela_13/data_ela_cis_13.txt","w+")
            ela_cis_14 = open(f"{path}/extr_data/data_ela/data_ela_14/data_ela_cis_14.txt","w+")
            ela_cis_15 = open(f"{path}/extr_data/data_ela/data_ela_15/data_ela_cis_15.txt","w+")
            ela_cis_16 = open(f"{path}/extr_data/data_ela/data_ela_16/data_ela_cis_16.txt","w+")
            ela_cis_17 = open(f"{path}/extr_data/data_ela/data_ela_17/data_ela_cis_17.txt","w+")
            ela_cis_18 = open(f"{path}/extr_data/data_ela/data_ela_18/data_ela_cis_18.txt","w+")
            ela_cis_19 = open(f"{path}/extr_data/data_ela/data_ela_19/data_ela_cis_19.txt","w+")
        # end if

        if traitement == 'sh_ela':
            compression = open(f"{path}/extr_data/data/data_comp.txt","w+") # create and write in the file data_comp
            relaxation = open(f"{path}/extr_data/data/data_relax.txt","w+") # create and write in the file data_relax
            pre_comp = open(f"{path}/extr_data/data/data_pre_comp.txt","w+") # create and write in the file data_pre_comp
            cisaillement = open(f"{path}/extr_data/data/data_cis.txt","w+") # create and write in the file data_cis

            # Open and write in files data_ela_comp for elastic data
            ela_comp_1 = open(f"{path}/extr_data/data_ela/data_ela_1/data_ela_comp_1.txt","w+")
            ela_comp_2 = open(f"{path}/extr_data/data_ela/data_ela_2/data_ela_comp_2.txt","w+")
            ela_comp_3 = open(f"{path}/extr_data/data_ela/data_ela_3/data_ela_comp_3.txt","w+")
            ela_comp_4 = open(f"{path}/extr_data/data_ela/data_ela_4/data_ela_comp_4.txt","w+")
            ela_comp_5 = open(f"{path}/extr_data/data_ela/data_ela_5/data_ela_comp_5.txt","w+")
            ela_comp_6 = open(f"{path}/extr_data/data_ela/data_ela_6/data_ela_comp_6.txt","w+")
            ela_comp_7 = open(f"{path}/extr_data/data_ela/data_ela_7/data_ela_comp_7.txt","w+")
            ela_comp_8 = open(f"{path}/extr_data/data_ela/data_ela_8/data_ela_comp_8.txt","w+")
            ela_comp_9 = open(f"{path}/extr_data/data_ela/data_ela_9/data_ela_comp_9.txt","w+")
            ela_comp_10 = open(f"{path}/extr_data/data_ela/data_ela_10/data_ela_comp_10.txt","w+")
            ela_comp_11 = open(f"{path}/extr_data/data_ela/data_ela_11/data_ela_comp_11.txt","w+")
            ela_comp_12 = open(f"{path}/extr_data/data_ela/data_ela_12/data_ela_comp_12.txt","w+")
            ela_comp_13 = open(f"{path}/extr_data/data_ela/data_ela_13/data_ela_comp_13.txt","w+")
            ela_comp_14 = open(f"{path}/extr_data/data_ela/data_ela_14/data_ela_comp_14.txt","w+")
            ela_comp_15 = open(f"{path}/extr_data/data_ela/data_ela_15/data_ela_comp_15.txt","w+")
            ela_comp_16 = open(f"{path}/extr_data/data_ela/data_ela_16/data_ela_comp_16.txt","w+")
            ela_comp_17 = open(f"{path}/extr_data/data_ela/data_ela_17/data_ela_comp_17.txt","w+")
            ela_comp_18 = open(f"{path}/extr_data/data_ela/data_ela_18/data_ela_comp_18.txt","w+")
            ela_comp_19 = open(f"{path}/extr_data/data_ela/data_ela_19/data_ela_comp_19.txt","w+")

            # Open and write in the file data_ela_cis for elastic data
            ela_cis_1 = open(f"{path}/extr_data/data_ela/data_ela_1/data_ela_cis_1.txt","w+")
            ela_cis_2 = open(f"{path}/extr_data/data_ela/data_ela_2/data_ela_cis_2.txt","w+")
            ela_cis_3 = open(f"{path}/extr_data/data_ela/data_ela_3/data_ela_cis_3.txt","w+")
            ela_cis_4 = open(f"{path}/extr_data/data_ela/data_ela_4/data_ela_cis_4.txt","w+")
            ela_cis_5 = open(f"{path}/extr_data/data_ela/data_ela_5/data_ela_cis_5.txt","w+")
            ela_cis_6 = open(f"{path}/extr_data/data_ela/data_ela_6/data_ela_cis_6.txt","w+")
            ela_cis_7 = open(f"{path}/extr_data/data_ela/data_ela_7/data_ela_cis_7.txt","w+")
            ela_cis_8 = open(f"{path}/extr_data/data_ela/data_ela_8/data_ela_cis_8.txt","w+")
            ela_cis_9 = open(f"{path}/extr_data/data_ela/data_ela_9/data_ela_cis_9.txt","w+")
            ela_cis_10 = open(f"{path}/extr_data/data_ela/data_ela_10/data_ela_cis_10.txt","w+")
            ela_cis_11 = open(f"{path}/extr_data/data_ela/data_ela_11/data_ela_cis_11.txt","w+")
            ela_cis_12 = open(f"{path}/extr_data/data_ela/data_ela_12/data_ela_cis_12.txt","w+")
            ela_cis_13 = open(f"{path}/extr_data/data_ela/data_ela_13/data_ela_cis_13.txt","w+")
            ela_cis_14 = open(f"{path}/extr_data/data_ela/data_ela_14/data_ela_cis_14.txt","w+")
            ela_cis_15 = open(f"{path}/extr_data/data_ela/data_ela_15/data_ela_cis_15.txt","w+")
            ela_cis_16 = open(f"{path}/extr_data/data_ela/data_ela_16/data_ela_cis_16.txt","w+")
            ela_cis_17 = open(f"{path}/extr_data/data_ela/data_ela_17/data_ela_cis_17.txt","w+")
            ela_cis_18 = open(f"{path}/extr_data/data_ela/data_ela_18/data_ela_cis_18.txt","w+")
            ela_cis_19 = open(f"{path}/extr_data/data_ela/data_ela_19/data_ela_cis_19.txt","w+")
        # end if

        # Extraction of the log LAMMPS log file
        ext.sep_fichier(fichier_source,compression,relaxation,pre_comp,cisaillement,ela_comp_1,ela_comp_2,ela_comp_3,ela_comp_4,ela_comp_5,ela_comp_6,ela_comp_7,ela_comp_8,ela_comp_9,ela_comp_10,ela_comp_11,ela_comp_12,ela_comp_13,ela_comp_14,ela_comp_15,ela_comp_16,ela_comp_17,ela_comp_18,ela_comp_19,ela_cis_1,ela_cis_2,ela_cis_3,ela_cis_4,ela_cis_5,ela_cis_6,ela_cis_7,ela_cis_8,ela_cis_9,ela_cis_10,ela_cis_11,ela_cis_12,ela_cis_13,ela_cis_14,ela_cis_15,ela_cis_16,ela_cis_17,ela_cis_18,ela_cis_19,traitement)

        # Closure of the data files
        fichier_source.close()
        compression.close()
        relaxation.close()
        pre_comp.close()
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
        ela_comp_9.close()
        ela_comp_10.close()
        ela_comp_11.close()
        ela_comp_12.close()
        ela_comp_13.close()
        ela_comp_14.close()
        ela_comp_15.close()
        ela_comp_16.close()
        ela_comp_17.close()
        ela_comp_18.close()
        ela_comp_19.close()

        # Elastic shearing datas
        ela_cis_1.close()
        ela_cis_2.close()
        ela_cis_3.close()
        ela_cis_4.close()
        ela_cis_5.close()
        ela_cis_6.close()
        ela_cis_7.close()
        ela_cis_8.close()
        ela_cis_9.close()
        ela_cis_10.close()
        ela_cis_11.close()
        ela_cis_12.close()
        ela_cis_13.close()
        ela_cis_14.close()
        ela_cis_15.close()
        ela_cis_16.close()
        ela_cis_17.close()
        ela_cis_18.close()
        ela_cis_19.close()
        print(path)

        cisaillement = open(f"{path}/extr_data/data/data_cis.txt", "r")
        len_cis = len(cisaillement.readlines())
        cisaillement.close()

        """
        print("no line of sh file = ", len_cis)
        if len_cis < no_line_cis :
            line_to_add = abs(len_cis-no_line_cis)
            ext.file_function(path,no_line_cis,line_to_add)
        # end if
        """
    # end of for loop

    # Evolution of the mechanical properties graphs
    print("Graph print : ","\n", "Do you want graphs ? yes/no (default no)")
    choice = input()

    if (choice == "yes"):
        print("Compression, relaxation and cisaillement ? yes/no (default no)")
        choice = input()
        if (choice == "yes"):
            # Opening of the files to print the graph
            compression = open(f"{path}/extr_data/data/data_comp.txt","r")
            relaxation = open(f"{path}/extr_data/data/data_relax.txt","r")
            cisaillement = open(f"{path}/extr_data/data/data_cis.txt","r")

            # Graph creation
            g.graph_call(compression,relaxation,cisaillement)

            # Closure of the files
            fichier_source.close()
            compression.close()
            relaxation.close()
            cisaillement.close()
        # end of if

        print("\n Elastic oscillatory biaxial compression and shear test ? yes/no (default no)")
        choice = input()
        if (choice == "yes"):
            # Opening of the files to print the graph
                comp1 = open(f"{path}/extr_data/data_ela/data_ela_1/data_ela_comp_1.txt","r")
                comp3 = open(f"{path}/extr_data/data_ela/data_ela_3/data_ela_comp_3.txt","r")
                comp5 = open(f"{path}/extr_data/data_ela/data_ela_5/data_ela_comp_5.txt","r")
                comp8 = open(f"{path}/extr_data/data_ela/data_ela_8/data_ela_comp_8.txt","r")
                comp11 = open(f"{path}/extr_data/data_ela/data_ela_11/data_ela_comp_11.txt","r")
                comp19 = open(f"{path}/extr_data/data_ela/data_ela_19/data_ela_comp_19.txt","r")

                cis1 = open(f"{path}/extr_data/data_ela/data_ela_1/data_ela_cis_1.txt","r")
                cis3 = open(f"{path}/extr_data/data_ela/data_ela_3/data_ela_cis_3.txt","r")
                cis5 = open(f"{path}/extr_data/data_ela/data_ela_5/data_ela_cis_5.txt","r")
                cis8 = open(f"{path}/extr_data/data_ela/data_ela_8/data_ela_cis_8.txt","r")
                cis11 = open(f"{path}/extr_data/data_ela/data_ela_11/data_ela_cis_11.txt","r")
                cis19 = open(f"{path}/extr_data/data_ela/data_ela_19/data_ela_cis_19.txt","r")

            # Create the graph
                g.graph_ela_comp(comp1,comp3,comp5,comp8,comp11,comp19)
                g.graph_ela_cis(cis1,cis3,cis5,cis8,cis11,cis19)

            # Close the file
                comp1.close()
                comp3.close()
                comp5.close()
                comp8.close()
                comp11.close()
                comp19.close()

                cis1.close()
                cis3.close()
                cis5.close()
                cis8.close()
                cis11.close()
                cis19.close()
    # end of if

elif traitement == 'relax' or traitement == 'gran':
    for no_run in range(N): # do 30 iteration to extract the 30 simu file for 1 stack of simulation
        path  = f"/home/rigottia/Nextcloud/Documents/{stack_file}/simu_{num_simu}/run_{no_run+1}"

        fichier_source = open(f"{path}/simulation/log_relax.lammps","r") # source file for the lammps log extraction

        if traitement == 'relax':
            # Open and write in files data_ela_relax for elastic datas
            ela_relax_1 = open(f"{path}/extr_data/data_ela/data_ela_1/data_ela_relax_1.txt","w+")
            ela_relax_2 = open(f"{path}/extr_data/data_ela/data_ela_2/data_ela_relax_2.txt","w+")
            ela_relax_3 = open(f"{path}/extr_data/data_ela/data_ela_3/data_ela_relax_3.txt","w+")
            ela_relax_4 = open(f"{path}/extr_data/data_ela/data_ela_4/data_ela_relax_4.txt","w+")
            ela_relax_5 = open(f"{path}/extr_data/data_ela/data_ela_5/data_ela_relax_5.txt","w+")
            ela_relax_6 = open(f"{path}/extr_data/data_ela/data_ela_6/data_ela_relax_6.txt","w+")
            ela_relax_7 = open(f"{path}/extr_data/data_ela/data_ela_7/data_ela_relax_7.txt","w+")
            ela_relax_8 = open(f"{path}/extr_data/data_ela/data_ela_8/data_ela_relax_8.txt","w+")
            ela_relax_9 = open(f"{path}/extr_data/data_ela/data_ela_9/data_ela_relax_9.txt","w+")
            ela_relax_10 = open(f"{path}/extr_data/data_ela/data_ela_10/data_ela_relax_10.txt","w+")
            ela_relax_11 = open(f"{path}/extr_data/data_ela/data_ela_11/data_ela_relax_11.txt","w+")
            ela_relax_12 = open(f"{path}/extr_data/data_ela/data_ela_12/data_ela_relax_12.txt","w+")
            ela_relax_13 = open(f"{path}/extr_data/data_ela/data_ela_13/data_ela_relax_13.txt","w+")
            ela_relax_14 = open(f"{path}/extr_data/data_ela/data_ela_14/data_ela_relax_14.txt","w+")
            ela_relax_15 = open(f"{path}/extr_data/data_ela/data_ela_15/data_ela_relax_15.txt","w+")
            ela_relax_16 = open(f"{path}/extr_data/data_ela/data_ela_16/data_ela_relax_16.txt","w+")
            ela_relax_17 = open(f"{path}/extr_data/data_ela/data_ela_17/data_ela_relax_17.txt","w+")
            ela_relax_18 = open(f"{path}/extr_data/data_ela/data_ela_18/data_ela_relax_18.txt","w+")
            ela_relax_19 = open(f"{path}/extr_data/data_ela/data_ela_19/data_ela_relax_19.txt","w+")

            # Extraction of the log LAMMPS log file
            ext_relax.sep_fichier(fichier_source,ela_relax_1,ela_relax_2,ela_relax_3,ela_relax_4,ela_relax_5,ela_relax_6,ela_relax_7,ela_relax_8,ela_relax_9,ela_relax_10,ela_relax_11,ela_relax_12,ela_relax_13,ela_relax_14,ela_relax_15,ela_relax_16,ela_relax_17,ela_relax_18,ela_relax_19,traitement)

            # Closure of the data files
            fichier_source.close()

            # Elastic compression datas
            ela_relax_1.close()
            ela_relax_2.close()
            ela_relax_3.close()
            ela_relax_4.close()
            ela_relax_5.close()
            ela_relax_6.close()
            ela_relax_7.close()
            ela_relax_8.close()
            ela_relax_9.close()
            ela_relax_10.close()
            ela_relax_11.close()
            ela_relax_12.close()
            ela_relax_13.close()
            ela_relax_14.close()
            ela_relax_15.close()
            ela_relax_16.close()
            ela_relax_17.close()
            ela_relax_18.close()
            ela_relax_19.close()
            print(path)
        # end if

        if traitement == 'gran':
            # Open and write in files data_ela_relax for elastic datas
            ela_gran_1 = open(f"{path}/extr_data/data_ela/data_ela_1/data_gran_1.txt","w+")
            ela_gran_2 = open(f"{path}/extr_data/data_ela/data_ela_2/data_gran_2.txt","w+")
            ela_gran_3 = open(f"{path}/extr_data/data_ela/data_ela_3/data_gran_3.txt","w+")
            ela_gran_4 = open(f"{path}/extr_data/data_ela/data_ela_4/data_gran_4.txt","w+")
            ela_gran_5 = open(f"{path}/extr_data/data_ela/data_ela_5/data_gran_5.txt","w+")
            ela_gran_6 = open(f"{path}/extr_data/data_ela/data_ela_6/data_gran_6.txt","w+")
            ela_gran_7 = open(f"{path}/extr_data/data_ela/data_ela_7/data_gran_7.txt","w+")
            ela_gran_8 = open(f"{path}/extr_data/data_ela/data_ela_8/data_gran_8.txt","w+")
            ela_gran_9 = open(f"{path}/extr_data/data_ela/data_ela_9/data_gran_9.txt","w+")
            ela_gran_10 = open(f"{path}/extr_data/data_ela/data_ela_10/data_gran_10.txt","w+")
            ela_gran_11 = open(f"{path}/extr_data/data_ela/data_ela_11/data_gran_11.txt","w+")
            ela_gran_12 = open(f"{path}/extr_data/data_ela/data_ela_12/data_gran_12.txt","w+")
            ela_gran_13 = open(f"{path}/extr_data/data_ela/data_ela_13/data_gran_13.txt","w+")
            ela_gran_14 = open(f"{path}/extr_data/data_ela/data_ela_14/data_gran_14.txt","w+")
            ela_gran_15 = open(f"{path}/extr_data/data_ela/data_ela_15/data_gran_15.txt","w+")
            ela_gran_16 = open(f"{path}/extr_data/data_ela/data_ela_16/data_gran_16.txt","w+")
            ela_gran_17 = open(f"{path}/extr_data/data_ela/data_ela_17/data_gran_17.txt","w+")
            ela_gran_18 = open(f"{path}/extr_data/data_ela/data_ela_18/data_gran_18.txt","w+")
            ela_gran_19 = open(f"{path}/extr_data/data_ela/data_ela_19/data_gran_19.txt","w+")

            # Extraction of the log LAMMPS log file
            ext_relax.sep_fichier(fichier_source,ela_gran_1,ela_gran_2,ela_gran_3,ela_gran_4,ela_gran_5,ela_gran_6,ela_gran_7,ela_gran_8,ela_gran_9,ela_gran_10,ela_gran_11,ela_gran_12,ela_gran_13,ela_gran_14,ela_gran_15,ela_gran_16,ela_gran_17,ela_gran_18,ela_gran_19,traitement)

            # Closure of the data files
            fichier_source.close()

            # Elastic compression datas
            ela_gran_1.close()
            ela_gran_2.close()
            ela_gran_3.close()
            ela_gran_4.close()
            ela_gran_5.close()
            ela_gran_6.close()
            ela_gran_7.close()
            ela_gran_8.close()
            ela_gran_9.close()
            ela_gran_10.close()
            ela_gran_11.close()
            ela_gran_12.close()
            ela_gran_13.close()
            ela_gran_14.close()
            ela_gran_15.close()
            ela_gran_16.close()
            ela_gran_17.close()
            ela_gran_18.close()
            ela_gran_19.close()
            print(path)
        # end if
    # end of i for loop

    print("Graph print : ","\n", "Do you want graphs ? yes/no (default no)")
    choice = input()

    if (choice == "yes"):
        relax1 = open(f"{path}/extr_data/data_ela/data_ela_1/data_ela_relax_1.txt","r")
        relax3 = open(f"{path}/extr_data/data_ela/data_ela_3/data_ela_relax_3.txt","r")
        relax5 = open(f"{path}/extr_data/data_ela/data_ela_5/data_ela_relax_5.txt","r")
        relax8 = open(f"{path}/extr_data/data_ela/data_ela_8/data_ela_relax_8.txt","r")
        relax11 = open(f"{path}/extr_data/data_ela/data_ela_11/data_ela_relax_11.txt","r")
        relax19 = open(f"{path}/extr_data/data_ela/data_ela_19/data_ela_relax_19.txt","r")

        g.graph_ela_relax(relax1,relax3,relax5,relax8,relax11,relax19)

        relax1.close()
        relax3.close()
        relax5.close()
        relax8.close()
        relax11.close()
        relax19.close()
    # end if
# end if

# End