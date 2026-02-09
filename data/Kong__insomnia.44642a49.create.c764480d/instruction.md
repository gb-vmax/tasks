# Bug Report

### Describe the bug

When creating a new client certificate with additional properties in the patch object, all properties except `parentId` are being ignored. The certificate is created with only the `parentId` field, losing any other data that was passed in.

### Reproduction

```js
const cert = await clientCertificate.create({
  parentId: 'workspace_123',
  host: 'api.example.com',
  passphrase: 'secret',
  cert: '/path/to/cert.pem',
  key: '/path/to/key.pem'
});

// Expected: cert contains all the properties
// Actual: cert only has parentId, all other fields are missing
console.log(cert.host); // undefined
console.log(cert.passphrase); // undefined
```

### Expected behavior

The `create` function should accept and persist all properties provided in the patch object, not just `parentId`. When I pass in certificate details like host, passphrase, cert path, and key path, they should be included in the created certificate document.

### System Info
- Version: Latest from main branch

---
Repository: /testbed
