## Fonctions   

# this function take as argument the lammps log file and create 5 files : data_com, data_relax data_cis, data_ela_comp, data_ela_cis
def sep_fichier(log,f1,f2,f3,f4,f_ela_comp_1,f_ela_comp_2,f_ela_comp_3,f_ela_comp_4,f_ela_comp_5,f_ela_comp_6,f_ela_comp_7,f_ela_comp_8,f_ela_comp_9,f_ela_comp_10,f_ela_comp_11,f_ela_comp_12,f_ela_comp_13,f_ela_comp_14,f_ela_comp_15,f_ela_comp_16,f_ela_comp_17,f_ela_comp_18,f_ela_comp_19,f_ela_cis_1,f_ela_cis_2,f_ela_cis_3,f_ela_cis_4,f_ela_cis_5,f_ela_cis_6,f_ela_cis_7,f_ela_cis_8,f_ela_cis_9,f_ela_cis_10,f_ela_cis_11,f_ela_cis_12,f_ela_cis_13,f_ela_cis_14,f_ela_cis_15,f_ela_cis_16,f_ela_cis_17,f_ela_cis_18,f_ela_cis_19,traitement):
    ## Function variable
    # 0 -> nothing is write
    # i -> write in the file no i
    # N -> end of the program 
    ecriture = 0 # defining if something is write or not
    bloc = 0 # filter num data + head of the data column
    bloc_ela_comp = 1 # write in files comp_ela
    bloc_ela_cis = 1 # write in files cis_ela
    
    if traitement == 'sh' :
        max_ecriture = 5
    elif traitement == 'sh_ela' or traitement == 'ela':
        max_ecriture = 43
    # end if
    
    iteration = 0 # loop while counter
    it_max = 26000 # max iteration of while loop
    
    # limit of the blocs
    dbt_comp = str('## End of compression ##') # begining of the compression file
    fin_comp = str('### End of compression step ###') # end of the compression file
    dbt_relax = str('## End of relaxation ##') # begining of the relaxation file
    fin_relax = str('### End of relaxation step ###') # end of the relaxation file
    dbt_precomp = str('## End of precompression  ##') # begining of the relaxation file
    fin_precomp = str('### End of precompression step ###') # end of the relaxation file
    dbt_cis = str('## End of shearing ##') # begining of the shearing file
    fin_cis = str('### End of shearing step ###')  # end of the shearing file
    
    dbt_ela_comp = str('## End of elastic compression ##') # begining of the elastic compression file
    fin_ela_comp = str('### End of elastic compression step ###') # end of the elastic compression file
    dbt_ela_cis = str('## End of elastic shearing ##') # begining of the elastic shearing file
    fin_ela_cis = str('### End of elastic shearing step ###') # end of the elastic shearing file
    
    fin_fichier_cut = str('Last command:')
    fin_fichier = str('Total wall time:')
    
    bloc_sup = 'Per MPI rank memory' # bloc are used to remove the text of the log file 
    bloc_inf = 'Loop time'
    
    ## Split log.lammps in the right files
    while ecriture < max_ecriture and iteration < it_max: # scan the whole file
        ligne = log.readline().strip() # read the LAMMPS log file line by line
        
        # stop the treatement
        if (fin_fichier_cut in ligne) or (fin_fichier in ligne) : # end of the file reached
            ecriture = max_ecriture 
        # end if
        
        # stop writting in files
        if traitement == 'sh' or traitement == 'sh_ela':
            if ligne == fin_comp or ligne == fin_relax or ligne == fin_precomp or ligne == fin_cis : # if reach the end of a file
                ecriture = 0 # nothing written in the file for ecriture = 0
            # end if 
        # end if
        
        # stop writting in ela files
        if traitement == 'sh_ela' or traitement == 'ela':
            if ligne == fin_ela_comp : # if reach the end of an elastic prop file
                ecriture = 0 
                bloc_ela_comp = bloc_ela_comp + 1 # go to next elastic property bloc
            # end if 
        
            if (ligne == fin_ela_cis): # if reach the end of an elastic prop file
                if ecriture == max_ecriture - 1 :
                    ecriture = max_ecriture
                else :
                    ecriture = 0
                    bloc_ela_cis = bloc_ela_cis + 1 # go to next elastic property bloc
                # end if 
            # end if
        # end if 
        
        # filter numeric datas + head of the data columns
        if (ecriture != 0) and (ecriture != max_ecriture) :  # if ecriture == 1....35
            if bloc_sup in ligne : # reach the begining of a bloc
                bloc = 1 # write in the file 'compression'
            elif bloc_inf in ligne : # reach the end of a bloc
                bloc = 0 # stop writting
            # end if 
        # end if 
        
        # write in file
        # data comp and cis
        if bloc_sup not in ligne : 
        # write in files comp, and cis
            if traitement == 'sh' or traitement == 'sh_ela':
                if ecriture == 1 and bloc == 1:
                    f1.write(ligne+'\n') # write in the compression file
                elif ecriture == 2 and bloc == 1:
                    f2.write(ligne+'\n') # write in the relaxation file
                elif ecriture == 3 and bloc == 1:
                    f3.write(ligne+'\n') # write in the pre_comp file
                elif ecriture == 4 and bloc == 1:
                    f4.write(ligne+'\n') # write in the shearing file
                # end if 
            # end if
                
         # write in files ela_comp and ela_cis
         # elastic compression
            if traitement == 'sh_ela' or traitement == 'ela':
                if ecriture == 5 and bloc == 1:
                    f_ela_comp_1.write(ligne+'\n') # write in elastic compression file 1
                elif ecriture == 6 and bloc == 1:
                    f_ela_comp_2.write(ligne+'\n') # write in elastic compression file 2
                elif ecriture == 7 and bloc == 1:
                    f_ela_comp_3.write(ligne+'\n') # write in elastic compression file 3
                elif ecriture == 8 and bloc == 1:
                    f_ela_comp_4.write(ligne+'\n') # write in elastic compression file 4
                elif ecriture == 9 and bloc == 1:
                    f_ela_comp_5.write(ligne+'\n') # write in elastic compression file 5
                elif ecriture == 10 and bloc == 1:
                    f_ela_comp_6.write(ligne+'\n') # write in elastic compression file 6
                elif ecriture == 11 and bloc == 1:
                    f_ela_comp_7.write(ligne+'\n') # write in elastic compression file 7
                elif ecriture == 12 and bloc == 1:
                    f_ela_comp_8.write(ligne+'\n') # write in elastic compression file 8
                elif ecriture == 13 and bloc == 1:
                    f_ela_comp_9.write(ligne+'\n') # write in elastic compression file 9
                elif ecriture == 14 and bloc == 1:
                    f_ela_comp_10.write(ligne+'\n') # write in elastic compression file 10
                elif ecriture == 15 and bloc == 1:
                    f_ela_comp_11.write(ligne+'\n') # write in elastic compression file 11
                elif ecriture == 16 and bloc == 1:
                    f_ela_comp_12.write(ligne+'\n') # write in elastic compression file 12
                elif ecriture == 17 and bloc == 1:
                    f_ela_comp_13.write(ligne+'\n') # write in elastic compression file 13
                elif ecriture == 18 and bloc == 1:
                    f_ela_comp_14.write(ligne+'\n') # write in elastic compression file 14
                elif ecriture == 19 and bloc == 1:
                    f_ela_comp_15.write(ligne+'\n') # write in elastic compression file 15
                elif ecriture == 20 and bloc == 1:
                    f_ela_comp_16.write(ligne+'\n') # write in elastic compression file 16
                elif ecriture == 21 and bloc == 1:
                    f_ela_comp_17.write(ligne+'\n') # write in elastic compression file 17
                elif ecriture == 22 and bloc == 1:
                    f_ela_comp_18.write(ligne+'\n') # write in elastic compression file 18
                elif ecriture == 23 and bloc == 1:
                    f_ela_comp_19.write(ligne+'\n') # write in elastic compression file 19
                # end if 
                    
             # elastic shearing
                if ecriture == 24 and bloc == 1:
                    f_ela_cis_1.write(ligne+'\n') # write in elastic shearing file 1
                elif ecriture == 25 and bloc == 1:
                    f_ela_cis_2.write(ligne+'\n') # write in elastic shearing file 2
                elif ecriture == 26 and bloc == 1:
                    f_ela_cis_3.write(ligne+'\n') # write in elastic shearing file 3
                elif ecriture == 27 and bloc == 1:
                    f_ela_cis_4.write(ligne+'\n') # write in elastic shearing file 4
                elif ecriture == 28 and bloc == 1:
                    f_ela_cis_5.write(ligne+'\n') # write in elastic shearing file 5
                elif ecriture == 29 and bloc == 1:
                    f_ela_cis_6.write(ligne+'\n') # write in elastic shearing file 6
                elif ecriture == 30 and bloc == 1:
                    f_ela_cis_7.write(ligne+'\n') # write in elastic shearing file 7
                elif ecriture == 31 and bloc == 1:
                    f_ela_cis_8.write(ligne+'\n') # write in elastic shearing file 8
                elif ecriture == 32 and bloc == 1:
                    f_ela_cis_9.write(ligne+'\n') # write in elastic shearing file 9
                elif ecriture == 33 and bloc == 1:
                    f_ela_cis_10.write(ligne+'\n') # write in elastic shearing file 10
                elif ecriture == 34 and bloc == 1:
                    f_ela_cis_11.write(ligne+'\n') # write in elastic shearing file 11
                elif ecriture == 35 and bloc == 1:
                    f_ela_cis_12.write(ligne+'\n') # write in elastic shearing file 12
                elif ecriture == 36 and bloc == 1:
                    f_ela_cis_13.write(ligne+'\n') # write in elastic shearing file 13
                elif ecriture == 37 and bloc == 1:
                    f_ela_cis_14.write(ligne+'\n') # write in elastic shearing file 14
                elif ecriture == 38 and bloc == 1:
                    f_ela_cis_15.write(ligne+'\n') # write in elastic shearing file 15
                elif ecriture == 39 and bloc == 1:
                    f_ela_cis_16.write(ligne+'\n') # write in elastic shearing file 16
                elif ecriture == 40 and bloc == 1:
                    f_ela_cis_17.write(ligne+'\n') # write in elastic shearing file 17
                elif ecriture == 41 and bloc == 1:
                    f_ela_cis_18.write(ligne+'\n') # write in elastic shearing file 18
                elif ecriture == 42 and bloc == 1:
                    f_ela_cis_19.write(ligne+'\n') # write in elastic shearing file 19
                # end if
            # end if 
        # end if
        
        # search for the beginning of the datas   
            if ecriture == 0 : # if the file is not currently writing in a file
                if traitement == 'sh' or traitement == 'sh_ela':
                    if ligne == dbt_comp: # search for the begining of the compression file
                        ecriture = 1
                    elif ligne == dbt_relax: # search for the begining of the relaxation file
                        ecriture = 2
                    elif ligne == dbt_precomp: # search the begining of the shearing file
                        ecriture = 3
                    elif ligne == dbt_cis: # search the begining of the shearing file
                        ecriture = 4
                    # end if
                # end if
                    
                # elastc datas
                if traitement == 'sh_ela' or traitement == 'ela':
                    # elastic compression
                    if ligne == dbt_ela_comp :
                        if bloc_ela_comp == 1 : # search the begining of elastic compression file 1
                            ecriture = 5
                        elif bloc_ela_comp == 2 : # search the begining of elastic compression file 2
                            ecriture = 6
                        elif bloc_ela_comp == 3 : # search the begining of elastic compression file 3
                            ecriture = 7
                        elif bloc_ela_comp == 4 : # search the begining of elastic compression file 4
                            ecriture = 8
                        elif bloc_ela_comp == 5 : # search the begining of elastic compression file 5
                            ecriture = 9
                        elif bloc_ela_comp == 6 : # search the begining of elastic compression file 6
                            ecriture = 10
                        elif bloc_ela_comp == 7 : # search the begining of elastic compression file 7
                            ecriture = 11
                        elif bloc_ela_comp == 8 : # search the begining of elastic compression file 8
                            ecriture = 12
                        elif bloc_ela_comp == 9 : # search the begining of elastic compression file 9
                            ecriture = 13
                        elif bloc_ela_comp == 10 : # search the begining of elastic compression file 10
                            ecriture = 14
                        elif bloc_ela_comp == 11 : # search the begining of elastic compression file 11
                            ecriture = 15
                        elif bloc_ela_comp == 12 : # search the begining of elastic compression file 12
                            ecriture = 16
                        elif bloc_ela_comp == 13 : # search the begining of elastic compression file 13
                            ecriture = 17
                        elif bloc_ela_comp == 14 : # search the begining of elastic compression file 14
                            ecriture = 18
                        elif bloc_ela_comp == 15 : # search the begining of elastic compression file 15
                            ecriture = 19
                        elif bloc_ela_comp == 16 : # search the begining of elastic compression file 16
                            ecriture = 20
                        elif bloc_ela_comp == 17 : # search the begining of elastic compression file 17
                            ecriture = 21
                        elif bloc_ela_comp == 18 : # search the begining of elastic compression file 18
                            ecriture = 22
                        elif bloc_ela_comp == 19 : # search the begining of elastic compression file 18
                            ecriture = 23
                
                    # elastic shearing
                    elif ligne == dbt_ela_cis :
                        if bloc_ela_cis == 1 : # search the begining of elastic shearing file 1
                            ecriture = 24
                        elif bloc_ela_cis == 2 : # search the begining of elastic shearing file 2
                            ecriture = 25
                        elif bloc_ela_cis == 3 : # search the begining of elastic shearing file 3
                            ecriture = 26
                        elif bloc_ela_cis == 4 : # search the begining of elastic shearing file 4
                            ecriture = 27
                        elif bloc_ela_cis == 5 : # search the begining of elastic shearing file 5
                            ecriture = 28
                        elif bloc_ela_cis == 6 : # search the begining of elastic shearing file 6
                            ecriture = 29
                        elif bloc_ela_cis == 7 : # search the begining of elastic shearing file 7
                            ecriture = 30
                        elif bloc_ela_cis == 8 : # search the begining of elastic shearing file 8
                            ecriture = 31
                        elif bloc_ela_cis == 9 : # search the begining of elastic shearing file 9
                            ecriture = 32
                        elif bloc_ela_cis == 10 : # search the begining of elastic shearing file 10
                            ecriture = 33
                        elif bloc_ela_cis == 11 : # search the begining of elastic shearing file 11
                            ecriture = 34
                        elif bloc_ela_cis == 12 : # search the begining of elastic shearing file 12
                            ecriture = 35
                        elif bloc_ela_cis == 13 : # search the begining of elastic shearing file 13
                            ecriture = 36
                        elif bloc_ela_cis == 14 : # search the begining of elastic shearing file 14
                            ecriture = 37
                        elif bloc_ela_cis == 15 : # search the begining of elastic shearing file 15
                            ecriture = 38
                        elif bloc_ela_cis == 16 : # search the begining of elastic shearing file 16
                            ecriture = 39
                        elif bloc_ela_cis == 17 : # search the begining of elastic shearing file 17
                            ecriture = 40
                        elif bloc_ela_cis == 18 : # search the begining of elastic shearing file 18
                            ecriture = 41
                        elif bloc_ela_cis == 19 : # end of the file writing
                            ecriture = 42
                    # end if 
                # end if 
            # end if
        iteration = iteration + 1 # count the number of iteration to avoid infinite loop
    #print("iteration = ", iteration)
    return