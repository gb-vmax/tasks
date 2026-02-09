# Bug Report

### Describe the bug
When accessing response status codes through the plugin API, successful responses (2xx status codes) are returning -1 instead of the actual status code. Additionally, responses without a status code are defaulting to 200 instead of 0.

### Reproduction
```js
// After making a successful request with status 200
const statusCode = context.response.getStatusCode();
console.log(statusCode); // Expected: 200, Actual: -1

// For a 201 Created response
const statusCode = context.response.getStatusCode();
console.log(statusCode); // Expected: 201, Actual: -1

// For responses without a status code
const statusCode = context.response.getStatusCode();
console.log(statusCode); // Expected: 0, Actual: 200
```

### Expected behavior
- `getStatusCode()` should return the actual HTTP status code (200, 201, 204, etc.) for successful responses
- For responses without a status code, it should return 0, not 200
- Only non-2xx status codes (errors, redirects, etc.) should return their actual values

### System Info
- Insomnia version: latest
- Plugin API context: response

This is breaking plugins that rely on checking specific success status codes (like differentiating between 200 OK and 201 Created).

---
Repository: /testbed
