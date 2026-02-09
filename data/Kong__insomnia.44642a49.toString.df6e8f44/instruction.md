# Bug Report

### Describe the bug

When calling `toString(true)` on a URL object without a protocol set, the method returns an empty string for the protocol part instead of defaulting to `http://`. This breaks URL generation when you want to force a protocol to be present.

### Reproduction

```js
const url = new Url({
  host: 'example.com',
  path: '/api/test'
});

// Without protocol set, forceProtocol should default to http://
const urlString = url.toString(true);
console.log(urlString);
// Expected: "http://example.com/api/test"
// Actual: "example.com/api/test"
```

### Expected behavior

When `forceProtocol` is `true` and no protocol is set on the URL object, it should default to `http://` to ensure a valid URL is generated.

### System Info

- insomnia-sdk version: latest
- Node version: 18.x

---
Repository: /testbed
