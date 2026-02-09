# Bug Report

### Describe the bug

I'm experiencing an issue with tree-shaking where code that should be included in the bundle is being incorrectly removed. This appears to be related to call expressions and how they're being marked for inclusion during the bundling process.

### Reproduction

```js
// entry.js
import { sideEffect } from './module.js';

if (condition) {
  sideEffect();
}

// module.js
export function sideEffect() {
  console.log('This should always be included');
  window.globalState = true;
}
```

When bundling this code, the `sideEffect` function and its call are being removed from the output bundle even though they have side effects that should be preserved.

### Expected behavior

Functions with side effects should be included in the bundle when called, regardless of whether they appear in conditional branches. The call expression should properly mark all necessary code paths for inclusion.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: macOS

This seems to have started happening recently. The bundle output is missing critical code that was previously included correctly.

---
Repository: /testbed
