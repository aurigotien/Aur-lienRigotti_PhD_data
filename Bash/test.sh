#!/bin/bash 

num_simu=simu_1 # simu_N need to be modified for new stack of simulation
i=1

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
mkdir velocity

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

for k in `seq 1 13`; # create 13 velocity files 
do #{
       	cd /home/rigottia/Nextcloud/Documents/stacks/$num_simu/run_$i/extr_data/velocity/
       	mkdir temp
	touch vel_$k.txt

	cd /home/rigottia/Nextcloud/Documents/stacks/$num_simu/run_$i/extr_data/velocity/temp/
	touch vel_$k.txt
done #}

# copy source code + create rand_config.txt file for LAMMPS simulation
cd /home/rigottia/Nextcloud/Documents/python/preparation/
#cp * /home/rigottia/Nextcloud/Documents/stacks/code_copy/prep_$num_simu/python_copy/

cd /home/rigottia/Nextcloud/Documents/Code_source/
#cp * /home/rigottia/Nextcloud/Documents/stacks/code_copy/prep_$num_simu/lammps_copy/

cd /home/rigottia/Nextcloud/Documents/Code_source/visco_ela_relax/
#cp * /home/rigottia/Nextcloud/Documents/stacks/code_copy/prep_$num_simu/lammps_copy/

cd /home/rigottia/Nextcloud/Documents/stacks/code_copy/prep_$num_simu/python_copy/
#python3 Simulation.py

#cd /home/rigottia/Nextcloud/Documents/stacks/$num_simu/run_$i/simulation/
#mv log.lammps log_sh.lammps

echo "iteration : 1 ---------------------------------------------------------------------------"
# run LAMMPS simulation
if [ -d "$(find"/home/rigottia/Nextcloud/Documents/stacks/$num_simu/run_$i/extr_data/data/" -maxdepth 0 2>/dev/null)" ]; then #{
	echo "run_$i has already been done"
else
	cd /home/rigottia/Nextcloud/Documents/stacks/$num_simu/run_$i/simulation/
	#lmp_stable -in in.floes_simulation.lmp &
	lmp_stable -in in.floes_simu_relax.lmp
	fi #}
	echo "iteration 1 finish"
# end
