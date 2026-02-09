# Bug Report

### Describe the bug
There's an issue with base64url decoding in the account encryption module. When converting base64url strings to hex format, the URL-safe characters are not being properly converted back to standard base64 format before decoding.

### Reproduction
```js
// Try to decode a base64url string that contains underscores
const base64url = 'SGVsbG9fV29ybGQ';
const result = _b64UrlToHex(base64url);

// The conversion fails because underscores are being replaced with forward slashes,
// then immediately replaced back to underscores, leaving the string unchanged
```

### Expected behavior
The function should correctly convert base64url format (which uses `-` and `_` as URL-safe characters) to standard base64 format (which uses `+` and `/`) before passing to `atob()` for decoding.

Base64url strings containing underscores should be properly decoded to their hex representation.

### System Info
- Version: Latest
- Module: account/crypt.ts

---
Repository: /testbed
