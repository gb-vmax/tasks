# Bug Report

### Describe the bug

I'm experiencing an issue with external module imports where unused imports are not being detected correctly. It seems like the bundler is failing to warn about imports that aren't actually being used in the code.

### Reproduction

```js
// external-lib.js (external module)
export const usedExport = 'used';
export const unusedExport = 'unused';

// main.js
import { usedExport, unusedExport } from 'external-lib';

console.log(usedExport);
// unusedExport is never used
```

### Expected behavior

The bundler should identify `unusedExport` as an unused import from the external module and include it in the warnings. Currently, it's not being reported even though it's clearly not referenced anywhere in the code.

### Additional context

This affects tree-shaking analysis for external modules. The import tracking seems to be inverted - imports that should be flagged as unused are being ignored, while used imports might be getting flagged incorrectly.

---
Repository: /testbed
