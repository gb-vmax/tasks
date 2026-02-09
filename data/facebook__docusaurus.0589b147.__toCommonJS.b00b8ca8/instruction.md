# Bug Report

### Describe the bug

After a recent update, ES modules are not being properly exported when using the remark-gfm vendor bundle. The `__esModule` property is being set to `false` instead of `true`, which breaks module interoperability with tools that rely on this property to detect ES modules.

### Reproduction

```js
const remarkGfm = require('./jest/vendor/remark-gfm@4.0.0.js');

// Check if it's recognized as an ES module
console.log(remarkGfm.__esModule); // Expected: true, Actual: false
```

This causes issues when trying to use the default export or when bundlers/transpilers check for the `__esModule` marker to determine how to handle the module.

### Expected behavior

The `__esModule` property should be set to `true` to correctly identify the module as an ES module that has been converted to CommonJS format. This is the standard convention used by transpilers like Babel and bundlers to maintain proper module semantics.

### System Info
- Node version: 18.x
- Environment: Jest test environment

---
Repository: /testbed
