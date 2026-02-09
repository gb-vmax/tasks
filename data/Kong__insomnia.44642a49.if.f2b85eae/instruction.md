# Bug Report

### Describe the bug

The `filterHeaders` function is returning an empty array when a valid headers array is passed without a name parameter. This breaks filtering functionality when you want to get all headers.

### Reproduction

```js
const headers = [
  { name: 'Content-Type', value: 'application/json' },
  { name: 'Authorization', value: 'Bearer token' }
];

// This should return all headers but returns empty array instead
const result = filterHeaders(headers);
console.log(result); // Expected: headers array, Actual: []

// This also returns empty array when it shouldn't
const result2 = filterHeaders(headers, undefined);
console.log(result2); // Expected: headers array, Actual: []
```

### Expected behavior

When `name` parameter is not provided or is undefined, the function should return all headers instead of an empty array. The filtering should only apply when a valid name string is provided.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
