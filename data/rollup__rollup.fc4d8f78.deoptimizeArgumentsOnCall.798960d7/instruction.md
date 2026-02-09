# Bug Report

### Describe the bug

I'm encountering an issue with tree-shaking optimization for certain global functions. It seems like the wrong argument is being tracked for side effects, causing incorrect dead code elimination.

When using functions that mutate their arguments (like `Object.assign`, `Object.defineProperty`, etc.), the bundler is not properly detecting which argument gets mutated. This leads to code being incorrectly removed during the build process even though it has side effects.

### Reproduction

```js
const obj1 = { a: 1 };
const obj2 = { b: 2 };

// This should preserve obj1 since it gets mutated
Object.assign(obj1, obj2);

console.log(obj1); // Expected: { a: 1, b: 2 }
```

After bundling, the `Object.assign` call might be removed or optimized incorrectly because the side effect on the first argument isn't being tracked properly.

### Expected behavior

The bundler should correctly identify that the first argument to these mutation functions is being modified and preserve any code that depends on those side effects.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to have started recently - possibly related to changes in how global function calls are analyzed for side effects.

---
Repository: /testbed
