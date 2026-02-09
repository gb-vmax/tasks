# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with ES module exports in the vendored `remark-rehype` package. The `__esModule` property is being set incorrectly, which is causing module resolution problems in my Jest tests.

### Reproduction

When importing from the vendored remark-rehype module:

```js
const remarkRehype = require('./jest/vendor/remark-rehype@11.0.0.js');

// The module is not recognized as an ES module
console.log(remarkRehype.__esModule); // Expected: true, Actual: false
```

This is breaking interoperability between CommonJS and ES modules. The module should be properly marked as an ES module with `__esModule: true`, but it appears to be set to `false` instead.

### Expected behavior

The `__toCommonJS` helper should properly set the `__esModule` property to `true` to indicate that the module was originally an ES module. This is the standard convention for transpiled ES modules in CommonJS environments.

### System Info
- Jest version: latest
- Node version: 18.x

---
Repository: /testbed
