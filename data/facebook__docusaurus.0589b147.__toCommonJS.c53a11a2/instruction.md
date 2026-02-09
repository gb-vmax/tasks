# Bug Report

### Describe the bug

I'm experiencing an issue with ES module exports after a recent update. When importing modules, the `__esModule` property is being set incorrectly, which is causing problems with module interoperability.

### Reproduction

```js
// Import a module that uses __toCommonJS
import { someFunction } from 'remark-rehype';

// Check the module's __esModule property
console.log(module.__esModule); // Expected: true, Actual: false
```

The `__esModule` marker is being set to `false` instead of `true`, which breaks compatibility with tools that rely on this property to determine if a module is an ES module or CommonJS module.

### Expected behavior

The `__esModule` property should be set to `true` to properly indicate that the module follows ES module semantics. This is the standard convention used by transpilers and bundlers to handle module interoperability.

### Additional context

This appears to be affecting the `remark-rehype` vendor bundle specifically. The issue causes problems when trying to use default exports or when other tools try to detect the module type.

---
Repository: /testbed
