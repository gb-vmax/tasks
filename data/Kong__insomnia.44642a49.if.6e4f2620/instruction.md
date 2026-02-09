# Bug Report

### Describe the bug

The `filterHeaders` function is returning an empty array in cases where it should be filtering headers. It seems like the function is not working correctly when a valid header name is provided.

### Reproduction

```js
const headers = [
  { name: 'Content-Type', value: 'application/json' },
  { name: 'Authorization', value: 'Bearer token' },
  { name: 'Content-Type', value: 'text/html' }
];

// This returns an empty array instead of filtering
const result = filterHeaders(headers, 'Content-Type');
console.log(result); // Expected: array with 2 Content-Type headers, Actual: []
```

### Expected behavior

When calling `filterHeaders` with a valid headers array and a name string, it should return all headers matching that name. Currently it's returning an empty array even when the inputs are valid.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
