# Bug Report

### Describe the bug

When using optional chaining with member expressions that evaluate to a non-nullish value, the chain is incorrectly being skipped. This causes side effects to not be properly tracked in certain scenarios.

### Reproduction

```js
const obj = {
  prop: {
    method() {
      console.log('side effect');
    }
  }
};

// Using optional chaining when obj.prop is defined
obj.prop?.method();

// The method call should execute since obj.prop is not null/undefined,
// but the chain is being skipped incorrectly
```

### Expected behavior

When using optional chaining (`?.`), the chain should only be skipped if the value before `?.` is `null` or `undefined`. If the value is defined (not null/undefined), the chain should continue executing normally and all side effects should be tracked.

In the example above, since `obj.prop` is defined, `method()` should be called and its side effects should be properly detected.

### Additional context

This appears to be related to how optional member expressions determine whether to skip the rest of the chain. The logic seems inverted - it's skipping when the value is NOT null/undefined, rather than when it IS null/undefined.

---
Repository: /testbed
