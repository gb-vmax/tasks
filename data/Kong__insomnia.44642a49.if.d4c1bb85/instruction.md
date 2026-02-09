# Bug Report

### Describe the bug

After a recent update, the `filterHeaders` function is not working correctly. When I try to filter headers by name, I'm getting an empty array back even though matching headers exist.

### Reproduction

```js
const headers = [
  { name: 'Content-Type', value: 'application/json' },
  { name: 'Authorization', value: 'Bearer token123' },
  { name: 'X-Custom-Header', value: 'custom-value' }
];

// This returns an empty array instead of the matching header
const filtered = filterHeaders(headers, 'Content-Type');
console.log(filtered); // Expected: [{ name: 'Content-Type', value: 'application/json' }]
                       // Actual: []
```

### Expected behavior

The function should return headers that match the provided name. In the example above, it should return an array containing the Content-Type header.

### Additional context

This was working fine in the previous version. The function seems to be returning an empty array for all inputs now, even when there are clearly matching headers in the array.

---
Repository: /testbed
