# Bug Report

### Describe the bug

After a recent update, client certificates are no longer working properly. When trying to use existing client certificates, they seem to be lost or become undefined. This is breaking authentication for APIs that require client certificate authentication.

### Reproduction

```js
// Load an existing client certificate
const cert = await loadClientCertificate(certId);

// Certificate becomes undefined unexpectedly
console.log(cert); // undefined
```

The issue appears to happen when loading previously saved client certificates from the database. New certificates work fine initially, but after reloading the app or fetching them again, they become undefined.

### Expected behavior

Client certificates should persist correctly and remain accessible after being saved. Loading an existing certificate should return the certificate object, not undefined.

### System Info
- Insomnia version: latest
- OS: Multiple platforms affected

This is a critical issue as it completely breaks client certificate authentication workflows. Any help would be appreciated!

---
Repository: /testbed
