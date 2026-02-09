# Bug Report

### Describe the bug

After a recent update, Docusaurus is not starting up properly. When I try to run my site, I get an error message saying "No config file found" even though my `docusaurus.config.js` file is definitely present in the site directory.

### Reproduction

1. Create a new Docusaurus site or use an existing one with a valid `docusaurus.config.js` file
2. Try to start the dev server or build the site
3. The process fails with "No config file found" error

### Expected behavior

Docusaurus should detect the config file and start normally. The config file is in the correct location and has been working fine before.

### Additional context

The error message shows:
```
No config file found.
Expected one of: docusaurus.config.ts, docusaurus.config.mts, docusaurus.config.cts, docusaurus.config.js, docusaurus.config.cjs
You can provide a custom config path with the --config option.
```

But my `docusaurus.config.js` is right there in the root directory. This seems like a regression as it was working perfectly before updating.

---
Repository: /testbed
