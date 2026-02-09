# Bug Report

### Describe the bug

Import declarations are being treated as having side effects even when they're just importing bindings without any actual side-effecting code. This causes tree-shaking to fail and results in import statements being retained in the output bundle even when they should be removed.

### Reproduction

```js
// lib.js
export const unused = 'test';
export const alsoUnused = 'value';

// main.js
import { unused } from './lib.js';

// unused is never referenced
console.log('hello');
```

When bundling this code, the import statement is kept in the output even though `unused` is never used anywhere in the code. The import should be completely removed during tree-shaking since it has no side effects.

### Expected behavior

Pure import declarations (those that only import bindings without executing side-effecting code) should be removed by tree-shaking when the imported bindings are unused. The import statement should only be retained if:
- The imported values are actually used
- The module itself has side effects (like top-level code execution)

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
