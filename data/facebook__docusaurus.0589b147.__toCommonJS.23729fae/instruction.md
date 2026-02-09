# Bug Report

### Describe the bug

After a recent update, I'm encountering issues with module exports when using rehype-stringify. It appears that the `__esModule` property is not being set correctly, which is causing problems with module interoperability.

### Reproduction

When importing and using rehype-stringify in a CommonJS environment:

```js
const rehypeStringify = require('rehype-stringify');

// The module doesn't behave as expected
// __esModule property seems to be missing or incorrectly configured
console.log(rehypeStringify.__esModule); // Should be true but isn't working right
```

The issue seems to affect how the module is recognized by bundlers and module loaders. Properties from the original module aren't being properly copied over to the export object.

### Expected behavior

The module should export correctly with the `__esModule` marker set to `true`, and all properties from the original module should be accessible on the exported object.

### System Info
- rehype-stringify version: 10.0.0
- Node.js version: Latest
- Environment: CommonJS module system

---
Repository: /testbed
