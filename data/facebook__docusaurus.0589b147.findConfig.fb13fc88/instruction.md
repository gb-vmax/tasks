# Bug Report

### Describe the bug

I'm unable to start my Docusaurus site after updating to the latest version. The build process fails immediately with an error message saying "No config file found" even though I have a valid `docusaurus.config.js` file in my site directory.

### Reproduction

1. Create a new Docusaurus site or use an existing one
2. Ensure you have a `docusaurus.config.js` file in the root directory
3. Try to run the site (build or start command)
4. The process fails with "No config file found" error

### Expected behavior

The site should start normally and recognize the config file. Previously this was working fine, but after the recent update it can't find the configuration file anymore.

### Additional context

The error message suggests using `--config` option to provide a custom config path, but this shouldn't be necessary for the default config file location. This seems like a regression as it was working before.

---
Repository: /testbed
