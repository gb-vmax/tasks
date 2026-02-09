# Bug Report

### Describe the bug

The `Url` class is broken after a recent change. Methods like `getHost()`, `getPath()`, `getQueryString()`, and `removeQueryParams()` are no longer accessible or working. It looks like the code got corrupted or accidentally replaced during a refactor.

### Reproduction

```js
const url = new Url({
  protocol: 'https:',
  host: ['api', 'example', 'com'],
  path: ['users', '123'],
  query: [
    { key: 'page', value: '1' },
    { key: 'limit', value: '10' }
  ]
});

// These methods should work but don't
const host = url.getHost(); // Expected: 'api.example.com'
const path = url.getPath(); // Expected: '/users/123'
const queryString = url.getQueryString(); // Expected: 'page=1&limit=10'

// This should also work
url.removeQueryParams('page');
```

### Expected behavior

All the URL helper methods should be available and functional. The `getHost()` method should join host parts with dots, `getPath()` should join path segments with slashes, `getQueryString()` should format query parameters, and `removeQueryParams()` should remove specified parameters from the URL.

### System Info
- Package: insomnia-sdk
- Version: latest

This is blocking our URL manipulation functionality. Any help would be appreciated!

---
Repository: /testbed
