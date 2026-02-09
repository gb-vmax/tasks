# Bug Report

### Describe the bug

I'm experiencing an issue with account encryption/decryption functionality. When trying to decrypt data after deriving a key from a password and email, the decryption fails even though I'm using the correct credentials.

### Reproduction

```js
const password = 'mySecurePassword123';
const email = 'user@example.com';
const salt = 'randomSalt';

// Derive key for encryption
const key = await deriveKey(password, email, salt);

// Encrypt some data
const encrypted = await encryptData(key, 'sensitive data');

// Try to decrypt with the same credentials
const decryptKey = await deriveKey(password, email, salt);
const decrypted = await decryptData(decryptKey, encrypted);
// Decryption fails or returns garbage
```

### Expected behavior

The key derivation should produce consistent results when given the same password, email, and salt. Decryption should succeed when using the same credentials that were used for encryption.

### Additional context

This seems to have broken recently. I can't log in to my account anymore and all my synced data appears to be inaccessible. The encryption/decryption workflow was working fine before.

---
Repository: /testbed
