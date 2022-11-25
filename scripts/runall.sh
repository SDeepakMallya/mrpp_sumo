#!/bin/bash

ssh -l arms04 10.141.200.4 ./display.sh


python3 config_simulate.py ppa_exhaustive 0
python3 config_simulate.py ppa_exhaustive 3
python3 config_simulate.py ppa_exhaustive 5

ssh -l arms04 10.141.200.4 ./display.sh

python3 config_simulate.py ppa_random 0
python3 config_simulate.py ppa_random 3
python3 config_simulate.py ppa_random 5

ssh -l arms04 10.141.200.4 ./display.sh
