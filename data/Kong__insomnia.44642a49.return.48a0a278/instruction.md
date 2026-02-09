# Bug Report

### Describe the bug

I'm experiencing an issue with URL handling where the code seems to be incomplete or broken. When trying to use URL-related methods like `getHost()`, `getPath()`, `getQueryString()`, etc., they don't seem to work as expected or are missing entirely.

### Reproduction

```js
const url = new Url({
  protocol: 'https:',
  host: ['api', 'example', 'com'],
  path: ['v1', 'users'],
  query: [
    { key: 'id', value: '123' },
    { key: 'format', value: 'json' }
  ]
});

// These methods don't work properly
const host = url.getHost(); // Expected: 'api.example.com'
const path = url.getPath(); // Expected: '/v1/users'
const queryString = url.getQueryString(); // Expected: 'id=123&format=json'
```

### Expected behavior

- `getHost()` should return the joined host parts (e.g., 'api.example.com')
- `getPath()` should return the formatted path with leading slash
- `getQueryString()` should return the properly formatted query parameters
- `getRemote()` should return the host with optional port
- `removeQueryParams()` should properly filter out specified query parameters

These methods were working in the previous version but now seem to be broken or missing.

### System Info
- Package: insomnia-sdk
- Version: latest

---
Repository: /testbed
