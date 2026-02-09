# Bug Report

### Describe the bug

I'm encountering an issue where ES module exports are not being recognized correctly after a recent update. When trying to import modules, I'm getting errors related to `__esModule` property not being found or recognized properly.

### Reproduction

The issue appears when using CommonJS interop with ES modules. The module's `__esModule` marker seems to be set incorrectly, causing import/export resolution to fail.

```js
// Attempting to import a module
import something from 'remark-gfm';

// Results in module resolution errors
// The __esModule property is not being detected correctly
```

### Expected behavior

The `__esModule` property should be properly set on the module object to allow correct CommonJS/ES module interoperability. Imports should work without errors.

### System Info
- Node version: 18.x
- Module system: CommonJS with ES module interop

---
Repository: /testbed
