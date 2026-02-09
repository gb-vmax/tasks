# Bug Report

### Describe the bug

I'm experiencing an issue with object property deoptimization that seems to be causing incorrect behavior in my rollup builds. Objects with integer properties are not being properly deoptimized in certain scenarios, leading to unexpected optimization states.

### Reproduction

```js
const obj = {
  0: 'first',
  1: 'second',
  2: 'third'
};

// Modify integer properties
obj[0] = 'modified';
obj[3] = 'added';

// The deoptimization behavior seems inconsistent
// Sometimes integer properties maintain optimization state when they shouldn't
```

### Expected behavior

When an object has lost track of its properties OR has unknown deoptimized properties OR has unknown deoptimized integers, the deoptimization process should return early and skip further processing. Currently it seems like the logic is requiring ALL three conditions to be true simultaneously before returning, which doesn't match the expected behavior.

This is causing objects to be deoptimized when they should maintain their optimized state, or vice versa.

### System Info

- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
