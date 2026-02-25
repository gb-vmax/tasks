I need you to help me curate a list of enabled binary repositories for our artifact manager. You will find an INI configuration file at <code>/home/user/artifact_manager/repos.ini</code> which lists all available repositories, their base URLs, and their enabled/disabled status. Your task is as follows:

1. Parse the <code>/home/user/artifact_manager/repos.ini</code> INI file. Each repository is represented as a separate INI section (e.g., <code>[repo1]</code>), and inside each section, there are two keys: <code>base_url</code> and <code>enabled</code>. The value of <code>enabled</code> can be either <code>yes</code> or <code>no</code>.
2. Identify all repositories that have <code>enabled = yes</code>.
3. Create a new file at <code>/home/user/artifact_manager/enabled_repos.log</code>. In this file, write one line per enabled repository. Each line should be formatted as <code>&lt;repository_section_name&gt;: &lt;base_url&gt;</code>. For example, if the section is <code>[repo1]</code> and base_url is <code>https://binaries.example.com/repo1</code>, the line would be: <code>repo1: https://binaries.example.com/repo1</code>.
4. The output file should maintain the same order in which repositories are listed in the <code>repos.ini</code> file. Do not alter the order.
5. Only repositories with <code>enabled = yes</code> should appear in the output file.
6. Overwrite the <code>/home/user/artifact_manager/enabled_repos.log</code> file if it already exists.
7. You can output the enabled repository list to the terminal as well to verify.

Check the <code>enabled_repos.log</code> file to make sure it contains only the names and base URLs of enabled repositories, formatted exactly as specified.
