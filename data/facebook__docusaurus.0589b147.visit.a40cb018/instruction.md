# Bug Report

### Describe the bug

I'm encountering a syntax error when trying to use the `unist-util-visit` module. The module fails to load with a parsing error, making it completely unusable.

### Reproduction

```js
const { visit } = require('./jest/vendor/unist-util-visit@5.0.0.js');

// Attempting to use visit causes the module to fail loading
```

When trying to import or require the module, I get a syntax error during parsing. The module doesn't even load properly, so I can't use any of the exported functions.

### Expected behavior

The module should load without errors and the `visit` function should be available for use. The exports should be properly defined and accessible.

### Additional context

This appears to be affecting the vendored version of unist-util-visit in the jest directory. The issue prevents any code that depends on this module from running.

---
Repository: /testbed
