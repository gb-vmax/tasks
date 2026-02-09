# Bug Report

### Describe the bug

I'm experiencing an issue where pure functions are being incorrectly treated as having side effects during tree-shaking. This is causing code that should be eliminated to remain in the bundle.

### Reproduction

```js
// utils.js
export function pureHelper(x) {
  return x * 2;
}

export function unused() {
  return pureHelper(5);
}

// main.js
import { pureHelper } from './utils.js';

console.log(pureHelper(10));
```

When bundling this code, the `unused` function should be tree-shaken away since it's never called. However, it's being retained in the output bundle even though it has no side effects.

### Expected behavior

Pure functions that are not used should be removed during tree-shaking. The bundler should correctly identify that these functions have no side effects and can be safely eliminated.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to have started happening recently. Previously, unused pure functions were being correctly removed from the bundle.

---
Repository: /testbed
