As a database administrator, you have recently optimized some SQL queries in your project located at <code>/home/user/sql-optimizer</code>. The project uses semantic versioning and maintains a changelog. 

1. Bump the minor version (increase the "Y" in "X.Y.Z") in the project’s version file, <code>/home/user/sql-optimizer/VERSION</code>. Do not change the major or patch version numbers.
2. Add a new entry at the top of the changelog file, <code>/home/user/sql-optimizer/CHANGELOG.md</code>, describing "Optimized SELECT queries for faster execution." Include the new version and today’s date in the header in the format: <code>## [NEW_VERSION] - YYYY-MM-DD</code>. The entry should be at the top, immediately following the introductory section (if present).
3. The changelog entry should be prefixed with a dash and a space (e.g., <code>- Optimized SELECT queries for faster execution.</code>). The rest of the changelog must remain unchanged except for this new entry.

Example output in <code>/home/user/sql-optimizer/CHANGELOG.md</code> (with version 1.4.0 bumped to 1.5.0 and today’s date 2024-06-05):

<pre>
## [1.5.0] - 2024-06-05
- Optimized SELECT queries for faster execution.

## [1.4.0] - 2024-05-30
- Initial release.
</pre>

Ensure after completion that:
- <code>/home/user/sql-optimizer/VERSION</code> has the correct new version with no extra spaces or content.
- <code>/home/user/sql-optimizer/CHANGELOG.md</code> follows the above format, with your entry placed correctly.
