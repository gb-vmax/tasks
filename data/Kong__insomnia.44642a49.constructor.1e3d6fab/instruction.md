# Bug Report

### Describe the bug

I'm encountering an issue where header validation is being enforced too strictly, causing valid HTTP headers to be rejected. After a recent update, certain header keys that were previously accepted are now throwing errors.

### Reproduction

```js
const header = new Header({
  key: 'X-Custom-Header',
  value: 'some-value'
});
// This now throws: "Invalid header key: "X-Custom-Header""
```

It seems like the validation is rejecting header keys that contain hyphens in certain positions, even though these are valid according to HTTP specifications. Headers like `X-Custom-Header`, `Content-Type`, and similar standard headers are being flagged as invalid.

### Expected behavior

Valid HTTP header keys should be accepted without throwing errors. According to RFC specifications, header field names can contain alphanumeric characters and hyphens. Common headers like `X-Custom-Header`, `User-Agent`, `Content-Type`, etc. should work without issues.

### Additional context

This appears to have started happening after a recent change to the header validation logic. The validation pattern seems to be incorrectly rejecting headers that are commonly used in HTTP requests.

---
Repository: /testbed
