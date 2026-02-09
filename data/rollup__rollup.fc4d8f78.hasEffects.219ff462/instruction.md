# Bug Report

### Describe the bug

I'm seeing unexpected behavior with tree-shaking when using global variables in my code. Functions that should be tree-shaken away are being included in the bundle even though they have side effects and aren't being used.

### Reproduction

```js
// utils.js
export function pureGlobalFunction() {
  return Math.random();
}

export function unusedFunction() {
  console.log('This has side effects');
}

// main.js
import { pureGlobalFunction } from './utils.js';

// Only using pureGlobalFunction, but unusedFunction is still in the bundle
console.log(pureGlobalFunction());
```

When I build this with `unknownGlobalSideEffects` enabled in treeshake options, I expect `unusedFunction` to be removed from the bundle since it's not imported or used. However, it's still appearing in the final output.

### Expected behavior

Global functions that are pure should be properly analyzed and unused code should be tree-shaken away when `unknownGlobalSideEffects` is configured.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
