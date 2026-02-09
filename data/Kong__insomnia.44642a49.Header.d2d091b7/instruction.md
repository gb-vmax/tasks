# Bug Report

### Describe the bug

After a recent update, HTTP headers are being automatically modified in unexpected ways. Header keys are being converted to Title-Case format and header values are having newlines replaced with spaces. This is breaking our API calls that require specific header formatting.

### Reproduction

```js
const header = new Header({
  key: 'x-custom-header',
  value: 'some\nvalue'
});

console.log(header.key);   // Expected: 'x-custom-header', Got: 'X-Custom-Header'
console.log(header.value); // Expected: 'some\nvalue', Got: 'some value'
```

Also happens when parsing header strings:

```js
const header = new Header('content-type: application/json');
console.log(header.key); // Expected: 'content-type', Got: 'Content-Type'
```

### Expected behavior

Headers should preserve the exact casing and formatting that was provided. Some APIs are case-sensitive for custom headers (e.g., `x-custom-header` vs `X-Custom-Header`), and automatically normalizing them breaks compatibility.

The value sanitization is also problematic - while newlines in header values might not be standard HTTP, the library shouldn't silently modify them without the user's knowledge.

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

---
Repository: /testbed
