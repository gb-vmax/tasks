# Bug Report

### Describe the bug
When updating a certificate using the `update()` method, the `matches` property is not being set correctly. If I provide a list of URL match patterns, they don't get applied to the certificate - instead the matches array ends up empty.

Also noticed that the `passphrase` property seems to be getting the wrong value after calling `update()`.

### Reproduction
```js
const cert = new Certificate({
  name: 'My Cert',
  matches: ['https://example.com/*'],
  key: { src: 'key.pem' },
  cert: { src: 'cert.pem' },
  passphrase: 'secret123',
  pfx: { src: 'cert.pfx' }
});

// Update the certificate
cert.update({
  name: 'Updated Cert',
  matches: ['https://api.example.com/*', 'https://test.example.com/*'],
  key: { src: 'new-key.pem' },
  cert: { src: 'new-cert.pem' },
  passphrase: 'newsecret456',
  pfx: { src: 'new-cert.pfx' }
});

// Expected: cert.matches should contain the two new patterns
// Actual: cert.matches is empty

// Expected: cert.passphrase should be 'newsecret456'
// Actual: cert.passphrase has the pfx value instead
```

### Expected behavior
- The `matches` array should be populated with the provided URL patterns
- The `passphrase` should be set to the value from `options.passphrase`, not from `options.pfx`

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

---
Repository: /testbed
