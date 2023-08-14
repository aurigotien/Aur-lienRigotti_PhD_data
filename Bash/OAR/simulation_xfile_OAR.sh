#!/bin/bash 

num_simu=simu_108 # simu_N need to be modified for new stack of simulation

run_simu="1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20" # simu_ to rerun 

for i in $run_simu
do #{
	cd /data/failles/rigottia/Documents/stacks/$num_simu/run_$i/simulation/
	oarsub -S --project iste-equ-failles ./lammps_OAR.sh --notify "mail:aurelien.rigotti@univ-grenoble-alpes.fr"
done #}
# end
