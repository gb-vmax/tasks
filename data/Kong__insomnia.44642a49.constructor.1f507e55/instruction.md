# Bug Report

### Describe the bug
After a recent update, HTTP headers are being normalized/transformed in an unexpected way. Header keys are being modified automatically, which is breaking our API requests that require specific header casing.

### Reproduction
```js
const header = new Header({
  key: 'content-type',
  value: 'application/json'
});

// The header key is being automatically transformed
console.log(header.key); // Expected: 'content-type', but getting something different
```

We're also seeing issues when creating headers from strings:

```js
const header = new Header('x-custom-header: value');
// The key is being transformed instead of preserved as-is
```

### Expected behavior
Header keys should be preserved exactly as provided by the user. Some APIs are case-sensitive and require specific casing for custom headers (e.g., `X-API-Key`, `content-type`, etc.). The SDK should not automatically normalize or transform header keys.

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

This is causing our integration tests to fail because the API we're calling rejects requests with incorrectly cased headers. Would appreciate any guidance on how to work around this or if there's a way to disable the automatic transformation.

---
Repository: /testbed
