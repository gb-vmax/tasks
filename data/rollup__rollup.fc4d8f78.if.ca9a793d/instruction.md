# Bug Report

### Describe the bug

I'm experiencing an issue where Rollup fails to properly detect ES module loading errors when trying to load a config file. The error detection logic seems to have changed and now requires both error message patterns to be present simultaneously, which never happens in practice.

### Reproduction

1. Create a CommonJS package (without `"type": "module"` in package.json)
2. Try to use an ES module config file (e.g., `rollup.config.mjs` with `import` statements)
3. Rollup should detect the ES module loading error and provide a helpful message

**Expected behavior:**
Rollup should detect when it cannot load an ES module config file and set the `cannotLoadEsm` flag appropriately.

**Actual behavior:**
The ES module loading error is not detected, causing Rollup to fail without providing proper guidance to the user about the module loading issue.

### Additional context

This appears to affect the error handling when Node.js throws warnings about ES module loading failures. The detection logic should catch warnings that contain either of the relevant error messages, but currently it only triggers when both messages appear in the same warning (which doesn't happen).

---
Repository: /testbed
