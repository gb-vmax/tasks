You are a monitoring specialist preparing the release of a monitoring alert script located at <code>/home/user/alert_scripts/check_disk.sh</code>. The current version of this script is <b>1.2.3</b>, recorded at the top of the script file in a comment line with the format: <code># Version: current_version_here</code>.

Your task is to prepare a release for a <b>minor feature addition</b> (not a breaking change or patch) and update the version accordingly. Specifically:

1. Increment the minor version in <code>/home/user/alert_scripts/check_disk.sh</code> by 1, so that the version line reads: <code># Version: 1.3.0</code>.
2. Create or update a <code>CHANGELOG.md</code> file in <code>/home/user/alert_scripts/</code>. 
   - The changelog entry must be at the top of the file, in the following format (exactly, including leading '##') for the new version:
<pre>
## [1.3.0] - YYYY-MM-DD
### Added
- Initial alert email integration.
</pre>
Replace <b>YYYY-MM-DD</b> with today’s date (UTC, in ISO format).
3. Previous changelog entries (if any) must be preserved underneath the new entry; do not remove or overwrite them.

To verify, save a release log named <code>/home/user/alert_scripts/release.log</code> containing exactly these three lines:
<pre>
Bumped version to 1.3.0
Changelog updated for 1.3.0
Release prepared successfully
</pre>

Ensure all file permissions allow reading and writing by your user.
