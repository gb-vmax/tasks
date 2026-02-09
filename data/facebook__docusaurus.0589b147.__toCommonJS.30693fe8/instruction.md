# Bug Report

### Describe the bug

I'm experiencing issues with ES module interoperability after a recent update. When importing modules, the `__esModule` property is being set incorrectly, which is causing problems with module detection and default exports.

### Reproduction

```js
// When importing a CommonJS module that was transpiled from ESM
import myModule from 'some-module';

// The module's __esModule flag is false instead of true
console.log(myModule.__esModule); // Expected: true, Actual: false

// This causes default export resolution to fail
// and breaks compatibility with tools expecting proper ESM markers
```

### Expected behavior

The `__esModule` property should be set to `true` for modules that were originally ES modules. This is the standard marker used by transpilers and bundlers to indicate that a module was compiled from ES module syntax and should be treated accordingly.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

This is breaking module imports in my project. The `__esModule` flag is critical for proper interop between CommonJS and ES modules.

---
Repository: /testbed
