# Bug Report

### Describe the bug

The `filterHeaders` function is returning an empty array for all inputs, even when provided with valid headers array and name string. This appears to be breaking header filtering functionality across the application.

### Reproduction

```js
const headers = [
  { name: 'Content-Type', value: 'application/json' },
  { name: 'Authorization', value: 'Bearer token' },
  { name: 'Content-Type', value: 'text/html' }
];

const filtered = filterHeaders(headers, 'Content-Type');
console.log(filtered);
// Expected: Array with 2 Content-Type headers
// Actual: Empty array []
```

### Expected behavior

When calling `filterHeaders` with a valid headers array and a name string, it should return the filtered headers that match the provided name. Currently it's returning an empty array in all cases.

### Additional context

This seems to have broken after a recent change. The function is now rejecting valid inputs and always returning empty arrays, which is preventing header filtering from working anywhere in the codebase.

---
Repository: /testbed
