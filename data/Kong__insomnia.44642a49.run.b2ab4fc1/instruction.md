# Bug Report

### Describe the bug
The hash template tag is rejecting all encoding values even when they are valid. When trying to use the hash function with any encoding option (hex, latin1, or base64), it always throws an error saying the encoding is invalid.

### Reproduction
```js
// Try to hash a value with hex encoding
const result = hashTag.run(context, 'sha256', 'hex', 'test value');
// Error: Invalid encoding hex. Choices are hex, latin1, base64

// Same error occurs with other valid encodings
const result2 = hashTag.run(context, 'sha256', 'base64', 'test value');
// Error: Invalid encoding base64. Choices are hex, latin1, base64

const result3 = hashTag.run(context, 'sha256', 'latin1', 'test value');
// Error: Invalid encoding latin1. Choices are hex, latin1, base64
```

### Expected behavior
The hash function should accept 'hex', 'latin1', and 'base64' as valid encoding options and generate the hash without throwing an error. These are the documented valid choices for the encoding parameter.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
