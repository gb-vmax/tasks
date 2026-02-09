# Bug Report

### Describe the bug

The `filterHeaders` function is not working as expected after a recent update. When trying to filter headers by name, the function returns an empty array instead of the matching headers.

### Reproduction

```js
const headers = [
  { name: 'Content-Type', value: 'application/json' },
  { name: 'Authorization', value: 'Bearer token123' },
  { name: 'Accept', value: '*/*' }
];

// This returns an empty array instead of the matching header
const result = filterHeaders(headers, 'Content-Type');
console.log(result); // Expected: [{ name: 'Content-Type', value: 'application/json' }]
                     // Actual: []
```

### Steps to reproduce
1. Create an array of header objects with `name` and `value` properties
2. Call `filterHeaders` with the array and a header name string
3. The function returns an empty array instead of filtering the headers

This is breaking header filtering functionality across the application. The function used to work fine but now it seems like headers are never being matched.

### Expected behavior
The function should return headers that match the provided name parameter.

---
Repository: /testbed
