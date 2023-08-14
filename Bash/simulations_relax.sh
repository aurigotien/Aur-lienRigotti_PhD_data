#!/bin/bash 

num_simu=simu_1 # simu_N need to be modified for new stack of simulation

# copy source code + create rand_config.txt file for LAMMPS simulation
for i in `seq 1 30`;
do #{
	cd /home/rigottia/Nextcloud/Documents/stacks/$num_simu/run_$i/simulation/
	mv log.lammps log_sh.lammps
done #}

for i in 1 11 21; # iteration from 1 to 30 (1 11 21)
do #{
	echo "iteration : $i ---------------------------------------------------------------------------"
	
	#run LAMMPS simulation
        if [ -d "$(find"/home/rigottia/Nextcloud/Documents/stacks/$num_simu/run_$i/extr_data/data/" -maxdepth 0 2>/dev/null)" ]; then #{
		echo "run_$i has already been done"
	else
		cd /home/rigottia/Nextcloud/Documents/stacks/$num_simu/run_$i/simulation/
		lmp_stable -in in.floes_simu_relax.lmp &
		cd /home/rigottia/Nextcloud/Documents/stacks/$num_simu/run_$((i+1))/simulation/
		lmp_stable -in in.floes_simu_relax.lmp &
		cd /home/rigottia/Nextcloud/Documents/stacks/$num_simu/run_$((i+2))/simulation/
 		lmp_stable -in in.floes_simu_relax.lmp &
		cd /home/rigottia/Nextcloud/Documents/stacks/$num_simu/run_$((i+3))/simulation/
		lmp_stable -in in.floes_simu_relax.lmp &
		cd /home/rigottia/Nextcloud/Documents/stacks/$num_simu/run_$((i+4))/simulation/
        	lmp_stable -in in.floes_simu_relax.lmp &
		cd /home/rigottia/Nextcloud/Documents/stacks/$num_simu/run_$((i+5))/simulation/
		lmp_stable -in in.floes_simu_relax.lmp &
		cd /home/rigottia/Nextcloud/Documents/stacks/$num_simu/run_$((i+6))/simulation/
		lmp_stable -in in.floes_simu_relax.lmp &
                cd /home/rigottia/Nextcloud/Documents/stacks/$num_simu/run_$((i+7))/simulation/
		lmp_stable -in in.floes_simu_relax.lmp &
              	cd /home/rigottia/Nextcloud/Documents/stacks/$num_simu/run_$((i+8))/simulation/
		lmp_stable -in in.floes_simu_relax.lmp &
                cd /home/rigottia/Nextcloud/Documents/stacks/$num_simu/run_$((i+9))/simulation/
		lmp_stable -in in.floes_simu_relax.lmp
	fi #}
	echo "iteration $i finish"
done #}

# end
