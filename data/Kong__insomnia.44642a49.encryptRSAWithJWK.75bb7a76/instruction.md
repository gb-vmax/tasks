# Bug Report

### Describe the bug
Encrypted data cannot be decrypted after encryption using RSA with JWK. The encryption process appears to complete successfully, but when attempting to decrypt the encrypted blob, it fails or produces garbled output.

### Reproduction
```js
const publicKeyJWK = {
  n: 'some-base64-url-encoded-modulus',
  e: 'AQAB'
};

const privateJWK = {
  // corresponding private key
};

const plaintext = 'Hello, World!';

// Encrypt the data
const encrypted = encryptRSAWithJWK(publicKeyJWK, plaintext);

// Try to decrypt - this fails
const decrypted = decryptRSAWithJWK(privateJWK, encrypted);

// Expected: 'Hello, World!'
// Actual: Decryption error or garbled output
```

### Expected behavior
The encrypted data should be decryptable back to the original plaintext using the corresponding private key. The encryption and decryption should be symmetric and work correctly together.

### Additional context
This seems to have started happening recently. Previously encrypted data might also be affected if the encryption format has changed.

---
Repository: /testbed
