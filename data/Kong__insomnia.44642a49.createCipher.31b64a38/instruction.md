# Bug Report

### Describe the bug

I'm encountering an issue with cipher operations where the encrypted output appears to be corrupted or incorrectly transformed. When encrypting data, the resulting ciphertext doesn't decrypt back to the original plaintext, suggesting the encryption process is producing incorrect output.

### Reproduction

```js
const forge = require('node-forge');

// Create cipher and encrypt some data
const cipher = forge.cipher.createCipher();
const buffer = forge.util.createBuffer('test data');

cipher.start({ iv: 'initialization_vector' });
cipher.update(buffer);
cipher.finish();

const encrypted = cipher.output;

// The encrypted output doesn't match expected format
// When trying to decrypt, original data is not recovered
```

### Expected behavior

The cipher should properly encrypt data in a way that can be decrypted back to the original plaintext. The output should be a valid encrypted representation of the input data.

### System Info
- Package: insomnia
- Node version: Latest

---
Repository: /testbed
