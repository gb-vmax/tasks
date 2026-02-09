# Bug Report

### Describe the bug

When using bearer token authentication with a custom prefix, the Authorization header is being generated without a space between the prefix and the token. This results in malformed headers that fail authentication.

### Reproduction

```js
const header = getBearerAuthHeader('mytoken123', 'CustomBearer');
console.log(header.value);
// Output: "CustomBearermytoken123"
// Expected: "CustomBearer mytoken123"
```

The same issue occurs with the default 'Bearer' prefix:

```js
const header = getBearerAuthHeader('mytoken123');
console.log(header.value);
// Output: "Bearermytoken123"
// Expected: "Bearer mytoken123"
```

### Expected behavior

The Authorization header should include a space between the prefix (either custom or default 'Bearer') and the token value, following the standard HTTP Authorization header format.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
