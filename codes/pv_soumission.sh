#!/bin/bash

#SBATCH --nodes=1                # number of nodes
#SBATCH --cpus-per-task=1        # number of processes
#SBATCH --mem-per-cpu=2048M      # memory; default unit is megabytes
#SBATCH --time=0-00:15           # time (DD-HH:MM)

module load gcc/9.3.0 paraview-offscreen/9.3.1
cd ./paraview_national/codes
pvbatch --force-offscreen-rendering writeImage.py
