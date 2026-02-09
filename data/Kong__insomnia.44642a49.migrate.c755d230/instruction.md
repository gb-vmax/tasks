# Bug Report

### Describe the bug

After a recent update, client certificates are being migrated incorrectly. When loading existing client certificates with version < 2, the `version` field is being removed from the certificate object. This causes issues when the certificate is saved again, as it gets treated as a new certificate without version information.

### Reproduction

```js
const clientCert = {
  type: 'ClientCertificate',
  version: 1,
  host: 'example.com',
  passphrase: 'test123',
  cert: '/path/to/cert.pem',
  key: '/path/to/key.pem'
};

// After migration, the version field is deleted
const migrated = migrate(clientCert);
// migrated.version is now undefined instead of being updated to 2
```

### Expected behavior

The migration should update the `version` field to 2 rather than deleting it entirely. The certificate should maintain its version information after migration so subsequent saves work correctly.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
