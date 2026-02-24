I need your help organizing a project directory using symbolic links. In my home directory (/home/user), there's a directory called "project_alpha" containing a file "main.py" and a subdirectory "scripts" that has a file named "helper.sh". I want to do the following:

1. In my home directory (/home/user), create a directory called "workspace_links".
2. Inside "workspace_links", create a symbolic link named "alpha_main.py" that points to "/home/user/project_alpha/main.py".
3. Also inside "workspace_links", create a symbolic link named "alpha_helper.sh" that points to "/home/user/project_alpha/scripts/helper.sh".
4. After creating these links, produce a log file named "symlink_creation.log" inside "/home/user/workspace_links". The log should be a plain text file where each line lists the symbolic link name, an arrow (->), and the absolute path it points to (for example: "alpha_main.py -> /home/user/project_alpha/main.py"). Each link and its target should be on a separate line, and no extra lines should be present.

Please ensure the symbolic links use absolute paths for their targets, as described.
