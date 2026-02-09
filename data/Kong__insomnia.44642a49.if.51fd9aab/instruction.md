# Bug Report

### Describe the bug

The `filterHeaders` function is not working as expected and returns an empty array even when valid headers and a name parameter are provided. It seems like the filtering logic has been broken and headers that should be returned are being filtered out incorrectly.

### Reproduction

```js
const headers = [
  { name: 'Content-Type', value: 'application/json' },
  { name: 'Authorization', value: 'Bearer token123' }
];

const result = filterHeaders(headers, 'Content-Type');
console.log(result); // Expected: [{ name: 'Content-Type', value: 'application/json' }]
                     // Actual: []
```

The function returns an empty array instead of filtering and returning the matching headers.

### Expected behavior

When calling `filterHeaders` with a valid array of headers and a name string, it should return an array containing only the headers that match the specified name. Currently it's returning an empty array for all valid inputs.

### Additional context

This is breaking header filtering functionality across the application. Any code that relies on `filterHeaders` to extract specific headers is no longer working correctly.

---
Repository: /testbed
