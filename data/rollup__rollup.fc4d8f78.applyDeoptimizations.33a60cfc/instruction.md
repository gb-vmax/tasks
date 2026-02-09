# Bug Report

### Describe the bug

I'm experiencing an issue where modules that should be tree-shaken are being incorrectly included in the bundle. It appears that modules without side effects are being marked as executed and included even when they're not actually used in the code.

### Reproduction

```js
// module-a.js (no side effects)
export const unusedFunction = () => {
  console.log('This should be tree-shaken');
};

// module-b.js
import { unusedFunction } from './module-a.js';

// The function is imported but never called
export const myFunction = () => {
  return 'hello';
};

// main.js
import { myFunction } from './module-b.js';
console.log(myFunction());
```

In this case, `module-a.js` should be completely tree-shaken from the bundle since `unusedFunction` is never actually used. However, the module is being included in the final bundle.

### Expected behavior

Modules that are imported but whose exports are never used should be tree-shaken from the bundle when they have no side effects. The bundle should only include code that is actually executed or has side effects.

### Additional context

This seems to affect modules that are transitively imported through other modules. Direct imports that aren't used appear to be tree-shaken correctly, but when there's an intermediate module in the chain, the unused module gets included.

---
Repository: /testbed
