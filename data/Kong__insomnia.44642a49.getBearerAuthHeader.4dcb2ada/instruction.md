# Bug Report

### Describe the bug

When using bearer authentication with tokens that have leading or trailing whitespace, the token is no longer being trimmed before being added to the Authorization header. This causes authentication to fail because the token value includes the whitespace.

### Reproduction

```js
// Create a bearer auth header with a token that has whitespace
const token = '  myAccessToken123  ';
const header = getBearerAuthHeader(token);

// Expected: "Bearer myAccessToken123"
// Actual: "Bearer   myAccessToken123  "
```

The whitespace in the token is preserved, which breaks authentication with most APIs since they expect the token to be trimmed.

### Expected behavior

The token should be automatically trimmed of leading/trailing whitespace before being included in the Authorization header, similar to how the prefix is trimmed. This was working in previous versions.

### Additional context

This affects any request using bearer token authentication where the token value might accidentally include whitespace (e.g., copied from a text file, environment variable with extra spaces, etc.).

---
Repository: /testbed
