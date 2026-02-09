# Bug Report

### Describe the bug

I'm experiencing an issue with the `anyFactory` function where it's returning the opposite boolean value than expected. When testing with multiple conditions, cases that should return `true` are returning `false` and vice versa.

### Reproduction

```js
// Create a test with multiple check functions
const checks = [
  (val) => val > 5,
  (val) => val < 0
];

const anyCheck = anyFactory(checks);

// This should return true (7 > 5), but returns false
console.log(anyCheck(7)); // Expected: true, Actual: false

// This should return false (3 doesn't match any condition), but returns true
console.log(anyCheck(3)); // Expected: false, Actual: true
```

### Expected behavior

The `anyFactory` should return `true` if ANY of the provided checks pass, and `false` if NONE of them pass. Currently it seems to be doing the inverse - returning `false` when a check passes and `true` when all checks fail.

### Additional context

This appears to have broken after a recent update. The logic seems inverted compared to how it used to work. Any help would be appreciated!

---
Repository: /testbed
