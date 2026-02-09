# Bug Report

### Describe the bug

When trying to load an ES module config file in a CommonJS context, the CLI is not properly detecting the module loading error and falling back to the appropriate loader. The config file fails to load even though it should be detected as an ES module and handled accordingly.

### Reproduction

1. Create a `rollup.config.js` file that uses ES module syntax (e.g., `export default { ... }`)
2. Run rollup from a CommonJS context (package.json without `"type": "module"`)
3. The config file fails to load instead of being properly detected as an ES module

The error message appears but the fallback mechanism doesn't trigger correctly.

### Expected behavior

The CLI should detect when an ES module config file is being loaded in a CommonJS context (by checking for the warning message) and automatically use the appropriate loader to handle it.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: Linux

---
Repository: /testbed
