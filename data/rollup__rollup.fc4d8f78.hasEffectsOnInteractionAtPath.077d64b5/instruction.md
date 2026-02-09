# Bug Report

### Describe the bug

I'm experiencing an issue where variables are being incorrectly marked as having side effects when they're accessed. It seems like the check for whether a variable is null is missing in certain cases, causing the bundler to be overly conservative about tree-shaking.

### Reproduction

```js
// main.js
import { pureFunction } from './utils.js';

const result = pureFunction.someProperty;
console.log(result);
```

```js
// utils.js
export const pureFunction = {
  someProperty: 'value'
};
```

When bundling this code, the access to `pureFunction.someProperty` is being treated as if it has side effects, even though it's just a simple property access on a pure object.

### Expected behavior

The bundler should recognize that accessing properties on pure variables doesn't have side effects and should handle the tree-shaking correctly. The variable null check should be performed before attempting to evaluate side effects.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
