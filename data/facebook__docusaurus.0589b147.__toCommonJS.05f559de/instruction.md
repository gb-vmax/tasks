# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with module exports in the MDX remark plugin. When trying to import and use the plugin, I'm getting unexpected behavior where the exported module properties are not accessible as expected.

### Reproduction

```js
const remarkMdx = require('remark-mdx');

// Trying to access exported properties
console.log(remarkMdx);
// Expected: Object with __esModule: true and other exports
// Actual: Empty object or missing expected properties
```

When using the plugin in a Jest configuration or other CommonJS environments, the module doesn't seem to export its members correctly. This is breaking our build process.

### Expected behavior

The module should properly export its members with `__esModule` set to `true` and all exported functions/objects should be accessible when requiring the module.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x
- Environment: Jest/CommonJS

---
Repository: /testbed
