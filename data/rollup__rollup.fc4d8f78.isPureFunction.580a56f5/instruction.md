# Bug Report

### Describe the bug

When marking functions as pure using `manualPureFunctions`, the detection logic doesn't correctly identify pure functions at the root level (without nested property access). Functions that should be recognized as pure when called directly are not being detected properly.

### Reproduction

```js
// Configuration
const manualPureFunctions = {
  myPureFunc: {
    __PURE__: true
  }
}

// This should be detected as pure but isn't
myPureFunc()

// Only nested calls are being detected
myPureFunc.nested.method()
```

### Expected behavior

When a function is configured as pure in `manualPureFunctions` with the `__PURE__` marker, calling it directly (without property access) should be recognized as a pure function call. Currently, it seems like the path traversal logic is skipping the first element and only checking nested properties.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
