You are a build engineer managing artifacts in the directory /home/user/artifacts. In a recent build job, the output files are stored in /home/user/builds/output and must be moved to /home/user/artifacts for archival. However, to ensure a robust pipeline, you also need to identify and log any files that could not be moved (for example, due to file conflicts where a file with the same name already exists in the destination directory).

Your task is as follows:

1. Attempt to move all files from /home/user/builds/output to /home/user/artifacts.
2. If a file cannot be moved because a file with the same name already exists in /home/user/artifacts, skip moving that file and do not overwrite the existing file.
3. For each file you are unable to move due to this conflict, record its file name in a log file for further review. The log file should be located at /home/user/artifacts/move_errors.log.
4. The move_errors.log file must be a plain text file, with one file name per line, for each file in /home/user/builds/output that could not be moved due to a naming conflict in /home/user/artifacts.
5. Do not log files that move successfully.

At the end of this task, all non-conflicting files from /home/user/builds/output should be present in /home/user/artifacts, no files should be overwritten, and the log should accurately list the names (not full paths) of any files that could not be moved due to pre-existing files in the artifacts directory.
