# Bug Report

### Describe the bug

RSA encryption is failing when trying to encrypt data with a public key. The encrypted output appears to be corrupted or in the wrong format, and attempting to decrypt the data results in errors or garbled output.

### Reproduction

```js
const publicKeyJWK = {
  n: 'xGOr_H7A...',  // base64url encoded modulus
  e: 'AQAB'
};

const plaintext = 'sensitive data with special chars: @#$%';
const encrypted = encryptRSAWithJWK(publicKeyJWK, plaintext);

// Attempting to decrypt with the corresponding private key fails
// The encrypted blob format seems incorrect
```

### Expected behavior

The encryption function should properly encode the plaintext before encryption and return the encrypted data in a format that can be successfully decrypted using the corresponding private key. Special characters in the plaintext should be handled correctly.

### System Info

- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
