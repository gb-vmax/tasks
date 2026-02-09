# Bug Report

### Describe the bug

After a recent update, the `getContentTypeFromHeaders` function is not returning the content-type header value when it should. The function now returns `null` or the default value even when a valid content-type header is present in the headers array.

### Reproduction

```js
const headers = [
  { name: 'Content-Type', value: 'application/json' },
  { name: 'Accept', value: '*/*' }
];

const contentType = getContentTypeFromHeaders(headers);
// Expected: 'application/json'
// Actual: null
```

This also happens with other valid content types:

```js
const headers = [
  { name: 'content-type', value: 'text/html; charset=utf-8' }
];

const result = getContentTypeFromHeaders(headers);
// Expected: 'text/html; charset=utf-8'
// Actual: null
```

### Expected behavior

The function should return the content-type header value when a valid content-type header exists in the headers array. It should handle case-insensitive header names and return the original value including any parameters like charset.

### Additional context

This worked fine in previous versions. The issue seems to affect all content-type values, making it impossible to detect the content type of HTTP requests/responses.

---
Repository: /testbed
