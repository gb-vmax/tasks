# Bug Report

### Describe the bug

I'm encountering an issue with base64url decoding in the account cryptography module. When trying to decode base64url encoded strings, the conversion to hex produces incorrect results. This appears to be affecting authentication and encryption operations.

### Reproduction

```js
// Attempting to decode a base64url string
const base64url = 'SGVsbG8tV29ybGQ';  // Contains '-' character
const result = _b64UrlToHex(base64url);

// The result is incorrect because the character replacement is wrong
// Expected: proper hex conversion after replacing '-' with '+'
// Actual: incorrect hex output due to reversed replacement logic
```

### Expected behavior

Base64url strings should be correctly converted to standard base64 format before decoding to hex. The standard base64url format uses `-` and `_` characters which need to be replaced with `+` and `/` respectively before decoding.

### System Info
- Insomnia version: latest
- OS: macOS

This is breaking encrypted sync functionality for me. Any help would be appreciated!

---
Repository: /testbed
