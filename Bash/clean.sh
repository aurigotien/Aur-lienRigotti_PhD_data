#!/bin/bash

# remove ela file

num_simu=simu_1
#i=1

for i in `seq 1 30`;
do #{
	cd /home/rigottia/Nextcloud/Documents/stacks/$num_simu/run_$i/simulation/
	echo "/home/rigottia/Nextcloud/Documents/stacks/$num_simu/run_$i/simulation/"
	for j in $( ls endo.* ); do #{
		rm $j
	done #}
	for k in $( ls relaxation.* ); do #{
		rm $k
	done #} 
	for l in $( ls pre_comp.* ); do #{
		rm $l
	done #}
	rm *.jpg
	rm OAR.*
	rm lammps_OAR.sh

	cd /home/rigottia/Nextcloud/Documents/stacks_read/$num_simu/run_$i/extr_data/
	rm -r velocity
	rm -r temp
done #}

echo "Elastic files removed" 
