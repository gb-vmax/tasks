As a build engineer, you need to quickly verify which artifact is set as "release" in a configuration file for a project. In the directory <code>/home/user/projects/build_config/</code>, there is an INI file named <code>artifacts.ini</code>. This file contains multiple artifact definitions under different sections, with keys such as <code>name</code>, <code>type</code>, and <code>status</code> in each section.

Your task is to parse this INI file and determine the <code>name</code> value from the section where <code>status=release</code>.

Print only the artifact name(s) — one per line if there are multiple — with no extra spaces or formatting. Do not print section names, keys, or values not matching the requirement. The output should be plain text, suitable for automated checking.

Example output format:
<pre>
artifact1
artifact2
</pre>

Ensure your output includes <b>only</b> the value(s) of the <code>name</code> key for all artifact sections where <code>status=release</code>.
