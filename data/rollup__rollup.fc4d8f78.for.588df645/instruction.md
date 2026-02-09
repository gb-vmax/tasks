# Bug Report

### Describe the bug

I'm experiencing an issue with module side effect dependencies where some dependencies are being skipped during the collection process. When a module has multiple side effect dependencies, it appears that only every other dependency is being added to the `alwaysCheckedDependencies` set, causing some dependencies to be missed entirely.

### Reproduction

```js
// Module with multiple side effect dependencies
import './sideEffect1.js'
import './sideEffect2.js'
import './sideEffect3.js'
import './sideEffect4.js'

// When analyzing dependencies, only sideEffect1 and sideEffect3 
// are being tracked, while sideEffect2 and sideEffect4 are skipped
```

### Expected behavior

All side effect dependencies should be tracked and added to the dependency set. Every module that has side effects should be included in the analysis, not just alternating ones.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to have started happening recently and is causing bundling issues where certain side effects are not being properly evaluated.

---
Repository: /testbed
