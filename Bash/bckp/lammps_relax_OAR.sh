#!/bin/bash

# OAR -n lammps
# OAR -l/nodes=1/core=1,walltime=100:00:00

# Module loading

source /soft/env.bash
module load lammps/29092021_gcc_10.2.0

echo "stack = $stacks"
echo "num simu = $num_simu"
echo "run = $no_run"

lmp -in in.floes_simu_relax.lmp

# end
