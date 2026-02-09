# Bug Report

### Describe the bug

I'm experiencing an issue with ES module imports after a recent update. When trying to import from the remark-directive vendor module, the module's `__esModule` property is being set incorrectly, which is causing import resolution problems in my project.

### Reproduction

```js
import remarkDirective from './jest/vendor/remark-directive@3.0.0.js';

// Check the module's __esModule property
console.log(remarkDirective.__esModule); // Expected: true, Actual: false
```

This is breaking interoperability between CommonJS and ES modules. The module should be marked as an ES module but it's currently not being recognized as one.

### Expected behavior

The `__esModule` property should be set to `true` to properly identify this as an ES module and ensure correct import/export behavior across different module systems.

### System Info
- Node version: 18.x
- Module system: ESM/CommonJS interop

---
Repository: /testbed
