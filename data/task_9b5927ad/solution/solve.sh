#!/bin/bash
set -e
cd /home/user

mkdir -p /home/user/outputs/ && rm -f /home/user/outputs/*
/home/user/solvers/solverX /home/user/inputs/problemA.dat > /home/user/outputs/solverX_problemA.out & /home/user/solvers/solverY /home/user/inputs/problemA.dat > /home/user/outputs/solverY_problemA.out & /home/user/solvers/solverX /home/user/inputs/problemB.dat > /home/user/outputs/solverX_problemB.out & /home/user/solvers/solverY /home/user/inputs/problemB.dat > /home/user/outputs/solverY_problemB.out & wait
printf "BENCHMARK RESULTS\n\nInput File: problemA.dat\nsolverX output: solverX_problemA.out\nsolverY output: solverY_problemA.out\n\nInput File: problemB.dat\nsolverX output: solverX_problemB.out\nsolverY output: solverY_problemB.out\n" > /home/user/outputs/benchmark.log
ls -1 /home/user/outputs/
cat /home/user/outputs/benchmark.log
