You are assisting a technical writer tasked with ensuring that legacy Python scripts for two separate tools are functioning properly before updating the user documentation. Two directories exist in your home directory: /home/user/legacy_tool_a and /home/user/legacy_tool_b. Each contains a distinct Python script (tool_a.py in legacy_tool_a and tool_b.py in legacy_tool_b).

Your tasks are:
1. Simultaneously execute both /home/user/legacy_tool_a/tool_a.py and /home/user/legacy_tool_b/tool_b.py. These scripts produce output to standard output.
2. Collect and save the output from each script run into separate log files named /home/user/legacy_tool_a/run_output.log and /home/user/legacy_tool_b/run_output.log, respectively.
3. Create a master summary log at /home/user/legacy_scripts_outputs/summary.log. This log must have the following format (the automated test will check for exact formatting):

   ```
   === tool_a.py Output ===
   <entire contents of /home/user/legacy_tool_a/run_output.log>
   === tool_b.py Output ===
   <entire contents of /home/user/legacy_tool_b/run_output.log>
   ```

4. Confirm the existence and relative paths of all three log files by appending the following three lines to the MASTER summary log (after the output sections above):

   ```
   [LOG FILES CONFIRMED]
   legacy_tool_a/run_output.log
   legacy_tool_b/run_output.log
   summary.log
   ```

Notes:
- Run both scripts so that the outputs are generated in parallel, not sequentially.
- Ensure the log and summary files are readable by the current user and contain only the relevant outputs (no error messages or command prompts).
- All file and directory creations must occur within /home/user and its subdirectories.
- The agent is responsible for creating the /home/user/legacy_scripts_outputs directory if it does not exist.
- The final /home/user/legacy_scripts_outputs/summary.log file must match the specified format exactly for automated verification.
