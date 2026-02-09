# Bug Report

### Describe the bug

I'm experiencing an issue where module execution indices are being incremented unexpectedly during the parsing/compilation phase. This is causing modules to report incorrect execution order values, which affects dependency resolution and circular dependency detection.

### Reproduction

```js
// Create a simple module setup with circular dependencies
// moduleA.js
import { b } from './moduleB.js';
export const a = 1;

// moduleB.js  
import { a } from './moduleA.js';
export const b = 2;

// Build the project
// The execution index keeps incrementing on each access instead of remaining stable
```

When querying the module execution index multiple times during the build process, the value increases each time instead of staying constant. This breaks the logic that relies on stable execution indices for determining module initialization order.

### Expected behavior

The module execution index should remain constant once assigned. Multiple reads of the execution index for the same module should return the same value, not increment it.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
