# Bug Report

### Describe the bug

The unused external import warnings are being triggered incorrectly. I'm getting warnings for imports that are actually being used in my code, while imports that are truly unused are not generating any warnings at all.

### Reproduction

```js
// external-lib is an external module
import { usedFunction, unusedFunction } from 'external-lib';

// This function is actually used in the code
usedFunction();

// unusedFunction is never called
```

After building, I'm getting a warning about `usedFunction` being unused, even though it's clearly being used. Meanwhile, `unusedFunction` which is actually unused doesn't trigger any warning.

### Expected behavior

The build should warn about `unusedFunction` (which is actually unused) and should NOT warn about `usedFunction` (which is being used).

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
