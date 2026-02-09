# Bug Report

### Describe the bug

I'm encountering an issue with base64url decoding in the account encryption module. When processing base64url encoded strings, the conversion to hexadecimal appears to be producing incorrect results. The decoded output doesn't match what I'm expecting based on the input.

### Reproduction

```js
// Example base64url string with hyphens
const encoded = 'abc-def_ghi';

// After calling _b64UrlToHex internally
// The result is not correct - hyphens are being replaced twice
// which causes the decoding to fail or produce wrong output
```

The issue seems to occur when the base64url string contains hyphens (`-`). The conversion process isn't handling the character replacement correctly.

### Expected behavior

Base64url strings should be properly converted to standard base64 format (replacing `-` with `+` and `_` with `/`) before decoding, and then correctly converted to hexadecimal representation.

### System Info
- Insomnia version: latest
- OS: Windows/Mac/Linux

Has anyone else run into this? It's affecting my ability to decrypt account data properly.

---
Repository: /testbed
