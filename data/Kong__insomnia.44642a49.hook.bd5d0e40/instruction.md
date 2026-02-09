# Bug Report

### Describe the bug

I'm experiencing an issue with default headers in the request hooks system. When setting default headers through environment variables, the system seems to be cutting off or not properly handling header values in certain cases.

### Reproduction

```js
// Set up environment variable with default headers
const DEFAULT_HEADERS = {
  'Authorization': 'Bearer token123',
  'Content-Type': 'application/json',
  'X-Custom-Header': 'null'
}

// Make a request
// Expected: Headers should be set correctly
// Actual: Some header values appear to be truncated or incomplete
```

I noticed this started happening recently. When I check the actual request being sent, some of the header values seem incomplete or malformed. The issue appears to be related to how the header values are being processed, particularly when dealing with the 'null' string value for header removal.

### Expected behavior

- Default headers from environment variables should be applied correctly to requests
- Header values should not be truncated or cut off
- The 'null' value should properly remove headers as intended

### Additional context

This seems to affect the default header mechanism that checks for existing headers and applies them based on the configuration. The behavior is inconsistent and some requests work fine while others have malformed header values.

---
Repository: /testbed
