# Bug Report

### Describe the bug

I'm experiencing an issue where certain nodes in the AST are not being properly marked as included during tree-shaking. It appears that some code that should be included in the bundle is being incorrectly excluded.

### Reproduction

```js
// Example code that demonstrates the issue
import { someFunction } from './module';

// This call should mark the function as included
someFunction();

// But the function gets tree-shaken out of the final bundle
```

When building with rollup, I'm noticing that some functions/exports that are actually used are being removed from the bundle. This seems to happen specifically with certain patterns where the inclusion logic should be triggered but isn't working correctly.

### Expected behavior

All referenced code should be properly marked as included and retained in the final bundle. The tree-shaking should only remove genuinely unused code.

### System Info
- Rollup version: latest
- Node version: 18.x

This is causing production issues as critical code is being removed from our bundles. Any help would be appreciated!

---
Repository: /testbed
