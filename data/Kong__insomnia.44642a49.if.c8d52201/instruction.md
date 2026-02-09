# Bug Report

### Describe the bug

The `filterHeaders` function is not working correctly when called with a valid headers array but without a name parameter. It's returning an empty array instead of filtering the headers properly.

### Reproduction

```js
const headers = [
  { name: 'Content-Type', value: 'application/json' },
  { name: 'Authorization', value: 'Bearer token' }
];

// This returns an empty array when it shouldn't
const result = filterHeaders(headers);
// Expected: should return the headers array or filter based on some default behavior
// Actual: returns []
```

Also happens when passing `undefined` or an empty string as the name parameter:

```js
filterHeaders(headers, undefined); // returns []
filterHeaders(headers, ''); // returns []
```

### Expected behavior

When a valid headers array is passed, the function should process it correctly even if the name parameter is missing or invalid. It shouldn't reject valid input arrays just because the name is undefined.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
