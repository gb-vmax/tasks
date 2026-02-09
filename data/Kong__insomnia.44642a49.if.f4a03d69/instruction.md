# Bug Report

### Describe the bug

When setting client certificates in pre-request scripts, the certificate configuration is not being applied correctly. It looks like there's an issue with how certificates are being merged/processed - the code appears to have been refactored but the logic flow got broken.

### Reproduction

```js
// In a pre-request script
pm.request.certificate = {
  cert: '/path/to/cert.pem',
  key: '/path/to/key.pem',
  passphrase: 'my-passphrase'
}
```

After setting the certificate this way, the request doesn't use the specified certificate. The original certificate configuration (if any) seems to be used instead, or no certificate is applied at all.

### Expected behavior

The request should use the certificate configuration specified in the pre-request script. When `pm.request.certificate` is set, those certificate details should be applied to the outgoing request.

### Additional context

This might have been introduced in a recent refactor - it looks like the certificate merging logic may have been partially rewritten but not completed properly. The condition checks seem incomplete or disconnected from the actual certificate update logic.

---
Repository: /testbed
