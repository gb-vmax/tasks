You are assisting as a deployment engineer responsible for updating the configuration of an open-source optimization solver used by your development team. There is a configuration directory at <b>/home/user/opt_solver/configs/</b> containing a file named <b>solver.conf</b>. Your task is to:

1. Make a backup of the current <b>solver.conf</b> file to <b>/home/user/opt_solver/configs/solver.conf.bak</b>.
2. Update the <b>solver.conf</b> file so that the line specifying the solver's maximum iterations is set to <b>max_iterations = 2000</b>. Only this line should be modified; any other parameters or comments should remain intact.
3. Record a deployment log entry in <b>/home/user/opt_solver/deploy.log</b> with the following format (on a new line):

    <pre>
[YYYY-MM-DD HH:MM:SS] solver.conf updated: max_iterations set to 2000 and backup created as solver.conf.bak
    </pre>

Make sure the timestamp matches the current system time when the update is applied. The log entry should be appended, not replacing any existing content in the log file. 

Upon completion, there should be:

- An exact backup of the original solver.conf as solver.conf.bak
- The solver.conf should have max_iterations = 2000 (no duplication of the line)
- An appended log entry in the specified format with the proper timestamp

Please do not alter or remove any other lines in solver.conf. Existing directory and file permissions allow read/write for the current user.
