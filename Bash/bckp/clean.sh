#!/bin/bash

# remove ela file

num_simu=simu_3
#i=1

for i in `seq 1 30`;
do #{
	cd /data/failles/rigottia/Documents/stacks/$num_simu/run_$i/simulation/
	echo "/home/rigottia/Nextcloud/Documents/stacks/$num_simu/run_$i/simulation/"
	for j in `seq 1 9`; do #{
		for k in $( ls endo.restart.$j* ); do #{
			rm $k
		done #}
	done #}

	for l in $( ls relaxation.* ); do #{
		rm $l
	done #} 

	for m in $( ls pre_comp.* ); do #{
		rm $m
	done #}

	rm *.jpg
	rm *.jpg
	rm *.jpg
	rm OAR.*
	rm lammps_OAR.sh
done #}

echo "Elastic files removed" 
