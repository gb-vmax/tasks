# Bug Report

### Describe the bug

After updating, workspace client certificates are not being migrated properly. The first certificate in the list is being skipped during migration, and only certificates starting from the second position are being processed.

### Reproduction

1. Create a workspace with multiple client certificates
2. Trigger the certificate migration process
3. Observe that the first certificate is missing after migration

Example setup:
```js
const workspace = {
  _id: 'wrk_123',
  certificates: [
    { host: 'api.example.com', cert: '...' },
    { host: 'api2.example.com', cert: '...' },
    { host: 'api3.example.com', cert: '...' }
  ]
}
```

After migration, only the certificates for `api2.example.com` and `api3.example.com` are present. The first certificate for `api.example.com` is not migrated.

### Expected behavior

All certificates should be migrated, including the first one in the array. The migration should iterate through all certificates starting from index 0.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
