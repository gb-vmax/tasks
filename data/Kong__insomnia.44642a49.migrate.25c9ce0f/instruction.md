# Bug Report

### Describe the bug

After a recent update, client certificates are being automatically disabled even when they have valid configurations. This is causing authentication failures for requests that rely on client certificates.

### Reproduction

When creating or loading a client certificate with valid PFX or cert/key pair configuration, the certificate gets disabled unexpectedly:

```js
// Case 1: Valid PFX certificate
const cert1 = {
  host: 'api.example.com',
  pfx: '/path/to/certificate.pfx',
  passphrase: 'mypassword',
  disabled: false
}
// After migration, disabled becomes true

// Case 2: Valid cert + key pair
const cert2 = {
  host: 'api.example.com',
  cert: '/path/to/cert.pem',
  key: '/path/to/key.pem',
  disabled: false
}
// After migration, disabled becomes true
```

### Expected behavior

Client certificates with valid configurations (either PFX or cert/key pair) should remain enabled unless explicitly disabled by the user. The migration process should only disable certificates that are actually invalid or misconfigured.

### Additional context

This seems to have started happening after some changes to the certificate migration logic. Previously working certificates are now being disabled automatically, breaking existing API integrations that depend on client certificate authentication.

---
Repository: /testbed
