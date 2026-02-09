# Bug Report

### Describe the bug

I'm experiencing an issue where `undefined` values are being treated as `null` in the bundled output. When I use `undefined` in my code, it gets replaced with `null` instead, which breaks the expected behavior.

### Reproduction

```js
// Input code
const value = undefined;
console.log(value === undefined); // Expected: true
console.log(typeof value); // Expected: 'undefined'

// After bundling, the output behaves as if:
const value = null;
console.log(value === undefined); // Actual: false
console.log(typeof value); // Actual: 'object'
```

This is causing issues in my application where I need to distinguish between `null` and `undefined` values. For example:

```js
function processValue(val) {
  if (val === undefined) {
    return 'no value provided';
  }
  if (val === null) {
    return 'explicitly set to null';
  }
  return val;
}

// This should return 'no value provided' but returns 'explicitly set to null'
processValue(undefined);
```

### Expected behavior

`undefined` should remain as `undefined` in the bundled code and not be converted to `null`. These are distinct JavaScript values with different semantics and should be preserved.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
