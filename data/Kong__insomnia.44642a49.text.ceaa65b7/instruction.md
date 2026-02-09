# Bug Report

### Describe the bug
When calling `response.text()` on a response object that has a `stream` property but no `body` property, the method throws an error trying to call `toString()` on undefined. The code attempts to return `this.body.toString()` as a fallback even when `this.body` doesn't exist.

### Reproduction
```js
const response = new Response({
  stream: someBufferOrArrayBuffer,
  // no body property set
});

// This throws an error
const text = response.text();
// TypeError: Cannot read property 'toString' of undefined
```

### Expected behavior
The method should handle cases where `body` is undefined and fall back to decoding the `stream` property if available, or return an empty string/handle gracefully.

### System Info
- Package: insomnia-sdk
- Version: latest

This seems to be an issue with the fallback logic at the end of the `text()` method. When neither `this.body` nor `this.stream` contain data (or when body is undefined), it still tries to call `toString()` on the undefined `body` property.

---
Repository: /testbed
