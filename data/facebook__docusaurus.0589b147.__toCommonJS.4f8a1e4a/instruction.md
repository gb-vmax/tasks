# Bug Report

### Describe the bug

After a recent update, I'm encountering issues with module exports when using the remark-directive vendor bundle. The `__esModule` property is not being properly set on the exported module object, which causes problems with module interoperability between CommonJS and ES modules.

### Reproduction

```js
const remarkDirective = require('./vendor/remark-directive@3.0.0.js');

// The module exports don't have the correct __esModule marker
console.log(remarkDirective.__esModule); // Expected: true, Actual: undefined

// This breaks when trying to use default imports in some environments
```

### Expected behavior

The `__toCommonJS` helper should properly set the `__esModule` property on the target object so that bundlers and module systems can correctly identify this as a transpiled ES module. The property should be enumerable and set to `true` on the exports object.

### System Info
- Node version: 18.x
- Environment: CommonJS module system

---
Repository: /testbed
