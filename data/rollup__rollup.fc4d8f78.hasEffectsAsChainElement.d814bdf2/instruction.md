# Bug Report

### Describe the bug

I'm encountering an issue with optional chaining where side effects are not being properly tracked when the object in a member expression evaluates to a non-nullish value. The bundler seems to be incorrectly skipping the chain evaluation in cases where it should continue.

### Reproduction

```js
const obj = {
  method() {
    console.log('side effect');
    return { value: 42 };
  }
};

// This should execute the method and track its side effects
const result = obj?.method()?.value;
```

The method call should be recognized as having side effects and included in the bundle, but it appears to be getting skipped or optimized away incorrectly.

### Expected behavior

When using optional chaining with a non-null/undefined object, the chain should continue evaluating normally and all side effects (like method calls) should be properly tracked and preserved during bundling.

### Additional context

This seems to affect cases where:
1. Optional chaining is used (`?.`)
2. The object being accessed is not null/undefined
3. There are side effects in the chain (like function calls)

The issue appears to be related to how the chain skipping logic determines whether to continue or abort the evaluation.

---
Repository: /testbed
