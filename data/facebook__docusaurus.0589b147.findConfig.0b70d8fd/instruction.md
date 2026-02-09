# Bug Report

### Describe the bug

When running Docusaurus, the config file detection logic appears to be inverted. The application throws a "No config file found" error even when a valid config file exists in the site directory.

### Reproduction

1. Create a new Docusaurus site with a standard `docusaurus.config.js` file
2. Try to start the development server or build the site
3. The application fails with "No config file found" error despite the config file being present

```
Error: No config file found.
Expected one of: docusaurus.config.ts, docusaurus.config.mts, ...
```

This happens even though the config file clearly exists in the project root.

### Expected behavior

The application should detect and load the config file normally when it exists in the site directory. The error message should only appear when no config file is actually present.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
