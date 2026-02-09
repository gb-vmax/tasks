# Bug Report

### Describe the bug

I'm experiencing an issue with optional chaining in my bundled code. When using optional chaining with member expressions that have side effects, the code is being incorrectly tree-shaken or the side effects are not being preserved as expected.

### Reproduction

```js
const obj = {
  a: {
    b: () => console.log('side effect')
  }
};

// This should call the function and log 'side effect'
obj?.a?.b();

// Also affects cases where the property access itself has effects
const result = obj?.a?.[someGetterWithSideEffect()];
```

After bundling, the side effects from the optional chaining expressions are not being executed correctly. It seems like the bundler is treating these expressions as if they don't have effects when they actually do.

### Expected behavior

Optional chaining expressions that contain side effects (like function calls or property accesses with getters) should preserve those side effects during bundling. The code should execute the same way before and after bundling.

### Additional context

This seems to have started happening recently. I'm not sure if this is related to tree-shaking optimizations or how optional chaining is being handled internally.

---
Repository: /testbed
