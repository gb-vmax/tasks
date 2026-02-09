# Bug Report

### Describe the bug

RSA encryption/decryption is failing when trying to encrypt and decrypt data using JWK keys. The encrypted data cannot be decrypted back to the original plaintext.

### Reproduction

```js
const publicKeyJWK = {
  // ... valid JWK public key
};

const privateKeyJWK = {
  // ... corresponding JWK private key
};

const plaintext = "Hello, World!";

// Encrypt the data
const encrypted = encryptRSAWithJWK(publicKeyJWK, plaintext);

// Try to decrypt - this fails
const decrypted = decryptRSAWithJWK(privateKeyJWK, encrypted);

// decrypted !== plaintext
```

### Expected behavior

The decrypted value should match the original plaintext. The encryption and decryption should be symmetric and work correctly with JWK keys.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
