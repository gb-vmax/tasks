#!/bin/bash
set -e
cd /home/user

mkdir -p /home/user/solver_docs
cat > /home/user/solver_docs/optifast.md <<EOF
# Introduction
OptiFast is a high-speed optimization solver designed for real-time applications.

# Usage Example
optifast --input data.csv --max-iterations 1000
EOF
cat > /home/user/solver_docs/linearsolve.md <<EOF
# Introduction
LinearSolve efficiently solves large linear systems of equations.

# Usage Example
linearsolve --matrix matrix.txt --verbose
EOF
cat > /home/user/solver_docs/curvefit.md <<EOF
# Introduction
CurveFit provides advanced curve fitting features with robust statistical models.

# Usage Example
curvefit --data points.json --method least_squares
EOF
cat > /home/user/solver_docs/solvers_summary.csv <<EOF
Solver,Description,ExampleCommand
OptiFast,OptiFast is a high-speed optimization solver designed for real-time applications.,optifast --input data.csv --max-iterations 1000
LinearSolve,LinearSolve efficiently solves large linear systems of equations.,linearsolve --matrix matrix.txt --verbose
CurveFit,CurveFit provides advanced curve fitting features with robust statistical models.,curvefit --data points.json --method least_squares
EOF
ls -1 /home/user/solver_docs
cat /home/user/solver_docs/optifast.md
cat /home/user/solver_docs/solvers_summary.csv
