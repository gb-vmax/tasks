# Bug Report

### Describe the bug

HTTP response status codes are being parsed incorrectly, resulting in unexpected values. For example, a `200 OK` response is being interpreted as `512` instead of `200`.

### Reproduction

When making any HTTP request and checking the response status code, the value is wrong:

```js
// Expected: 200
// Actual: 512

// Expected: 404
// Actual: 1028

// Expected: 500
// Actual: 1280
```

It seems like the status codes are being converted from the wrong number base. Standard HTTP status codes are decimal (base 10), but they appear to be parsed as hexadecimal values instead.

### Expected behavior

HTTP status codes should be returned as their standard decimal values:
- 200 for OK
- 404 for Not Found
- 500 for Internal Server Error
- etc.

### Additional context

This affects all HTTP responses and makes it impossible to properly handle different response status codes in the application. The issue appears to be in the response header parsing logic.

---
Repository: /testbed
