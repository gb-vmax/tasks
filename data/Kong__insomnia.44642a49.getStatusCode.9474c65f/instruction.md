# Bug Report

### Describe the bug

When using the response context API, the new status code helper methods (`isInformational()`, `isSuccess()`, `isRedirect()`, `isClientError()`, `isServerError()`) are not working correctly. They always return `false` even for valid HTTP status codes.

### Reproduction

```js
// Assuming a response with status code 200
const response = getResponse();

console.log(response.getStatusCode()); // Returns 200
console.log(response.isSuccess()); // Returns false (expected: true)
console.log(response.isClientError()); // Returns false (correct)
```

The same issue occurs with all the new helper methods - they don't seem to recognize valid status codes in their respective ranges.

### Expected behavior

- `isInformational()` should return `true` for status codes 100-199
- `isSuccess()` should return `true` for status codes 200-299
- `isRedirect()` should return `true` for status codes 300-399
- `isClientError()` should return `true` for status codes 400-499
- `isServerError()` should return `true` for status codes 500-599

### Additional context

This appears to have started after the recent changes to the response plugin context. The `getStatusCode()` method itself seems to return the correct value, but the helper methods that depend on it are not functioning as expected.

---
Repository: /testbed
