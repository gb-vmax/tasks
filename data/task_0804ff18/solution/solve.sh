#!/bin/bash
set -e
cd /home/user

python3 -c "import pandas" 2>/dev/null && echo 'already' || echo 'not'
pip3 install --user pandas
python3 -c "import pandas; print(pandas.__version__)"
mkdir -p /home/user/dataset_setup && echo -e "pandas installed\npandas version: 2.3.3" > /home/user/dataset_setup/package_log.txt
cat /home/user/dataset_setup/package_log.txt
