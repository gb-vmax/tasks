#!/bin/bash
set -e
cd /home/user

mkdir -p /home/user/ml_experiments/artifacts && touch /home/user/ml_experiments/artifacts/experiment.log && echo -e "\nArtifacts directory and experiment log file are ready.\nDirectory: /home/user/ml_experiments/artifacts\nLog file: /home/user/ml_experiments/artifacts/experiment.log\n"
