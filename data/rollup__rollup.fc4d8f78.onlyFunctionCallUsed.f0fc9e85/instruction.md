# Bug Report

### Describe the bug

I'm experiencing an issue with tree-shaking of named function declarations. When a function is only used via function calls (not referenced directly), it's being incorrectly retained in the bundle even though it should be tree-shaken away.

### Reproduction

```js
// module.js
export function myFunction() {
  console.log('test');
}

// main.js
import { myFunction } from './module.js';
myFunction();
```

In this case, `myFunction` is only called and never referenced as a value, so it should be eligible for certain optimizations. However, the function is not being handled correctly during the tree-shaking analysis phase.

### Expected behavior

Named function declarations that are only used via direct function calls should be properly analyzed and tree-shaken when appropriate. The bundler should correctly detect when a function is only used for its call behavior.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
