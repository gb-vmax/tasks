# Bug Report

### Describe the bug

I'm experiencing an issue where async functions are being incorrectly identified. It seems like the async detection logic is inverted - non-async functions are being treated as async, and actual async functions are being treated as synchronous.

### Reproduction

```js
// Regular synchronous function
function regularFunc() {
  return 42;
}

// Async function
async function asyncFunc() {
  return await Promise.resolve(42);
}

// The async detection appears to be backwards
// regularFunc is detected as async (incorrect)
// asyncFunc is detected as non-async (incorrect)
```

### Expected behavior

Synchronous functions should be correctly identified as non-async, and async functions should be correctly identified as async. The current behavior seems to have the logic reversed.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
