# Bug Report

### Describe the bug

The unused import warnings are showing incorrect importers. When I have unused external imports, the warning message lists modules that are NOT actually importing the unused symbols, rather than the ones that are.

### Reproduction

```js
// external-lib.js (external module)
export const usedExport = 'used';
export const unusedExport = 'unused';

// module-a.js
import { usedExport, unusedExport } from 'external-lib';
console.log(usedExport); // only using usedExport

// module-b.js  
import { usedExport } from 'external-lib';
console.log(usedExport); // not importing unusedExport at all
```

Expected warning: `unusedExport` is imported but unused in `module-a.js`

Actual warning: `unusedExport` is imported but unused in `module-b.js`

The warning is pointing to the wrong module - it's showing module-b which doesn't even import the unused symbol, instead of module-a which actually imports it but doesn't use it.

### Expected behavior

The unused import warning should correctly identify which modules are importing but not using the external symbols. In the example above, it should warn about `module-a.js`, not `module-b.js`.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
