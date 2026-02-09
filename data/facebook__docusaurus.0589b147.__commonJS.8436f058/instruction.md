# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with module exports not being properly returned. When requiring CommonJS modules, the exports object is not being accessed correctly, leading to undefined values or missing exports.

### Reproduction

```js
// When using the bundled MDX vendor code
const mdx = require('@mdx-js/mdx');

// Expected: mdx should contain the exported functions/objects
// Actual: mdx is undefined or an object without the exports property
console.log(mdx); // Shows incorrect structure
```

The issue appears to be in how the `__commonJS` helper function handles the module exports. Instead of returning `mod.exports`, it's returning just `mod`, which breaks the expected CommonJS behavior.

### Expected behavior

The CommonJS wrapper should properly return `mod.exports` so that all exported functions and objects are accessible when requiring the module.

### System Info
- Package: @mdx-js/mdx@3.0.0
- Environment: Jest vendor bundle

---
Repository: /testbed
