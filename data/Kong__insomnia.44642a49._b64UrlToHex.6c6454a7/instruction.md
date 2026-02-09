# Bug Report

### Describe the bug
I'm experiencing an issue with base64url encoding/decoding in the account cryptography module. When trying to decode base64url encoded strings, the conversion seems to be happening in the wrong direction, causing the decoded output to be incorrect or potentially throwing errors.

### Reproduction
```js
// Example base64url string (URL-safe base64)
const base64urlString = "SGVsbG8tV29ybGQ_test";

// Attempting to convert to hex
const result = _b64UrlToHex(base64urlString);

// The result is incorrect because the conversion is backwards
```

### Expected behavior
The function should properly convert base64url format to standard base64 format before decoding:
- Replace `-` with `+`
- Replace `_` with `/`

Instead, it appears to be doing the opposite conversion (standard base64 to base64url), which breaks the decoding process.

### System Info
- Insomnia version: latest
- Module: `packages/insomnia/src/account/crypt.ts`

This is affecting any account-related cryptographic operations that rely on base64url encoded data.

---
Repository: /testbed
