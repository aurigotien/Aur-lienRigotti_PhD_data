#!/bin/bash 

#OAR -n python3.0
#OAR -l /nodes=1/core=1,walltime=100:00:00

# Module loading 

source /soft/env.bash

module load python/python3.9

num_simu=simu_5 # simu_N need to be modified for new stack of simulation

cd /data/failles/rigottia/Documents/stacks/

mkdir $num_simu

for i in `seq 1 30`; # create 30 files run_i to store the result files
do #{	
	cd /data/failles/rigottia/Documents/stacks/
	mkdir $num_simu
	mkdir code_copy

	cd /data/failles/rigottia/Documents/stacks/code_copy/
	mkdir prep_$num_simu

	cd /data/failles/rigottia/Documents/stacks/code_copy/prep_$num_simu/
	mkdir python_copy 
	mkdir lammps_copy

	cd /data/failles/rigottia/Documents/stacks/$num_simu/
        mkdir run_$i

	cd /data/failles/rigottia/Documents/stacks/$num_simu/run_$i/
        mkdir extr_data
	mkdir simulation

	cd /data/failles/rigottia/Documents/stacks/$num_simu/run_$i/simulation/
	touch rand_config.lj

	cd /data/failles/rigottia/Documents/Bash
	cp lammps_OAR.sh /data/failles/rigottia/Documents/stacks/$num_simu/run_$i/simulation/
	cp lammps_relax_OAR.sh /data/failles/rigottia/Documents/stacks/$num_simu/run_$i/simulation/

        cd /data/failles/rigottia/Documents/stacks/$num_simu/run_$i/extr_data/
        mkdir data
        mkdir data_ela

        cd /data/failles/rigottia/Documents/stacks/$num_simu/run_$i/extr_data/data/
        touch data_comp.txt
        touch data_relax.txt
        touch data_cis.txt
	
	for j in `seq 1 16`; # create 15 data_ela directory
       	do #{
        	cd /data/failles/rigottia/Documents/stacks/$num_simu/run_$i/extr_data/data_ela/
        	mkdir data_ela_$j # create file to stock the extracted datas

        	cd /data/failles/rigottia/Documents/stacks/$num_simu/run_$i/extr_data/data_ela/data_ela_$j/
        	touch data_ela_comp_$j.txt
                touch data_ela_cis_$j.txt
		touch data_ela_relax_$j.txt
	done #}

done #}

# copy source code + create rand_config.txt file for LAMMPS simulation
cd /data/failles/rigottia/Documents/python/preparation/
cp * /data/failles/rigottia/Documents/stacks/code_copy/prep_$num_simu/python_copy/

cd /data/failles/rigottia/Documents/Code_source/
cp * /data/failles/rigottia/Documents/stacks/code_copy/prep_$num_simu/lammps_copy/

cd /data/failles/rigottia/Documents/python/preparation/
python3 Simulation.py

# end
