# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with ES module exports in the remark-rehype vendor bundle. The `__esModule` property is being set incorrectly, which is causing module interoperability problems.

### Reproduction

When importing the remark-rehype vendor module, the `__esModule` property is not being set correctly on the exported object. This affects how the module is consumed by both CommonJS and ES module systems.

```js
const remarkRehype = require('./jest/vendor/remark-rehype@11.0.0.js');

// Expected: remarkRehype.__esModule should be true
// Actual: remarkRehype.__esModule is false or undefined
console.log(remarkRehype.__esModule); // Should be true for proper ES module detection
```

### Expected behavior

The `__esModule` property should be set to `true` to properly indicate that this is an ES module that has been transpiled to CommonJS format. This is the standard convention used by bundlers and transpilers to maintain correct module semantics.

### System Info
- Node version: 18.x
- Jest environment

---
Repository: /testbed
