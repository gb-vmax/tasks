You are a data engineer starting a new ETL pipeline project in your home directory at <code>/home/user</code>. Set up a Python virtual environment for the project using Python's built-in <code>venv</code> module with the following requirements:

1. Create a new directory named <code>/home/user/etl_project</code>, and ensure all steps are performed within this directory.
2. Inside <code>/home/user/etl_project</code>, create a Python 3 virtual environment named <code>venv</code> using <code>python3 -m venv venv</code>.
3. Activate the virtual environment, and install the exact versions of the following packages using <code>pip</code>:
    - pandas==1.4.2
    - requests==2.27.1
    - pyarrow==8.0.0
4. Once installation finishes, use <code>pip freeze</code> inside the virtual environment to get a list of all installed packages and their versions.
5. Save the output from <code>pip freeze</code> to a file in <code>/home/user/etl_project</code> named <code>requirements-locked.txt</code>.
6. To verify that your virtual environment is properly configured, write a minimal Python script named <code>etl_test.py</code> in the <code>/home/user/etl_project</code> directory. The script must:
    - Import the three installed packages: <code>pandas</code>, <code>requests</code>, <code>pyarrow</code>.
    - When run, print the version of each package in the following format:
<pre>
pandas: x.y.z
requests: x.y.z
pyarrow: x.y.z
</pre>
      (where <code>x.y.z</code> is the imported module's <code>__version__</code>)
7. Run the script using the Python interpreter from inside your virtual environment, and save the console output (stdout) into a file called <code>etl_test_output.log</code> in the same directory.

Your files should be:
- <code>/home/user/etl_project/requirements-locked.txt</code> (output of pip freeze)
- <code>/home/user/etl_project/etl_test.py</code> (Python script as described)
- <code>/home/user/etl_project/etl_test_output.log</code> (console output as precisely specified above)

The test will check that these files exist and are correctly formatted and that the specified versions of the packages are installed in the virtual environment.
