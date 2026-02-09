# Bug Report

### Describe the bug

After a recent update, HTTP header keys are being automatically normalized to title case (e.g., `content-type` becomes `Content-Type`). This is causing issues when working with headers that need to preserve their original casing, particularly for custom headers or APIs that are case-sensitive.

### Reproduction

```js
const header = new Header({
  key: 'x-custom-header',
  value: 'test-value'
});

console.log(header.key); // Expected: 'x-custom-header', Actual: 'X-Custom-Header'
```

Another example:
```js
const header = new Header('content-type: application/json');
console.log(header.key); // Expected: 'content-type', Actual: 'Content-Type'
```

### Expected behavior

Header keys should preserve their original casing as provided by the user. While HTTP headers are case-insensitive according to the spec, some APIs and tools may expect specific casing, and the SDK shouldn't enforce a particular style.

### Additional context

This seems to affect:
- Headers created from objects
- Headers parsed from strings
- Headers updated via the `update()` method

The normalization is being applied automatically without any way to opt out or preserve the original casing.

---
Repository: /testbed
