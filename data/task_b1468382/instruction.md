You are a site reliability engineer monitoring a service's uptime. There is a project directory at <code>/home/user/uptime_monitor</code> containing a <code>VERSION</code> file and a <code>CHANGELOG.md</code> file. 

The current <code>VERSION</code> file contains the string <code>1.4.1</code> (with no whitespace). You discovered and fixed a minor bug related to tracking downtime duration, and now you need to perform a semantic version bump: increase the patch version by 1 (e.g., from <code>X.Y.Z</code> to <code>X.Y.(Z+1)</code>). 

Update the <code>/home/user/uptime_monitor/VERSION</code> file to reflect the new version. Also, prepend the following entry at the very top of <code>/home/user/uptime_monitor/CHANGELOG.md</code> (above any previous entries, which should remain below):

<pre>
## [1.4.2] - 2023-08-10
### Fixed
- Corrected bug in downtime duration calculation.
</pre>

Ensure that the date in the changelog entry is exactly <code>2023-08-10</code>. The output format must preserve the Markdown headers and bullet style as shown above. No extra whitespace before or after the section; keep all previous changelog content as-is, below the new entry. 

Verify your changes by printing the first 6 lines of <code>CHANGELOG.md</code> and the complete contents of the <code>VERSION</code> file to the console.
