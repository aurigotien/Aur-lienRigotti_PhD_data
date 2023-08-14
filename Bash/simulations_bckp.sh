#!/bin/bash 

num_simu=simu_1 # simu_N need to be modified for new stack of simulation

cd /home/rigottia/Nextcloud/Documents/data_simu/stacks/

if [ -d "$(find "/home/rigottia/Nextcloud/Documents/data_simu/stacks/$num_simu/" -maxdepth 0 2>/dev/null)" ]; then #{
	echo "dir $num_simu already exist"
else 
	mkdir $num_simu
fi #}

for i in `seq 1 30`; # create 30 files run_i to store the result files
do #{
	cd /home/rigottia/Nextcloud/Documents/data_simu/stacks/$num_simu/
        mkdir run_$i

	cd /home/rigottia/Nextcloud/Documents/data_simu/stacks/$num_simu/run_$i/
        mkdir extr_data
	mkdir simulation

	cd /home/rigottia/Nextcloud/Documents/data_simu/stacks/$num_simu/run_$i/simulation/
	touch rand_config.lj

        cd /home/rigottia/Nextcloud/Documents/data_simu/stacks/$num_simu/run_$i/extr_data/
        mkdir data
        mkdir data_ela
	mkdir velocity
	mkdir temp 

        cd /home/rigottia/Nextcloud/Documents/data_simu/stacks/$num_simu/run_$i/extr_data/data/
        touch data_comp.txt
        touch data_relax.txt
        touch data_cis.txt
		
	for j in `seq 1 16`; # create 15 data_ela directory
       	do #{
        	cd /home/rigottia/Nextcloud/Documents/data_simu/stacks/$num_simu/run_$i/extr_data/data_ela/
        	mkdir data_ela_$j # create file to stock the extracted datas

        	cd /home/rigottia/Nextcloud/Documents/data_simu/stacks/$num_simu/run_$i/extr_data/data_ela/data_ela_$j/
        	touch data_ela_comp_$j.txt
                touch data_ela_cis_$j.txt
	done #}

	for i in `seq 1 7`; # create 7 velocity files 
        do #{
        	cd /home/rigottia/Nextcloud/Documents/data_simu/stacks/$num_simu/run_1/extr_data/velocity/
        	touch vel_$i.txt
	done #}

done #}

# copy source code + create rand_config.txt file for LAMMPS simulation
cd /home/rigottia/Nextcloud/Documents/python/preparation/
python3 Simulation.py

for i in `1 11 21`; # iteration from 1 to 30 (1 11 21)
do #{
	echo "iteration : $i ---------------------------------------------------------------------------"
	# run LAMMPS simulation
	if [ -d "$(find"/home/rigottia/Nextcloud/Documents/data_simu/stacks/$num_simu/run_$i/extr_data/data/" -maxdepth 0 2>/dev/null)" ]; then #{
		echo "run_$i has already been done"
	else
		cd /home/rigottia/Nextcloud/Documents/data_simu/stacks/$num_simu/run_$i/simulation/
		lmp_stable -in in.floes_simulation.lmp &
		cd /home/rigottia/Nextcloud/Documents/data_simu/stacks/$num_simu/run_$((i+1))/simulation/
		lmp_stable -in in.floes_simulation.lmp &
		cd /home/rigottia/Nextcloud/Documents/data_simu/stacks/$num_simu/run_$((i+2))/simulation/
 		lmp_stable -in in.floes_simulation.lmp &
		cd /home/rigottia/Nextcloud/Documents/data_simu/stacks/$num_simu/run_$((i+3))/simulation/
		lmp_stable -in in.floes_simulation.lmp &
		cd /home/rigottia/Nextcloud/Documents/data_simu/stacks/$num_simu/run_$((i+4))/simulation/
        	lmp_stable -in in.floes_simulation.lmp &
		cd /home/rigottia/Nextcloud/Documents/data_simu/stacks/$num_simu/run_$((i+5))/simulation/
		lmp_stable -in in.floes_simulation.lmp &
                cd /home/rigottia/Nextcloud/Documents/data_simu/stacks/$num_simu/run_$((i+6))/simulation/
		lmp_stable -in in.floes_simulation.lmp &
                cd /home/rigottia/Nextcloud/Documents/data_simu/stacks/$num_simu/run_$((i+7))/simulation/
		lmp_stable -in in.floes_simulation.lmp &
               	cd /home/rigottia/Nextcloud/Documents/data_simu/stacks/$num_simu/run_$((i+8))/simulation/
		lmp_stable -in in.floes_simulation.lmp &
                cd /home/rigottia/Nextcloud/Documents/data_simu/stacks/$num_simu/run_$((i+9))/simulation/
		lmp_stable -in in.floes_simulation.lmp
	fi #}
	echo "iteration $i finish"
done #}
	
for i in `seq 1 10`: 
do #{
	cd /home/rigottia/Nextcloud/Documents/data_simu/stacks/$num_simu/run_$i/simulation/
	for j in $( ls endo.* );
        do #{
                rm $j
       	done #}
done #}

# run LAMMPS log file extraction via python 
cd /home/rigottia/Nextcloud/Documents/python/extraction/
#python3 traitement_log.py

# end
