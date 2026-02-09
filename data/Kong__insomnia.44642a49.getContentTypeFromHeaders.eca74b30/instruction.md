# Bug Report

### Describe the bug

I'm experiencing an issue with the `getContentTypeFromHeaders` function. When I have headers with a `content-type` field, the function is returning `undefined` instead of the actual content type value.

### Reproduction

```js
const headers = [
  { name: 'Content-Type', value: 'application/json' },
  { name: 'Authorization', value: 'Bearer token123' }
];

const contentType = getContentTypeFromHeaders(headers, 'text/plain');
console.log(contentType); // Expected: 'application/json', Actual: undefined
```

The function seems to be looking for the content-type header correctly (case-insensitive matching works), but it's not returning the value properly. Instead, it returns `undefined` even when the header exists.

### Expected behavior

The function should return the value of the content-type header when it exists in the headers array. In the example above, it should return `'application/json'`.

### Additional context

This appears to have started happening recently. The function correctly falls back to the default value when no content-type header is present, but when the header does exist, something is wrong with how the value is being accessed.

---
Repository: /testbed
