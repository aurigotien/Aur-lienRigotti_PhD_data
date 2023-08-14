#!/bin/bash 

num_simu=simu_107 # simu_N need to be modified for new stack of simulation

i=1 # number of the simulation to run 

cd /data/failles/rigottia/Documents/stacks/$num_simu/run_$i/simulation/
oarsub -S --project iste-equ-failles ./lammps_OAR.sh --notify "mail:aurelien.rigotti@univ-grenoble-alpes.fr"

# end
