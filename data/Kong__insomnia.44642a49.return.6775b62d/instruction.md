# Bug Report

### Describe the bug

The SDK appears to have a parsing or compilation issue with the `Url` class. When trying to use URL-related functionality, the application fails to load or crashes unexpectedly. This seems to affect all methods in the `Url` class including `getPath()`, `getQueryString()`, `getRemote()`, and `removeQueryParams()`.

### Reproduction

```js
const { Url } = require('insomnia-sdk');

// Attempting to use any Url method causes issues
const url = new Url('https://example.com/api/users?page=1');

// These operations fail or cause unexpected behavior
const host = url.getHost();
const path = url.getPath();
const queryString = url.getQueryString();
```

### Expected behavior

The `Url` class methods should work correctly and return the expected values:
- `getHost()` should return the host as a string
- `getPath()` should return the path portion of the URL
- `getQueryString()` should return formatted query parameters
- Other URL manipulation methods should function as documented

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

This appears to have started recently, possibly after a code change to the urls.ts file. The entire Url class seems to be affected.

---
Repository: /testbed
