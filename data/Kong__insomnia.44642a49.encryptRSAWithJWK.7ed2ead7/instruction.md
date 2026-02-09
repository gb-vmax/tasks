# Bug Report

### Describe the bug

I'm encountering an issue with RSA encryption when using public keys. The encryption function appears to be rejecting valid public keys that have the correct key operations.

### Reproduction

```js
const publicKeyJWK = {
  alg: 'RSA-OAEP-256',
  kty: 'RSA',
  key_ops: ['encrypt'],
  n: '...',
  e: 'AQAB'
};

const plaintext = 'Hello World';

// This throws an error even though the key has 'encrypt' operation
encryptRSAWithJWK(publicKeyJWK, plaintext);
```

The error message says: `Public key does not have "encrypt" op`

But as you can see, the public key clearly has `'encrypt'` in the `key_ops` array. This should work for encrypting data with a public key.

### Expected behavior

The function should accept public keys with the `'encrypt'` operation and successfully encrypt the plaintext. Public keys are meant for encryption, so checking for the `'encrypt'` operation makes sense.

### Additional context

This seems to have broken recently. I'm using this for encrypting sensitive data before sending it to the server, and now all my encryption calls are failing with this validation error.

---
Repository: /testbed
