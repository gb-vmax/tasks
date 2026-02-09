# Bug Report

### Describe the bug

I'm experiencing an issue with the `Url` class where the methods `getHost()`, `getPath()`, `getPathWithQuery()`, `getQueryString()`, `getRemote()`, and `removeQueryParams()` are no longer accessible. It seems like these methods have been removed or replaced, but I can't figure out what happened.

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

// These methods no longer work
const host = url.getHost(); // Error: getHost is not a function
const path = url.getPath(); // Error: getPath is not a function
const queryString = url.getQueryString(); // Error: getQueryString is not a function
```

### Expected behavior

The `Url` object should expose methods like `getHost()`, `getPath()`, `getQueryString()`, etc. to retrieve formatted parts of the URL. These were working in previous versions.

For example:
- `getHost()` should return `'api.example.com'`
- `getPath()` should return `'/users/profile'`
- `getQueryString()` should return `'id=123&format=json'`

### System Info
- Package: insomnia-sdk
- Node version: 18.x

This seems to have broken after a recent update. Is this intentional or a regression?

---
Repository: /testbed
