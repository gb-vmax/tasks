#!/bin/bash
set -e
cd /home/user

grep -E 'WARNING|ERROR' /home/user/logs/optim-solver.log > /home/user/alerts/optim-solver-alerts.log && cat /home/user/alerts/optim-solver-alerts.log
mkdir -p /home/user/alerts && grep -E 'WARNING|ERROR' /home/user/logs/optim-solver.log > /home/user/alerts/optim-solver-alerts.log && cat /home/user/alerts/optim-solver-alerts.log
