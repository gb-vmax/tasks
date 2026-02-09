# Bug Report

### Describe the bug

When calling `toString()` on a URL object without a protocol and with `forceProtocol` set to `true`, the method no longer adds a default protocol. Previously it would default to `http://` but now it just returns an empty string for the protocol part.

### Reproduction

```js
const url = new Url({
  host: 'example.com',
  path: '/api/test'
  // no protocol specified
});

const urlString = url.toString(true);
console.log(urlString);
// Expected: "http://example.com/api/test"
// Actual: "example.com/api/test"
```

### Expected behavior

When `forceProtocol` is `true` and no protocol is set on the URL object, it should default to `http://` as the protocol prefix.

### Additional context

This seems to have changed recently. The behavior was working correctly before where calling `toString(true)` would ensure a protocol was always present in the output string.

---
Repository: /testbed
