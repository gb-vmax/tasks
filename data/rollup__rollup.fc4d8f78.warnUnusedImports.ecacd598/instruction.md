# Bug Report

### Describe the bug

I'm getting incorrect warnings about unused external imports. The warning system seems to be reporting modules that are actually being used, and I suspect it's not correctly identifying which importers are actually using the imports.

### Reproduction

```js
// external-lib.js (external module)
export const usedFunction = () => {};
export const unusedFunction = () => {};

// my-module.js
import { usedFunction } from 'external-lib';

usedFunction(); // This is clearly being used
```

When building with rollup, I'm getting warnings about `usedFunction` being unused from `external-lib`, even though it's clearly being imported and used in `my-module.js`. 

The warning appears to be triggered for imports that are actually used, which is the opposite of what should happen.

### Expected behavior

- No warnings should be shown for `usedFunction` since it's actually being used
- Only truly unused imports like `unusedFunction` should trigger warnings
- The warning should correctly identify which modules are importing the unused exports

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
