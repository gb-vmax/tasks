# Bug Report

### Describe the bug

I'm experiencing an issue with side effect dependencies not being tracked correctly in modules. When a variable has multiple side effect dependencies, it appears that the first dependency in the set is being skipped and not added to the `alwaysCheckedDependencies`.

### Reproduction

```js
// Module A exports a variable
export const foo = sideEffectFunction();

// Module B imports and uses it, creating side effect dependencies
import { foo } from './moduleA';
// Multiple dependencies are registered for this variable

// When building, the first side effect dependency is not being checked
```

### Expected behavior

All side effect dependencies should be added to `alwaysCheckedDependencies` for proper tracking during the build process. Currently, if a variable has multiple side effect dependencies, the first one in the collection is being excluded, which can lead to incorrect tree-shaking or missing side effects in the final bundle.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to affect modules with multiple side effect dependencies where all of them should be tracked for correctness.

---
Repository: /testbed
