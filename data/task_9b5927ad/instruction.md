You are a mobile build engineer managing a pipeline for testing and benchmarking two different optimization solver binaries, `solverX` and `solverY`, stored in `/home/user/solvers/`. Each solver takes input from `.dat` files located in `/home/user/inputs/` and writes results to a corresponding output file in `/home/user/outputs/`, using the same base filename but replacing `.dat` with `.out`. For example, `/home/user/inputs/problemA.dat` produces `/home/user/outputs/problemA.out`. 

Your tasks are as follows:

1. Ensure that the directory `/home/user/outputs/` exists and is empty (delete any old files inside if present).
2. In parallel, run both `solverX` and `solverY` on each input file located in `/home/user/inputs/` (you can assume there are exactly two input files: `problemA.dat` and `problemB.dat`). For each solver, copy the results to output files named as `<solver_name>_<problem_name>.out` in `/home/user/outputs/`. For instance, results from `solverX` on `problemA.dat` should be written to `/home/user/outputs/solverX_problemA.out`.
3. After completion, generate a benchmark log file at `/home/user/outputs/benchmark.log` with the following format:

```
BENCHMARK RESULTS

Input File: problemA.dat
solverX output: solverX_problemA.out
solverY output: solverY_problemA.out

Input File: problemB.dat
solverX output: solverX_problemB.out
solverY output: solverY_problemB.out
```

All filenames and their references in `benchmark.log` must exactly follow the format and order shown above. The automated test will validate the precise format of the log, the existence of all specified output files, and their correct naming scheme. No output files should exist in `/home/user/outputs/` except those named as described.
