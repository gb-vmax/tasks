# Bug Report

### Describe the bug

The config file is no longer being found in the site directory. After a recent update, Docusaurus is now searching for the config file in the parent directory instead of the actual site directory, and the error message is being displayed even when a valid config file exists.

### Reproduction

```
my-project/
  ├── docusaurus.config.js  (this file exists)
  └── docs/
```

When running Docusaurus from the `my-project` directory, I get:

```
No config file found.
Expected one of: docusaurus.config.ts, docusaurus.config.mts, docusaurus.config.cts, docusaurus.config.js, docusaurus.config.mjs, docusaurus.config.cjs
You can provide a custom config path with the --config option.
```

Even though `docusaurus.config.js` is present in the site directory.

### Expected behavior

Docusaurus should find the config file when it's located in the site directory and proceed with the build/start process without showing an error.

### Additional context

This seems to have broken after a recent change. The config file discovery logic appears to be looking in the wrong location now.

---
Repository: /testbed
