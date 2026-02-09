# Bug Report

### Describe the bug

The `filterHeaders` function seems to have broken after a recent update. When I try to filter headers by name, I'm getting unexpected behavior - the function is returning an empty array even when there are matching headers in the input.

### Reproduction

```js
const headers = [
  { name: 'Content-Type', value: 'application/json' },
  { name: 'Authorization', value: 'Bearer token123' },
  { name: 'Accept', value: '*/*' }
];

// This returns an empty array instead of the filtered results
const filtered = filterHeaders(headers, 'content-type');
console.log(filtered); // Expected: [{ name: 'Content-Type', value: 'application/json' }]
                       // Actual: []
```

### Expected behavior

The function should return matching headers when a valid name is provided. It was working fine before but now it's not filtering anything.

### Additional context

This is blocking our API request functionality since we rely on this to extract specific headers from responses. The headers array is valid and the name parameter is a proper string, but nothing is being returned.

---
Repository: /testbed
