FROM ubuntu:22.04

RUN <<'ENDPOST'
set -e

    apt-get update
    apt-get install -y python3-pip
    pip3 install --no-cache-dir pytest

    # Create the documentation directory
    DOCS_DIR="/home/user/solver_docs"
    mkdir -p "$DOCS_DIR"

    # Create optifast.md
    cat > "$DOCS_DIR/optifast.md" <<'EOF'
# Introduction
OptiFast is a high-speed optimization solver designed for real-time applications.

# Usage Example
optifast --input data.csv --max-iterations 1000
EOF

    # Create linearsolve.md
    cat > "$DOCS_DIR/linearsolve.md" <<'EOF'
# Introduction
LinearSolve efficiently solves large linear systems of equations.

# Usage Example
linearsolve --matrix matrix.txt --verbose
EOF

    # Create curvefit.md
    cat > "$DOCS_DIR/curvefit.md" <<'EOF'
# Introduction
CurveFit provides advanced curve fitting features with robust statistical models.

# Usage Example
curvefit --data points.json --method least_squares
EOF

    # Create solvers_summary.csv
    cat > "$DOCS_DIR/solvers_summary.csv" <<'EOF'
Solver,Description,ExampleCommand
OptiFast,OptiFast is a high-speed optimization solver designed for real-time applications.,optifast --input data.csv --max-iterations 1000
LinearSolve,LinearSolve efficiently solves large linear systems of equations.,linearsolve --matrix matrix.txt --verbose
CurveFit,CurveFit provides advanced curve fitting features with robust statistical models.,curvefit --data points.json --method least_squares
EOF

    # Ensure user read/write permissions for all files and directory
    chmod 700 "$DOCS_DIR"
    chmod 600 "$DOCS_DIR"/*.md "$DOCS_DIR"/*.csv
ENDPOST

WORKDIR /home/user
