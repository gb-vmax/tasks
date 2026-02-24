You are an operations engineer doing incident triage on a Linux system. A Python-based tool, used for monitoring disk health, is not working as expected. Your tasks are as follows:

1. In your home directory, create a new isolated Python virtual environment named <b>diskmon-env</b> in <b>/home/user/diskmon-env</b>.
2. Activate the virtual environment.
3. Using <b>pip</b>, install the following exact package versions: <b>psutil==5.9.8</b> and <b>click==8.1.7</b>.
4. After installation, use the <b>pip freeze</b> command to output the list of installed packages (and their versions) to a new file named <b>/home/user/diskmon-env/pip-freeze.log</b>.

<b>Output Format Specification:</b>
<ul>
    <li>The <b>pip-freeze.log</b> file must contain a plain text, line-separated list of the installed packages with their versions, formatted precisely as output by <code>pip freeze</code>. Each line should be in the form <code>package==version</code>.</li>
    <li>The file should list at least <code>psutil==5.9.8</code> and <code>click==8.1.7</code>. If there are any additional packages required by the environment management tools (e.g., <code>pip</code>, <code>setuptools</code>, <code>wheel</code>, etc.), those should also appear in the output exactly as reported by <code>pip freeze</code>.</li>
</ul>

Make sure the <code>pip-freeze.log</code> file is placed at <code>/home/user/diskmon-env/pip-freeze.log</code> and follows the format strictly for automated checking.
