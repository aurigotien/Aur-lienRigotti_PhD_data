#!/bin/bash 

num_simu=simu_8 # simu_N need to be modified for new stack of simulation

cd /home/rigottia/Nextcloud/Documents/stacks/

mkdir $num_simu

for i in `seq 1 30`; # create 30 files run_i to store the result files
do #{	
	cd /home/rigottia/Nextcloud/Documents/stacks/
	mkdir $num_simu
	mkdir code_copy

	cd /home/rigottia/Nextcloud/Documents/stacks/code_copy/
	mkdir prep_$num_simu

	cd /home/rigottia/Nextcloud/Documents/stacks/code_copy/prep_$num_simu/
	mkdir python_copy 
	mkdir lammps_copy

	cd /home/rigottia/Nextcloud/Documents/stacks/$num_simu/
        mkdir run_$i

	cd /home/rigottia/Nextcloud/Documents/stacks/$num_simu/run_$i/
        mkdir extr_data
	mkdir simulation

	cd /home/rigottia/Nextcloud/Documents/stacks/$num_simu/run_$i/simulation/
	touch rand_config.lj

        cd /home/rigottia/Nextcloud/Documents/stacks/$num_simu/run_$i/extr_data/
        mkdir data
        mkdir data_ela

        cd /home/rigottia/Nextcloud/Documents/stacks/$num_simu/run_$i/extr_data/data/
        touch data_comp.txt
        touch data_relax.txt
        touch data_cis.txt
		
	for j in `seq 1 16`; # create 15 data_ela directory
       	do #{
        	cd /home/rigottia/Nextcloud/Documents/stacks/$num_simu/run_$i/extr_data/data_ela/
        	mkdir data_ela_$j # create file to stock the extracted datas

        	cd /home/rigottia/Nextcloud/Documents/stacks/$num_simu/run_$i/extr_data/data_ela/data_ela_$j/
        	touch data_ela_comp_$j.txt
                touch data_ela_cis_$j.txt
	done #}
done #}

# end
