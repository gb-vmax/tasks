# Bug Report

### Describe the bug

After a recent update, Docusaurus is failing to load configuration files. The build process throws an error saying "No config file found" even when a valid `docusaurus.config.js` (or other supported config file) exists in the project directory.

### Reproduction

1. Create a new Docusaurus project or use an existing one with a valid config file (e.g., `docusaurus.config.js`)
2. Run the build or start command
3. The process fails with "No config file found" error

I have a `docusaurus.config.js` file in my project root, but it's not being detected. The error message lists all the possible config file names, but it seems like none of them are being found even though the file clearly exists.

### Expected behavior

Docusaurus should detect and load the configuration file (e.g., `docusaurus.config.js`, `docusaurus.config.ts`, etc.) when it exists in the site directory and proceed with the build/start process normally.

### Additional context

This was working fine before. The config file hasn't been moved or renamed. Other developers on my team are experiencing the same issue after pulling the latest changes.

---
Repository: /testbed
