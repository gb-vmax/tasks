# Bug Report

### Describe the bug

I'm experiencing an issue with header handling after a recent update. When creating headers with certain values, I'm getting unexpected validation errors that weren't happening before. Specifically, headers like `Content-Type` are now throwing errors with values that should be valid.

### Reproduction

```js
const header = new Header({
  key: 'Content-Type',
  value: 'application/json'
});

// This now throws an error but shouldn't
const header2 = new Header({
  key: 'Authorization',
  value: 'Bearer token123'
});
```

Also noticed that some header values are being normalized/modified when they shouldn't be:

```js
const header = new Header({
  key: 'Cache-Control',
  value: 'no-cache,  must-revalidate'
});

console.log(header.value); // Gets normalized unexpectedly
```

### Expected behavior

Headers should be created without throwing validation errors for valid values. The header values should remain as provided unless there's a specific reason to normalize them.

### Additional context

This seems to have started after updating to the latest version. The validation is too strict and is rejecting perfectly valid HTTP header values. Not sure if this is a regression or if there's new behavior I'm not aware of.

---
Repository: /testbed
