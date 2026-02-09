# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with ES module interoperability. When importing modules, the `__esModule` property is being set incorrectly, which is causing problems with CommonJS/ESM compatibility.

### Reproduction

```js
// When importing the remark-rehype module
const remarkRehype = require('remark-rehype');

// The __esModule property is set to false instead of true
console.log(remarkRehype.__esModule); // Expected: true, Actual: false
```

This is breaking module resolution and causing import statements to fail in environments that rely on the `__esModule` flag to determine module type.

### Expected behavior

The `__esModule` property should be set to `true` for proper ES module compatibility. This is the standard convention for transpiled ES modules to indicate they were originally ES modules.

### System Info
- Node version: 16.x
- Module system: CommonJS with ES module imports

---
Repository: /testbed
