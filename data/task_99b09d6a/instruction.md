You are a configuration manager and need to track recent changes to your project. First, generate a markdown-formatted changelog file at <code>/home/user/project/CHANGELOG.md</code> that documents the following changes:

<ul>
  <li>Added a new module for API integrations</li>
  <li>Fixed an issue with database connections</li>
  <li>Updated documentation for the install process</li>
</ul>

The changelog must use this exact structure and formatting:

<pre>
# Changelog

## [1.0.1] - 2024-05-21
### Added
- New module for API integrations

### Fixed
- Issue with database connections

### Changed
- Documentation for the install process
</pre>

(Do not use any placeholders, and ensure the date, version, and messages are exactly as above.)

After writing the file, use a markdown linter tool (such as <code>markdownlint-cli</code>) to check <code>/home/user/project/CHANGELOG.md</code> for style or formatting issues. Generate a linting report and save it as <code>/home/user/project/CHANGELOG_lint.log</code>.

The linting report should include any style warnings or confirm there are no issues. Indicate "No issues found" if the file passes linting.

This process will help ensure your documentation is consistent and professional.
