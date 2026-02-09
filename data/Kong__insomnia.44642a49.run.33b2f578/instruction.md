# Bug Report

### Describe the bug

The base64 decode template tag is not working correctly when decoding standard base64 strings. It appears to be treating all base64 inputs as if they were URL-safe encoded, which causes decoding failures for regular base64 strings.

### Reproduction

```js
// Using the base64 template tag with decode action
const encoded = 'SGVsbG8gV29ybGQ=';  // Standard base64 for "Hello World"

// Try to decode with kind='normal'
// Expected: "Hello World"
// Actual: Decoding fails or returns incorrect output
```

The issue occurs when trying to decode a standard base64 string (with `+`, `/`, and `=` padding characters). The decoder seems to be applying URL-safe normalization even when `kind='normal'` is specified.

### Expected behavior

When decoding with `kind='normal'`, the template tag should handle standard base64 strings with `+`, `/`, and `=` characters correctly without applying URL-safe transformations.

When decoding with `kind='url'`, it should convert URL-safe base64 (using `-` and `_`) back to standard format before decoding.

### Additional context

This seems to have broken recently. Standard base64 strings should be decoded as-is when using the normal kind, but they're being processed through URL-safe normalization which corrupts the input.

---
Repository: /testbed
