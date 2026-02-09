# Bug Report

### Describe the bug

When using `applyTrailingSlash` with paths containing query parameters, the function doesn't preserve the query string correctly. The path gets truncated at the query parameter, losing important URL information.

### Reproduction

```js
const path = '/docs/intro?version=1.0';
const options = {
  trailingSlash: true,
  baseUrl: '/'
};

const result = applyTrailingSlash(path, options);
// Expected: '/docs/intro/?version=1.0'
// Actual: '/docs/intro/' (query string is lost)
```

### Steps to reproduce:
1. Call `applyTrailingSlash` with a path that includes query parameters
2. The query string gets dropped from the result
3. Only the pathname portion is returned

This is problematic for pages that rely on query parameters for functionality (like versioning, filtering, etc.). The URL should maintain its query string after applying trailing slash rules.

### Expected behavior

The function should preserve query parameters in the URL while only modifying the pathname portion to add or remove trailing slashes.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
