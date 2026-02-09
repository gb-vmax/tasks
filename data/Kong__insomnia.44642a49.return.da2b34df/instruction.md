# Bug Report

### Describe the bug
The URL object's `getPath()` method appears to be broken and returns incomplete/corrupted output. When trying to access path information from a URL object, the method doesn't return the full path string as expected.

### Reproduction
```js
const url = new Url({
  protocol: 'https',
  host: ['example', 'com'],
  path: ['api', 'users', '123']
});

// This should return '/api/users/123' but returns something incomplete
const path = url.getPath();
console.log(path); // Expected: '/api/users/123', Actual: incomplete/truncated
```

### Expected behavior
The `getPath()` method should return the complete path string with proper formatting. When `unresolved` is false (default), it should return the resolved path. When `unresolved` is true, it should return the unresolved path.

Additionally, other methods that depend on `getPath()` like `getPathWithQuery()` are also affected and not working properly.

### System Info
- Package: insomnia-sdk
- Affected methods: `getPath()`, `getPathWithQuery()`, `getQueryString()`, `getRemote()`, `removeQueryParams()`

---
Repository: /testbed
