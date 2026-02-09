# Bug Report

### Describe the bug
Client certificates are not being matched correctly when making requests. It seems like disabled certificates are now being included in the matching process, and the port matching logic has been reversed.

### Reproduction
```js
const clientCertificates = [
  { host: 'example.com:443', disabled: false, cert: 'cert1' },
  { host: 'example.com', disabled: true, cert: 'cert2' }
];

const filtered = filterClientCertificates(
  clientCertificates, 
  'https://example.com:443/api',
  'https:'
);

// Expected: Should return the first certificate only (not disabled)
// Actual: Returns the disabled certificate as well
```

### Expected behavior
- Disabled certificates should never be included in the results
- The function should first try to match with port checking enabled, then fall back to ignoring ports if no match is found
- Only enabled certificates matching the request URL should be returned

### System Info
- Insomnia version: latest
- OS: macOS

This is causing issues with SSL/TLS connections where disabled certificates are being incorrectly applied to requests, or valid certificates are being skipped.

---
Repository: /testbed
