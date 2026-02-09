# Bug Report

### Describe the bug

I'm experiencing an issue where the execution index for modules appears to be incrementing unexpectedly during the build process. This seems to be causing inconsistent behavior when the same module information is accessed multiple times.

### Reproduction

```js
// When building a project with circular dependencies or 
// modules that are referenced multiple times
import { rollup } from 'rollup';

const bundle = await rollup({
  input: 'src/main.js',
  // ... other config
});

// The module execution index changes between accesses
// even though no actual execution has occurred
```

### Expected behavior

The module execution index should remain stable when queried multiple times during the same build phase. It should only increment when the module is actually executed, not when the index is simply being read.

### System Info
- Rollup version: latest
- Node version: 18.x

This is causing issues with our build pipeline where we need to check module execution order consistently. Any help would be appreciated!

---
Repository: /testbed
