# Bug Report

### Describe the bug

The `filterParameters` function appears to have broken logic - there's duplicate code and the function signature doesn't match the implementation. When trying to filter parameters by name, the function always returns an empty result regardless of the input.

### Reproduction

```js
const params = [
  { name: 'Content-Type', value: 'application/json' },
  { name: 'Authorization', value: 'Bearer token' },
  { name: 'Accept', value: '*/*' }
];

// This returns an empty array instead of filtering
const filtered = filterParameters(params, 'Content-Type');
console.log(filtered); // Expected: [{ name: 'Content-Type', value: 'application/json' }]
                       // Actual: []
```

### Expected behavior

The function should filter and return parameters that match the given name. It looks like there might be some unreachable code or incorrect control flow that's preventing the filtering logic from executing properly.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
