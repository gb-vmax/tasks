As the database reliability engineer, you maintain a backup utility project located in <code>/home/user/db-backup-utility</code>. The utility uses semantic versioning (semver) for releases and tracks changes in a file named <code>CHANGELOG.md</code> (located in the project root). 

You have been tasked to:
1. Bump the minor version of the project from <b>2.3.4</b> to <b>2.4.0</b>. The current version is specified as <code>version</code> in the <code>/home/user/db-backup-utility/config.yaml</code> file.
2. Add a new entry to <code>CHANGELOG.md</code> at the very top, following the precise format:
    <br>
    <pre>
## [2.4.0] - 2024-06-24
### Added
- Implemented automatic backup retention checks with alerting (Reliability Improvement).
    </pre>
    <br>
    The date in the header (<code>2024-06-24</code>) <b>must be today's date</b> (system date when the task is performed, format YYYY-MM-DD).
3. Ensure that all prior changelog entries remain unchanged and <b>the newly added block is at the very top</b> of the <code>CHANGELOG.md</code>.
4. At the end, <b>output to the console</b>:
    <ul>
        <li>The new version line from <code>config.yaml</code></li>
        <li>The complete new <code>CHANGELOG.md</code> contents</li>
    </ul>
    Print both outputs exactly as they appear in the files, with no extra commentary.

<b>Verification will:</b> check that <code>config.yaml</code> specifies <code>version: "2.4.0"</code> and that <code>CHANGELOG.md</code> has the required entry at its very top with the correct date and format, preserving existing content below.
