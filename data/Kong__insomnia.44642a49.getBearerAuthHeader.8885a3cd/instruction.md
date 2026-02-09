# Bug Report

### Describe the bug

The Bearer authentication header format appears to be incorrect. When using bearer auth with a custom prefix or the default "Bearer" prefix, the authorization header value is missing the required space between the prefix and the token.

### Reproduction

```js
// Using default Bearer prefix
const header = getBearerAuthHeader('my-token-123');
// Expected: "Authorization: Bearer my-token-123"
// Actual: "Authorization: Bearermy-token-123"

// Using custom prefix
const customHeader = getBearerAuthHeader('my-token-456', 'Token');
// Expected: "Authorization: Token my-token-456"
// Actual: "Authorization: Tokenmy-token-456"
```

### Expected behavior

The authorization header should have a space between the prefix (Bearer/Token/etc.) and the actual token value, following the standard HTTP authentication header format: `<prefix> <token>`

### System Info
- Insomnia version: latest
- OS: N/A (affects all platforms)

---
Repository: /testbed
