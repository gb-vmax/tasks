# Bug Report

### Describe the bug

I'm unable to create new client certificates in my workspace. Every time I try to add a client certificate with a valid parent ID, I get an error saying the parentId is missing, which doesn't make sense since I'm clearly providing it.

### Reproduction

```js
// Attempting to create a client certificate with a parentId
const cert = {
  parentId: 'wrk_123456',
  host: 'api.example.com',
  passphrase: 'secret',
  cert: '/path/to/cert.pem',
  key: '/path/to/key.pem'
};

// This throws an error: "New ClientCertificate missing `parentId`"
createClientCertificate(cert);
```

### Expected behavior

The client certificate should be created successfully when a valid `parentId` is provided. The error should only be thrown when the `parentId` is actually missing or undefined.

### Additional context

This seems to have started happening recently. Previously I was able to create client certificates without any issues. The validation logic appears to be backwards - it's rejecting valid certificates that have a parentId instead of rejecting ones that don't.

---
Repository: /testbed
