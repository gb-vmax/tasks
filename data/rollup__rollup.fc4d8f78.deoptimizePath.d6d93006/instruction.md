# Bug Report

### Describe the bug

I'm experiencing an issue where property access on function return values is not being properly tracked for side effects. It seems like the deoptimization logic is inverted - paths that should be deoptimized are being skipped, and vice versa.

### Reproduction

```js
// Example code that demonstrates the issue
function getObject() {
  return { prop: 'value' };
}

const result = getObject();
result.prop; // This access should trigger deoptimization tracking
```

When accessing properties on the return value of a function call, the deoptimization tracker appears to be behaving incorrectly. Properties that should be tracked for potential side effects are not being deoptimized properly.

### Expected behavior

Property accesses on function return values should be properly tracked and deoptimized when necessary to ensure correct tree-shaking and side effect detection.

### System Info
- Rollup version: latest
- Node version: 18.x

This seems to have started recently. The logic for checking whether to proceed with deoptimization appears to be backwards - it's returning early when it should continue, and continuing when it should return early.

---
Repository: /testbed
