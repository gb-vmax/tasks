# Bug Report

### Describe the bug

I'm encountering an issue with the `anyFactory` function where it's returning unexpected values when checking against multiple test conditions. Instead of returning a boolean `true` when a condition matches, it seems to be returning the actual result of the check function, which can be any truthy value.

### Reproduction

```js
// Create a factory with multiple test functions
const tests = [
  (node) => node.type === 'text' ? { matched: true } : false,
  (node) => node.type === 'code' ? { matched: true } : false
];

const anyTest = anyFactory(tests);

// When checking a node
const node = { type: 'text' };
const result = anyTest(node);

// Expected: true
// Actual: { matched: true } (the return value from the check function)
```

The function is also checking one extra iteration beyond the array length, which could potentially cause issues when accessing `checks[index3]` at an out-of-bounds index.

### Expected behavior

The `anyFactory` should return a boolean `true` when any of the test conditions pass, not the actual return value from the check function. It should maintain consistent return types.

### Additional context

This appears to affect any code that relies on the `anyFactory` utility for combining multiple test conditions. The inconsistent return type can break downstream logic that expects strict boolean values.

---
Repository: /testbed
