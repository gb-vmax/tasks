# Bug Report

### Describe the bug

I'm experiencing an issue with client certificate management where duplicate certificates are appearing in the list. After adding or updating certificates, the application shows multiple entries for what should be the same certificate configuration.

### Reproduction

```js
// Create a certificate
const cert1 = await create({
  host: 'example.com',
  cert: '/path/to/cert.pem',
  key: '/path/to/key.pem',
  passphrase: 'secret'
});

// Update the certificate
await update(cert1, {
  passphrase: 'newsecret'
});

// Fetch all certificates
const allCerts = await all();

// Expected: 1 certificate
// Actual: Multiple entries for the same certificate appear
console.log(allCerts.length); // Shows more than expected
```

### Expected behavior

When fetching all certificates, each unique certificate configuration should appear only once in the list. If a certificate is updated, the old version should not persist in the results.

### Additional context

This seems to have started recently. The certificate list keeps growing with what appear to be duplicate or stale entries. It's making it difficult to manage certificates properly since the UI shows multiple identical entries.

---
Repository: /testbed
