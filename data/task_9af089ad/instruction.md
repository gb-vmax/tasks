You are a technical writer responsible for organizing the documentation of three optimization solvers: "OptiFast", "LinearSolve", and "CurveFit". In the directory /home/user/solver_docs, you will create a well-organized set of documentation files and a summary CSV.

Here are your tasks:

1. Create a directory /home/user/solver_docs if it does not already exist.

2. For each solver, create a Markdown documentation file in /home/user/solver_docs named optifast.md, linearsolve.md, and curvefit.md, respectively. Each file must contain two sections with the following specific headings (Markdown format):

   - # Introduction
   - # Usage Example

3. The contents to place under each heading should be as follows:
   - For "OptiFast":
     - Introduction: "OptiFast is a high-speed optimization solver designed for real-time applications."
     - Usage Example: "optifast --input data.csv --max-iterations 1000"
   - For "LinearSolve":
     - Introduction: "LinearSolve efficiently solves large linear systems of equations."
     - Usage Example: "linearsolve --matrix matrix.txt --verbose"
   - For "CurveFit":
     - Introduction: "CurveFit provides advanced curve fitting features with robust statistical models."
     - Usage Example: "curvefit --data points.json --method least_squares"

4. Create a CSV summary file at /home/user/solver_docs/solvers_summary.csv with the following columns, exactly spelled and ordered: Solver, Description, ExampleCommand

5. Fill the rows of solvers_summary.csv so each row contains the exact corresponding solver name, its single-sentence description (from the Introductions above), and the specific usage example (from above). The file must be comma-separated (no quotations around text), contain a header row, and preserve the exact order: OptiFast, LinearSolve, CurveFit.

Your output files must contain exactly the text and formats described above. To verify, ensure there is a total of four files created in /home/user/solver_docs: optifast.md, linearsolve.md, curvefit.md, and solvers_summary.csv, with the precise content format as specified.
