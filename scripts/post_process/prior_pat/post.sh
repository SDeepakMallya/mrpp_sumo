#!/bin/bash

python3 process_simulations.py ppa_sampled 0 && python3 process_simulations.py ppa_sampled 3 && python3 process_simulations.py ppa_sampled 5

ssh -l arms04 10.141.200.4 ./display.sh

