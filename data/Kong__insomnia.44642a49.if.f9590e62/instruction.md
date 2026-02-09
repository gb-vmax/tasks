# Bug Report

### Describe the bug

I'm experiencing an issue with client certificate management in pre-request scripts. When trying to add a new certificate that doesn't already exist in the collection, the certificate is not being added to the list properly.

### Reproduction

```js
// In a pre-request script
const newCert = {
  id: 'new-cert-123',
  key: 'key-content',
  cert: 'cert-content'
};

pm.request.certificate = newCert;
```

After executing the script, the new certificate should be added to the existing certificates, but it appears to not be included when the request is sent.

### Expected behavior

When setting a certificate object with a new ID (one that doesn't exist in the original certificates list), it should be appended to the certificates array so the request uses it.

### System Info

- Insomnia SDK version: latest
- Platform: macOS

---
Repository: /testbed
