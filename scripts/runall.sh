#!/bin/bash

ssh -l arms04 10.141.200.4 ./display.sh

python3 config_simulate.py ppa_sampled 0

ssh -l arms04 10.141.200.4 ./display.sh

python3 config_simulate.py ppa_sampled 3

ssh -l arms04 10.141.200.4 ./display.sh

python3 config_simulate.py ppa_sampled 5

ssh -l arms04 10.141.200.4 ./display.sh
