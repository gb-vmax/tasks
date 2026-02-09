# Bug Report

### Describe the bug

I'm experiencing an issue with the `getContentTypeFromHeaders` function where it's not correctly identifying the Content-Type header. The function seems to be matching headers too loosely, causing it to return incorrect values when header names contain "content-type" as a substring rather than being an exact match.

### Reproduction

```js
const headers = [
  { name: 'X-Custom-Content-Type-Override', value: 'text/plain' },
  { name: 'Content-Type', value: 'application/json' }
];

const contentType = getContentTypeFromHeaders(headers);
// Returns 'text/plain' instead of 'application/json'
```

The function is now matching any header name that includes "content-type" anywhere in the string, so headers like "X-Custom-Content-Type-Override" or "Accept-Content-Type" would incorrectly be treated as the Content-Type header.

### Expected behavior

The function should only match headers where the name is exactly "content-type" (case-insensitive), not headers that merely contain "content-type" as part of the name. In the example above, it should return `'application/json'`.

### Additional context

This also seems to have introduced an issue where passing an empty array causes the function to return `null` instead of the default value that should be returned when no Content-Type header is found.

---
Repository: /testbed
