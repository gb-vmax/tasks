# Bug Report

### Describe the bug
The `getContentTypeFromHeaders` function is not returning the correct Content-Type header value. When I pass in an array of headers that includes a Content-Type header, the function returns `null` (or the default value) instead of the actual Content-Type value.

### Reproduction
```js
const headers = [
  { name: 'Content-Type', value: 'application/json' },
  { name: 'Authorization', value: 'Bearer token123' }
];

const contentType = getContentTypeFromHeaders(headers);
console.log(contentType); // Expected: 'application/json', Actual: null
```

### Expected behavior
The function should find and return the value of the Content-Type header when it exists in the headers array. It should only return the default value (or null) when the Content-Type header is not present.

### Additional context
This seems to have started happening recently. The function works correctly when the headers array is empty or when Content-Type is missing, but fails to find it when it's actually present in the array.

---
Repository: /testbed
