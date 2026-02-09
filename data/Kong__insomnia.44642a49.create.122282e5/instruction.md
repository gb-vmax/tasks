# Bug Report

### Describe the bug

After a recent update, I'm unable to create new client certificates in my workspace. When I try to add a certificate, nothing happens and the certificate doesn't get saved.

### Reproduction

```js
// Try to create a client certificate with a parentId
const cert = await clientCertificate.create({
  parentId: 'wrk_abc123',
  host: 'example.com',
  passphrase: 'test'
});

// The certificate is created but the parentId is missing
console.log(cert.parentId); // undefined
```

### Expected behavior

The client certificate should be created with the `parentId` field properly set so it's associated with the correct workspace. The `parentId` should be preserved in the created certificate object.

### Additional context

This seems to have broken after the latest changes. The certificate gets created but it's not linked to any workspace because the `parentId` is missing from the final object. This makes it impossible to manage certificates per workspace.

---
Repository: /testbed
