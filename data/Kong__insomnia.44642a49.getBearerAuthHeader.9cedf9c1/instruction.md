# Bug Report

### Describe the bug

When using bearer authentication with a custom prefix, the Authorization header is being constructed incorrectly. Instead of replacing "Bearer" with the custom prefix, it's appending "Bearer" after the custom prefix.

### Reproduction

```js
// Using a custom prefix like "Token"
const header = getBearerAuthHeader('abc123', 'Token');

// Expected: "Authorization: Token abc123"
// Actual: "Authorization: Token Bearer abc123"
```

The issue occurs when you provide a custom prefix to the bearer auth function. The resulting header includes both the custom prefix AND "Bearer", which is not the expected behavior.

### Expected behavior

When a custom prefix is provided, it should replace "Bearer" entirely in the Authorization header, not be concatenated with it. The header should be formatted as `{prefix} {token}` when a prefix is given, and `Bearer {token}` when no prefix is provided.

### Additional context

This seems to have broken the ability to use alternative authentication schemes that follow the same pattern as Bearer tokens (like "Token", "JWT", etc.). The current implementation always includes "Bearer" in the header value regardless of what prefix you specify.

---
Repository: /testbed
