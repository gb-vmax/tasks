# Bug Report

### Bearer token with whitespace not handled correctly

I'm experiencing an issue with bearer token authentication where tokens containing leading/trailing whitespace are being sent incorrectly in the Authorization header.

### Reproduction
```js
// When setting a bearer token with whitespace
const token = '  my-token-123  ';

// The Authorization header is generated
// Expected: "Bearer my-token-123"
// Actual: "Bearer   my-token-123  "
```

The token value is not being trimmed before being added to the Authorization header, which causes authentication to fail on the server side since the token includes the extra whitespace.

### Expected behavior
The bearer token should be trimmed of any leading/trailing whitespace before being included in the Authorization header value, similar to how the prefix is already being trimmed.

### Additional context
This affects API requests that use bearer token authentication. Servers typically reject tokens with extra whitespace, causing requests to fail with 401 Unauthorized errors even when the token itself is valid.

---
Repository: /testbed
