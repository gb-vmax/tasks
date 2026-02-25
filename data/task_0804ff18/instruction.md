You are a researcher organizing your machine for future data analysis work. Please perform the following actions step by step:

1. Verify whether the Python package "pandas" is already installed in your environment.
2. If it is not already installed, install the "pandas" package using the pip package manager for Python 3.
3. Create a log file at <code>/home/user/dataset_setup/package_log.txt</code>. In this file, record the results of your actions in the following strict format so it can be automatically checked:
    - The very first line of the file should be either <code>pandas already installed</code> or <code>pandas installed</code> (depending on whether you needed to install it).
    - The second line should be the version of pandas installed, in the exact format: <code>pandas version: x.y.z</code> (where <code>x.y.z</code> is the version number reported by pandas).
4. Ensure the <code>dataset_setup</code> directory exists before writing the log file. If not, create it.

For example, your <code>/home/user/dataset_setup/package_log.txt</code> might look like this if pandas was already present and its version was 1.4.2:
<pre>
pandas already installed
pandas version: 1.4.2
</pre>

Or, if you had to install it and the version is 2.0.1:
<pre>
pandas installed
pandas version: 2.0.1
</pre>
Please ensure there are no extra blank lines or any other output in the log file except as specified above.
