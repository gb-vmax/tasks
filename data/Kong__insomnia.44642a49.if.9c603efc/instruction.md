# Bug Report

### Describe the bug

When calling `addHeader()` on a Request object, the method is completely broken and throws a syntax error. It appears that some code got corrupted or improperly merged, making it impossible to add headers to requests.

### Reproduction

```js
const request = new Request({
  url: 'https://example.com'
});

// This throws an error
request.addHeader({
  key: 'Content-Type',
  value: 'application/json'
});
```

Even trying to add a Header instance directly fails:

```js
const header = new Header({
  key: 'Authorization',
  value: 'Bearer token123'
});

request.addHeader(header);
```

### Expected behavior

The `addHeader()` method should successfully add headers to the request without throwing errors. It should accept both Header instances and plain objects with `key` and `value` properties.

### System Info
- insomnia-sdk version: latest
- Node.js version: 18.x

This is blocking our ability to construct requests programmatically. Any help would be appreciated!

---
Repository: /testbed
