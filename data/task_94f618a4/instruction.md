You are developing a set of Python utilities and want to manage the dependent packages in a clear, reproducible way. Please do the following:

1. In your home directory (/home/user), create a new directory named "/home/user/pyutils".
2. In this new directory, set up a Python virtual environment named "venv".
3. Using pip (inside the virtual environment), install the packages "requests==2.31.0" and "pytz==2024.1".
4. Once installed, create a file at "/home/user/pyutils/package_list.txt". This file must contain a list of all installed packages in the virtual environment, with each line following this precise format: "<package-name>==<version>". 
5. Only include the direct packages: "requests" and "pytz" (do not list pip, setuptools, or any other dependencies).
6. Sort the entries alphabetically by package name.

Your task is complete when the "package_list.txt" file is present at "/home/user/pyutils/package_list.txt" and matches the format as specified above.
