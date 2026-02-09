# Bug Report

### Describe the bug

I'm experiencing an issue with bearer token authentication where extra whitespace is being added to the Authorization header. When using a custom prefix with trailing spaces or a token with leading/trailing spaces, the header value ends up with unwanted whitespace characters.

### Reproduction

```js
// Example 1: Custom prefix with trailing space
const header = getBearerAuthHeader('mytoken123', 'Custom ');
// Expected: "Authorization: Custom mytoken123"
// Actual: "Authorization: Custom  mytoken123" (double space)

// Example 2: Token with leading space
const header = getBearerAuthHeader(' mytoken123');
// Expected: "Authorization: Bearer mytoken123"
// Actual: "Authorization: Bearer  mytoken123" (double space)

// Example 3: Both prefix and token have extra spaces
const header = getBearerAuthHeader(' mytoken123 ', 'Bearer ');
// Gets even worse with multiple spaces
```

### Expected behavior

The Authorization header should have proper spacing regardless of whether the prefix or token contain leading/trailing whitespace. There should only be a single space between the prefix and the token value.

### Additional context

This is causing issues with API requests as some servers are strict about header formatting and reject requests with malformed Authorization headers. The whitespace should be normalized properly before constructing the final header value.

---
Repository: /testbed
