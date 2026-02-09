# Bug Report

### Describe the bug
The hash template tag is rejecting all valid encoding values (hex, latin1, base64) and throwing an error instead of processing the hash. When trying to use any of the supported encodings, I get an error message saying the encoding is invalid.

### Reproduction
```js
// Try to hash a value with hex encoding
const result = hashTag.run(context, 'sha256', 'hex', 'test value');
// Error: Invalid encoding hex. Choices are hex, latin1, base64

// Same issue with base64
const result = hashTag.run(context, 'sha256', 'base64', 'test value');
// Error: Invalid encoding base64. Choices are hex, latin1, base64
```

### Expected behavior
The hash function should accept 'hex', 'latin1', and 'base64' as valid encoding options and return the hashed value without throwing an error. These are the documented supported encodings for the hash template tag.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
