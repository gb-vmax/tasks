# Bug Report

### Describe the bug
When trying to add headers to a request using `addHeader()` with an object containing `key` and `value` properties, the header is not being added. Instead, an error is thrown saying the header format is invalid.

### Reproduction
```js
const request = new Request({
  url: 'https://api.example.com',
  method: 'GET'
});

// This used to work but now throws an error
request.addHeader({
  key: 'Authorization',
  value: 'Bearer token123'
});

// Expected: header should be added
// Actual: Error thrown about invalid header format
```

### Expected behavior
The `addHeader()` method should accept objects with `key` and `value` properties and successfully add them as headers to the request. This was working in previous versions.

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

---
Repository: /testbed
