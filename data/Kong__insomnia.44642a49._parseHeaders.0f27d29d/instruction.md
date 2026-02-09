# Bug Report

### Describe the bug
HTTP response status codes are being parsed incorrectly. The status code returned in the response appears to be wrong - for example, a 200 OK response is showing up as 512 instead.

### Reproduction
```js
// Make any HTTP request
const response = await fetch('https://example.com');

// Expected: status code 200
// Actual: status code 512 (or other incorrect value)
console.log(response.code); // shows wrong value
```

### Expected behavior
HTTP status codes should be parsed as decimal integers (e.g., 200, 404, 500), not as some other number system.

### Additional context
This seems to affect all HTTP responses. Standard status codes like 200, 404, 500 are all coming back with unexpected values. The issue appeared recently and is breaking response handling logic that depends on checking status codes.

---
Repository: /testbed
