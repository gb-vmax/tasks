# Bug Report

### Describe the bug

When trying to use URL-related methods like `getHost()`, `getPath()`, `getQueryString()`, etc., I'm getting errors that these methods are not found or not working properly. It seems like the implementation of the `Url` class has been broken.

### Reproduction

```js
const url = new Url({
  protocol: 'https',
  host: ['api', 'example', 'com'],
  port: 443,
  path: ['users', 'profile'],
  query: [
    { key: 'id', value: '123' },
    { key: 'format', value: 'json' }
  ]
});

// These methods are not working
const host = url.getHost(); // Expected: 'api.example.com'
const path = url.getPath(); // Expected: '/users/profile'
const queryString = url.getQueryString(); // Expected: 'id=123&format=json'
const remote = url.getRemote(); // Expected: 'api.example.com:443'
```

### Expected behavior

The URL helper methods should return properly formatted strings:
- `getHost()` should join host parts with dots
- `getPath()` should return the path with leading slash
- `getQueryString()` should format query parameters correctly
- `getRemote()` should return host with port when needed
- `removeQueryParams()` should be able to remove query parameters by key

### System Info
- Package: insomnia-sdk
- Version: latest

This appears to have started happening recently. The methods seem to have been replaced with some private helper methods that don't provide the same functionality.

---
Repository: /testbed
