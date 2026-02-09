# Bug Report

### Describe the bug

I'm experiencing an issue where modules with side effects are not being included in the bundle correctly. It seems like dependencies that should be included because of their side effects are being excluded, causing runtime errors in the final bundle.

### Reproduction

```js
// entry.js
import './moduleWithSideEffects.js'
import { foo } from './main.js'

console.log(foo)

// moduleWithSideEffects.js
// This module has side effects but no exports
window.myGlobal = 'initialized'
console.log('Side effect executed')

// main.js
export const foo = 'bar'
```

When bundling this code, the `moduleWithSideEffects.js` file is not being included in the output even though it has `moduleSideEffects: true` set in the module info. The side effects should execute but they don't appear in the final bundle.

### Expected behavior

Modules marked with `moduleSideEffects: true` should always be included in the bundle, even if they have no exports that are used. The side effects should execute at runtime.

### Additional context

This seems to affect modules that are:
- Imported for their side effects only (no named imports)
- Have `moduleSideEffects: true` configured
- Are part of a dependency chain

The issue appears to be related to how the dependency graph is being traversed when determining which modules to include.

---
Repository: /testbed
