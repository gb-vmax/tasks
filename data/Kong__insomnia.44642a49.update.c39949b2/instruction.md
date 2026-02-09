# Bug Report

### Describe the bug
Certificate update is not working properly - the `passphrase` and `pfx` values are being swapped when calling the `update()` method on a Certificate object. When I set a passphrase, it ends up in the pfx field instead, and vice versa.

### Reproduction
```js
const cert = new Certificate({
  name: 'my-cert',
  passphrase: 'my-secret-passphrase',
  pfx: 'my-pfx-data'
});

cert.update({
  name: 'my-cert',
  passphrase: 'updated-passphrase',
  pfx: 'updated-pfx-data'
});

// Expected: cert.passphrase = 'updated-passphrase'
// Actual: cert.passphrase = 'updated-pfx-data'

// Expected: cert.pfx = 'updated-pfx-data'  
// Actual: cert.pfx = 'updated-passphrase'
```

### Expected behavior
When updating a certificate, the `passphrase` field should contain the passphrase value and the `pfx` field should contain the pfx value. They shouldn't be swapped.

This is causing issues when trying to update certificate configurations - the wrong values end up in the wrong fields.

---
Repository: /testbed
