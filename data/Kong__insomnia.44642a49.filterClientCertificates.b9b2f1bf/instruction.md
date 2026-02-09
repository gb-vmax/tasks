# Bug Report

### Describe the bug
Client certificates are not being matched correctly for requests. It seems like only disabled certificates are being considered instead of enabled ones, which prevents any valid certificates from being used for secure connections.

### Reproduction
```js
const clientCertificates = [
  { host: 'example.com', disabled: false, cert: '...' },
  { host: 'test.com', disabled: true, cert: '...' }
];

const result = filterClientCertificates(
  clientCertificates, 
  'https://example.com/api',
  'https:'
);

// Expected: Should return the enabled certificate for example.com
// Actual: Returns empty array or wrong certificate
```

### Steps to reproduce
1. Set up a client certificate with `disabled: false`
2. Make a request to a URL that matches the certificate host
3. The certificate is not applied to the request

### Expected behavior
Enabled certificates (where `disabled: false`) should be matched and used for requests to their corresponding hosts. Disabled certificates should be ignored.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
