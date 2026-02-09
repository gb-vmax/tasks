# Bug Report

### Describe the bug

The URL object seems to be broken after a recent change. When trying to use methods like `getPath()`, `getQueryString()`, or `getRemote()` on a URL instance, I'm getting unexpected errors or the methods are completely missing.

### Reproduction

```js
const url = new Url({
  protocol: 'https:',
  host: ['api', 'example', 'com'],
  port: 443,
  path: ['users', 'profile'],
  query: [
    { key: 'id', value: '123' },
    { key: 'format', value: 'json' }
  ]
});

// These methods don't work anymore
const path = url.getPath();
const queryString = url.getQueryString();
const remote = url.getRemote();
```

### Expected behavior

The URL object should provide working methods to:
- Get the full path with `getPath()`
- Get the query string with `getQueryString()`
- Get the remote host with `getRemote()`
- Remove query parameters with `removeQueryParams()`
- Get path with query string combined with `getPathWithQuery()`

All of these methods appear to be broken or incomplete.

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

---
Repository: /testbed
