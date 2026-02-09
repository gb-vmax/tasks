# Bug Report

### Describe the bug

I'm experiencing an issue with variable deoptimization when accessing nested properties. It seems like the deoptimization logic is not being properly propagated through the path, causing incorrect optimization behavior in the bundler.

### Reproduction

```js
// Example code that triggers the issue
const obj = {
  nested: {
    value: 42
  }
};

// When accessing nested properties
const { nested } = obj;
console.log(nested.value);

// The deoptimization doesn't work correctly for the nested path
```

When bundling code with nested object destructuring and property access, the optimizer incorrectly assumes certain paths are safe when they shouldn't be. This leads to potential issues where side effects or mutations might not be properly tracked.

### Expected behavior

The deoptimization should properly traverse the full path and deoptimize all nested properties accordingly, not just reset to an empty path.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
