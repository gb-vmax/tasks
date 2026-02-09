# Bug Report

### Describe the bug
Certificate properties are being assigned incorrectly when creating a new Certificate object. The `cert` and `pfx` properties appear to be swapped during initialization.

### Reproduction
```js
const certificate = new Certificate({
  name: 'my-cert',
  matches: ['https://example.com/*'],
  cert: { src: '/path/to/cert.pem' },
  pfx: { src: '/path/to/cert.pfx' }
});

// Expected: certificate.cert should contain the cert path
// Actual: certificate.cert contains the pfx path

console.log(certificate.cert); // Shows pfx data instead of cert data
console.log(certificate.pfx);  // Shows cert data instead of pfx data
```

### Expected behavior
When passing `cert` and `pfx` options to the Certificate constructor, they should be assigned to their corresponding properties. Currently it seems like the values are being swapped - the cert option ends up in the pfx property and vice versa.

### Additional context
This is causing issues when trying to use client certificates for HTTPS requests. The certificate files are being read from the wrong paths, leading to authentication failures.

---
Repository: /testbed
