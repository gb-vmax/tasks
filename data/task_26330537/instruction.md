You are acting as an artifact manager curating binary repositories. Your goal is to ensure that the correct number of artifact-related client processes are running, log their states, and manage their execution as follows:

1. Prepare a workspace at /home/user/repos/binmgr. If the directory does not exist, create it.
2. In this workspace, create a file named /home/user/repos/binmgr/artifact_client.sh with the following specifications:
   - The script must be a Bash shell script.
   - When executed, it must print the phrase "artifact-client running on PID [PID]" (where [PID] is the real process ID of the shell script) to standard output.
   - The script must then sleep for 120 seconds.
3. Ensure that this script is executable.
4. Start exactly three (3) background instances of artifact_client.sh from /home/user/repos/binmgr, so they run simultaneously in the background. You should ensure that all three processes are running at the same time.
5. Create a process management log at /home/user/repos/binmgr/process_log.txt with the following format:
   - For each running artifact_client.sh process, log a single line containing the PID, the command used, and the start time in the following precise format:
     ```
     PID: [PID] | CMD: /home/user/repos/binmgr/artifact_client.sh | START: [YYYY-MM-DD HH:MM:SS]
     ```
     where [PID] is the numeric Unix process ID for each process, and [YYYY-MM-DD HH:MM:SS] is the local time when the process started (in 24-hour format).
   - Only list artifact_client.sh processes; do not include other system processes.
   - List all three processes in the log, each on a single line as described.
6. After verifying all three processes are running, clean up by terminating only the artifact_client.sh background processes you started, without affecting any unrelated processes, and update the process_log.txt file:
   - For each previously-logged process, add a line immediately after its original entry in the following format:
     ```
     PID: [PID] | STATUS: TERMINATED | END: [YYYY-MM-DD HH:MM:SS]
     ```
     where [PID] matches the previous entry and [YYYY-MM-DD HH:MM:SS] is the local end time when the process was terminated.
   - Ensure that every termination entry corresponds to a previously-logged process and appears immediately after its corresponding START entry.

Your final deliverables for verification will be:
- The artifact_client.sh script with correct behavior and permissions.
- The process_log.txt file formatted exactly as described, with accurate information for the three managed processes.
