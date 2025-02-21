## Fonctions

# this function take as argument the lammps log file and create 5 files : data_com, data_relax data_cis, data_ela_comp, data_ela_cis
def sep_fichier(log,f_ela_relax_1,f_ela_relax_2,f_ela_relax_3,f_ela_relax_4,f_ela_relax_5,f_ela_relax_6,f_ela_relax_7,f_ela_relax_8,f_ela_relax_9,f_ela_relax_10,f_ela_relax_11,f_ela_relax_12,f_ela_relax_13,f_ela_relax_14,f_ela_relax_15,f_ela_relax_16,f_ela_relax_17,f_ela_relax_18,f_ela_relax_19,traitement):
    ## Function variable
    # 0 -> nothing is write
    # i -> write in the file no i
    # N -> end of the program
    ecriture = 0 # defining if something is write or not
    bloc = 0 # filter num data + head of the data column
    bloc_ela_relax = 1 # write in files relax_ela
    end_check = 0 # check if the program reach the last line of the data file

    iteration = 0 # loop while counter
    it_max = 20000 # max iteration of while loop

    # limit of the blocs
    if traitement == 'relax':
        dbt_ela_relax = str('## End of elastic relaxation ##') # begining of the elastic shearing file
        fin_ela_relax = str('### End of elastic relaxation step ###') # end of the elastic shearing file
    if traitement == 'gran':
        dbt_ela_relax = str('## End of elastic relaxation ##') # begining of the elastic shearing file
        fin_ela_relax = str('### End of granulence computation ###') # end of the elastic shearing file
    # end if

    bloc_sup = 'Per MPI rank memory' # bloc are used to remove the text of the log file
    bloc_inf = 'Loop time'

    ## Split log.lammps in 36 files
    while ecriture < 20 and iteration < it_max: # scan the whole file
        ligne = log.readline().strip() # read the LAMMPS log file line by line

        # stop writting in ela_ files
        if ligne == fin_ela_relax : # if reach the end of an elastic prop file
            if ecriture == 19 :
                ecriture = 20
            else :
                ecriture = 0
                bloc_ela_relax = bloc_ela_relax + 1 # go to next elastic property bloc
        # end if

        # filter numeric datas + head of the data columns
        if ecriture != 0 and ecriture != 33 :  # if ecriture == 1....16
            if bloc_sup in ligne : # reach the begining of a bloc
                bloc = 1 # write in the file 'relaxation'
            elif bloc_inf in ligne : # reach the end of a bloc
                bloc = 0 # stop writting
            # end if
        # end if

        # wrtie in file
        # data comp and cis
        if bloc_sup not in ligne :
         # write in files ela_relax
         # write in elastic shear relaxation files
            if ecriture == 1 and bloc == 1:
                f_ela_relax_1.write(ligne+'\n') # write in elastic relaxation file 1

            elif ecriture == 2 and bloc == 1:
                f_ela_relax_2.write(ligne+'\n') # write in elastic relaxation file 2

            elif ecriture == 3 and bloc == 1:
                f_ela_relax_3.write(ligne+'\n') # write in elastic relaxation file 3

            elif ecriture == 4 and bloc == 1:
                f_ela_relax_4.write(ligne+'\n') # write in elastic relaxation file 4

            elif ecriture == 5 and bloc == 1:
                f_ela_relax_5.write(ligne+'\n') # write in elastic relaxation file 5

            elif ecriture == 6 and bloc == 1:
                f_ela_relax_6.write(ligne+'\n') # write in elastic relaxation file 6

            elif ecriture == 7 and bloc == 1:
                f_ela_relax_7.write(ligne+'\n') # write in elastic relaxation file 7

            elif ecriture == 8 and bloc == 1:
                f_ela_relax_8.write(ligne+'\n') # write in elastic relaxation file 8

            elif ecriture == 9 and bloc == 1:
                f_ela_relax_9.write(ligne+'\n') # write in elastic relaxation file 9

            elif ecriture == 10 and bloc == 1:
                f_ela_relax_10.write(ligne+'\n') # write in elastic relaxation file 10

            elif ecriture == 11 and bloc == 1:
                f_ela_relax_11.write(ligne+'\n') # write in elastic relaxation file 11

            elif ecriture == 12 and bloc == 1:
                f_ela_relax_12.write(ligne+'\n') # write in elastic relaxation file 12

            elif ecriture == 13 and bloc == 1:
                f_ela_relax_13.write(ligne+'\n') # write in elastic relaxation file 13

            elif ecriture == 14 and bloc == 1:
                f_ela_relax_14.write(ligne+'\n') # write in elastic relaxation file 14

            elif ecriture == 15 and bloc == 1:
                f_ela_relax_15.write(ligne+'\n') # write in elastic relaxation file 15

            elif ecriture == 16 and bloc == 1:
                f_ela_relax_16.write(ligne+'\n') # write in elastic relaxation file 16

            elif ecriture == 17 and bloc == 1:
                f_ela_relax_17.write(ligne+'\n') # write in elastic relaxation file 17

            elif ecriture == 18 and bloc == 1:
                f_ela_relax_18.write(ligne+'\n') # write in elastic relaxation file 18

            elif ecriture == 19 and bloc == 1:
                f_ela_relax_19.write(ligne+'\n') # write in elastic relaxation file 19

        # search for the beginning of the datas
            if ecriture == 0 : # if the file is not currently writing in a file
                # elastic datas
                # elastic compression
                if ligne == dbt_ela_relax :
                    if bloc_ela_relax == 1 : # search the begining of elastic relaxation file 1
                        ecriture = 1
                    elif bloc_ela_relax == 2 : # search the begining of elastic relaxation file 2
                        ecriture = 2
                    elif bloc_ela_relax == 3 : # search the begining of elastic relaxation file 3
                        ecriture = 3
                    elif bloc_ela_relax == 4 : # search the begining of elastic relaxation file 4
                        ecriture = 4
                    elif bloc_ela_relax == 5 : # search the begining of elastic relaxation file 5
                        ecriture = 5
                    elif bloc_ela_relax == 6 : # search the begining of elastic relaxation file 6
                        ecriture = 6
                    elif bloc_ela_relax == 7 : # search the begining of elastic relaxation file 7
                        ecriture = 7
                    elif bloc_ela_relax == 8 : # search the begining of elastic relaxation file 8
                        ecriture = 8
                    elif bloc_ela_relax == 9 : # search the begining of elastic relaxation file 9
                        ecriture = 9
                    elif bloc_ela_relax == 10 : # search the begining of elastic relaxation file 10
                        ecriture = 10
                    elif bloc_ela_relax == 11 : # search the begining of elastic relaxation file 11
                        ecriture = 11
                    elif bloc_ela_relax == 12 : # search the begining of elastic relaxation file 12
                        ecriture = 12
                    elif bloc_ela_relax == 13 : # search the begining of elastic relaxation file 13
                        ecriture = 13
                    elif bloc_ela_relax == 14 : # search the begining of elastic relaxation file 14
                        ecriture = 14
                    elif bloc_ela_relax == 15 : # search the begining of elastic relaxation file 15
                        ecriture = 15
                    elif bloc_ela_relax == 16 : # search the begining of elastic relaxation file 16
                        ecriture = 16
                    elif bloc_ela_relax == 17 : # search the begining of elastic relaxation file 16
                        ecriture = 17
                    elif bloc_ela_relax == 18 : # search the begining of elastic relaxation file 16
                        ecriture = 18
                    elif bloc_ela_relax == 19 : # search the begining of elastic relaxation file 16
                        ecriture = 19
                        end_check = 1
                    # end if
                # end if
            # end if
        # end if
        iteration = iteration + 1 # count the number of iteration to avoid infinite loop
        #print('it = ', iteration/it_max, 'ecriture = ', ecriture)

    if end_check == 0 :
        print('Problem in the run')
    # end if

    #print("iteration = ", iteration)
    return