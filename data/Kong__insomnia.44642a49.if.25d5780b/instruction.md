# Bug Report

### Describe the bug

When updating client certificates through the pre-request script, the certificate list is not being updated correctly. Even when a new certificate is added or an existing one is modified, the original certificate list is returned unchanged.

### Reproduction

```js
const originalCerts = [
  { id: 'cert1', key: 'key1', cert: 'cert1' }
];

const updatedRequest = {
  certificate: { id: 'cert2', key: 'key2', cert: 'cert2' }
};

// Expected: originalCerts should now include cert2
// Actual: originalCerts remains unchanged with only cert1
const result = mergeClientCertificates(originalCerts, updatedRequest);
```

### Expected behavior

When a certificate is specified in the pre-request script:
- If it has a new ID, it should be added to the certificate list
- If it matches an existing ID, it should replace that certificate
- The updated list should be returned

Currently, the function returns the original certificate list without any modifications, even when valid certificates are provided.

### System Info
- insomnia-sdk version: latest
- Platform: All

---
Repository: /testbed
