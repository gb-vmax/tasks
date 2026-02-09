# Bug Report

### Describe the bug

When updating client certificates in pre-request scripts, duplicate certificates are being added instead of replacing existing ones when the host and port match. This causes the certificate list to grow indefinitely with duplicate entries.

### Reproduction

```js
// Initial client certificates
const originalCerts = [
  {
    host: 'example.com',
    port: 443,
    certificate: 'cert1',
    key: 'key1'
  }
];

// Update with new certificate for same host/port
const updatedReq = {
  host: 'example.com',
  port: 443,
  certificate: {
    cert: 'cert2',
    key: 'key2'
  }
};

// After merging, both certificates exist instead of replacing the old one
// Result: [
//   { host: 'example.com', port: 443, certificate: 'cert1', key: 'key1' },
//   { host: 'example.com', port: 443, certificate: 'cert2', key: 'key2' }
// ]
```

### Expected behavior

When a certificate is updated for an existing host/port combination, it should replace the old certificate entry, not add a duplicate. The result should only contain one certificate per host/port pair.

### System Info
- Insomnia SDK version: latest
- Platform: All

---
Repository: /testbed
