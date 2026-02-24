You are acting as a capacity planner who maintains a resource monitoring tool stored in a git repository located at <code>/home/user/projects/resmon</code>. The project uses semantic versioning and maintains a changelog to track notable changes between releases.

Complete the following steps:
1. Navigate to the repository at <code>/home/user/projects/resmon</code>.
2. Retrieve and analyze the previous resource usage report located at <code>/home/user/projects/resmon/reports/usage_2024-06-01.csv</code>. It is in CSV format with columns: <code>resource,cpu_usage,mem_usage</code>.
3. Simulate the addition of a new feature to the monitoring tool by appending a line to <code>CHANGELOG.md</code> under a new unreleased section called <code>## [Unreleased]</code>. The entry should clearly state: <code>- Added disk I/O statistics collection to the monitoring tool.</code>
4. Bump the semantic version in <code>resmon/version.txt</code>. The current version is <code>1.4.2</code> (found as the only line in the file). Update the version appropriately to reflect a minor feature addition. The new version should be placed as the only line in the file.
5. Update <code>CHANGELOG.md</code>:
    - Move the new changelog entry from the Unreleased section to a new versioned section at the top of the file, with a heading in the following format: <code>## [NEW_VERSION] - YYYY-MM-DD</code>, where <code>NEW_VERSION</code> is the bumped semantic version and <code>YYYY-MM-DD</code> is today’s date in ISO format.
    - Ensure any existing earlier entries for 1.4.2 remain unchanged and below the new version section.
    - The file should have a section order: most recent version at top, then previous versions.
6. Create and save a release log at <code>/home/user/projects/resmon/reports/release_2024-06-02.log</code> containing:
    - The new version number.
    - The full changelog entry for this version (verbatim from the section in CHANGELOG.md).
    - A summary sentence stating: <code>Disk I/O statistics monitoring is now available as part of the resource usage tool.</code>

The output format in <code>CHANGELOG.md</code> must use markdown heading style (##), and the changelog must be clear and concise as indicated above. The <code>release_2024-06-02.log</code> file must be plain text, containing only the required items in the order specified, each on its own line, without extra comments or formatting.
