# Bug Report

### Describe the bug

When updating a certificate with a passphrase and pfx file, the values appear to be swapped. After calling the `update()` method on a certificate object, the passphrase is set to the pfx value and the pfx is set to the passphrase value.

### Reproduction

```js
const cert = new Certificate({
  name: 'my-cert',
  passphrase: 'my-secret-passphrase',
  pfx: '/path/to/certificate.pfx'
});

cert.update({
  name: 'my-cert',
  passphrase: 'new-passphrase',
  pfx: '/path/to/new-cert.pfx'
});

// Expected: cert.passphrase === 'new-passphrase'
// Actual: cert.passphrase === '/path/to/new-cert.pfx'

// Expected: cert.pfx === '/path/to/new-cert.pfx'
// Actual: cert.pfx === 'new-passphrase'
```

### Expected behavior

The passphrase and pfx properties should be set to their corresponding values from the options object, not swapped with each other.

### System Info

- insomnia-sdk version: latest
- Node version: 18.x

---
Repository: /testbed
