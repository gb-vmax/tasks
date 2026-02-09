# Bug Report

### Describe the bug

When calling `toString()` on a URL object with `forceProtocol` set to `true`, the protocol string is missing the `//` separator. This results in malformed URLs like `http://example.com` being rendered as `httpexample.com`.

### Reproduction

```js
const url = new Url({
  protocol: 'https',
  host: 'example.com',
  path: '/api/test'
});

// This produces a malformed URL
const urlString = url.toString(true);
console.log(urlString);
// Expected: https://example.com/api/test
// Actual: httpsexample.com/api/test
```

The issue also affects URLs without a protocol specified:

```js
const url = new Url({
  host: 'example.com',
  path: '/test'
});

const urlString = url.toString(true);
console.log(urlString);
// Expected: http://example.com/test
// Actual: http://example.com/test (this one works correctly)
```

### Expected behavior

When `forceProtocol` is true and a protocol exists, the URL should include the `//` separator after the protocol (e.g., `https://`). The generated URL string should be valid and parseable.

### Additional context

This appears to affect URL generation when protocols are present. URLs without protocols seem to work fine when forcing the default `http://` protocol.

---
Repository: /testbed
