# Bug Report

### Describe the bug

I'm experiencing issues with password-based encryption/decryption in the account module. When trying to encrypt or decrypt data using a passphrase, the operation fails or produces incorrect results. This seems to be affecting the key derivation process.

### Reproduction

```js
const passphrase = 'my-secure-password';
const salt = generateRandomSalt();

// Attempt to derive key from passphrase
const derivedKey = await _pbkdf2Passphrase(passphrase, salt);

// Try to use the derived key for encryption/decryption
// Results in incorrect key length or decryption failures
```

### Expected behavior

The PBKDF2 key derivation should produce a valid key that can be used for encryption/decryption operations. The derived key should have the correct byte length and work consistently across both the Web Crypto API path and the Forge fallback path.

### Additional context

This might be related to how the key derivation handles the salt parameter or the output key length. The issue appears to affect both browser environments (using Web Crypto API) and non-browser environments (using Forge).

---
Repository: /testbed
