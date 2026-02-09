# Bug Report

### Describe the bug

I'm encountering an issue with header keys after a recent update. When creating headers with certain key formats, I'm getting validation errors that weren't happening before. Specifically, headers with underscores or other special characters that used to work are now being rejected.

### Reproduction

```js
// This now throws an error
const header = new Header({
  key: 'x_custom_header',
  value: 'test'
});

// Also fails with other special characters
const header2 = new Header({
  key: 'x.custom.header',
  value: 'test'
});
```

The error message says something like "Header keys must contain only letters, digits, and hyphens" but underscores and dots are valid in HTTP headers according to the spec.

### Expected behavior

Headers with underscores, dots, and other valid special characters should be accepted without throwing errors. The validation seems too strict now.

### Additional context

This is breaking existing code that was working fine before. Many APIs use custom headers with underscores (like `x_request_id`, `x_correlation_id`, etc.) and these are all failing now.

---
Repository: /testbed
