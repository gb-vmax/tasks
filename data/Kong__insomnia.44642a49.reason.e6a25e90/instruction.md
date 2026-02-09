# Bug Report

### Describe the bug
When calling `response.reason()` on a response object, it throws an error `reason: response status is not properly initialized` even though the response appears to be valid and has status information.

### Reproduction
```js
// After making a request
const response = pm.response;

// This now throws an error
const reason = response.reason();
// Error: reason: response status is not properly initialized
```

The response object has all the expected properties (code, status, responseTime) but calling `reason()` fails with the initialization error.

### Expected behavior
The `reason()` method should return the status text (e.g., "OK", "Not Found") without throwing an error when the response is properly formed.

### Additional context
This appears to have started happening recently. Previously, `reason()` would return the status without any issues. The response object itself seems fine - I can access `response.code` and other properties without problems.

---
Repository: /testbed
