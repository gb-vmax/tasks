# Bug Report

### Describe the bug

The hash template tag is producing incorrect hash values when using non-UTF8 characters or binary data. The hash output doesn't match what's expected when hashing strings with special encodings.

### Reproduction

```js
// Try hashing a string with the hash template tag
// Using algorithm: sha256, encoding: base64
const input = 'test string';

// The hash generated is different from what standard crypto libraries produce
// when hashing the same input with base64 encoding
```

### Expected behavior

The hash template tag should produce the same hash output as standard crypto libraries when given the same input, algorithm, and encoding parameters. Currently, it seems like the encoding parameter might not be applied correctly during the hashing process.

### System Info
- Insomnia version: latest
- OS: Multiple platforms affected

---
Repository: /testbed
