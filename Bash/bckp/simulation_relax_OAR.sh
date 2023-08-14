#!/bin/bash 

num_simu=simu_2 # simu_N need to be modified for new stack of simulation

for i in `seq 1 30`; # iteration from 1 to 30
do #{
	#run LAMMPS simulations
		cd /home/rigottia/Nextcloud/Documents/stacks/$num_simu/run_$i/simulation/
		oarsub -S --project iste-equ-failles ./lammps_relax_OAR.sh --notify "mail:aurelien.rigotti@univ-grenoble-alpes.fr"
done #}

# end
