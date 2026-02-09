# Bug Report

### Describe the bug

I'm unable to create client certificates anymore. When trying to add a new certificate, I'm getting an error about missing or invalid host even though I'm providing a valid hostname.

### Reproduction

```js
// This used to work but now throws an error
const cert = {
  parentId: 'wrk_123',
  host: 'api.example.com',
  cert: '/path/to/cert.pem',
  key: '/path/to/key.pem'
}

// Error: New ClientCertificate missing or invalid `host`
```

Also noticed that creating a certificate without both cert/key or pfx now fails:

```js
const cert = {
  parentId: 'wrk_123',
  host: 'api.example.com',
  cert: '/path/to/cert.pem'
  // Missing key - this now throws an error
}
```

### Expected behavior

Should be able to create client certificates with valid hostnames like before. The validation seems too strict now - it's rejecting valid configurations that worked in previous versions.

### Additional context

This started happening after the recent update. Not sure if the new validation is intentional but it's breaking existing workflows for certificate management.

---
Repository: /testbed
