You are a QA engineer setting up a clean Python test environment for a new project. Please perform the following steps:

1. In your home directory (/home/user), create a new directory named "qa_project_env".
2. Inside "qa_project_env", set up a Python virtual environment using the standard venv module. The virtual environment directory must be named "venv".
3. After creating the virtual environment, activate it.
4. While the virtual environment is active, run the command `python --version` and redirect the output to a file named "python_version.txt" inside the "qa_project_env" directory.

Make sure that the "python_version.txt" file contains only a single line with the Python version of the virtual environment (e.g., "Python 3.10.12") and no additional text, whitespace, or error messages. The test will check that the "python_version.txt" file in /home/user/qa_project_env exactly matches the output format specified.
