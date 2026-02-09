# Bug Report

### Describe the bug

I'm experiencing an issue where modules with side effects are not being tracked correctly in the dependency graph. It appears that some side effect dependencies are being skipped during the module resolution process, which causes certain modules to not be included in the final bundle even though they should be.

### Reproduction

```js
// moduleA.js - has side effects
console.log('Side effect A');
export const a = 1;

// moduleB.js - has side effects
console.log('Side effect B');
export const b = 2;

// moduleC.js - has side effects
console.log('Side effect C');
export const c = 3;

// main.js
import { a } from './moduleA.js';
import { b } from './moduleB.js';
import { c } from './moduleC.js';
```

When bundling this code, I notice that some of the side effect modules are missing from the output. The console logs don't all execute as expected - it seems like every other module is being skipped.

### Expected behavior

All modules with side effects should be included in the bundle and their side effects should execute in the correct order. Every module that is imported and has side effects should be tracked as a dependency.

### Additional context

This seems to have started happening recently. The dependency tracking appears to be inconsistent - sometimes certain modules are included, sometimes they're not. It's almost like the algorithm is alternating between including and excluding modules.

---
Repository: /testbed
