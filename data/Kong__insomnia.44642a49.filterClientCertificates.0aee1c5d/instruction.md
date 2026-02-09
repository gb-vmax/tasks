# Bug Report

### Describe the bug

Client certificates are not being matched correctly when making requests. When I have a certificate configured for a specific host, the request fails to use it even though the certificate is enabled and should match the request URL.

### Reproduction

```js
const clientCertificates = [
  {
    host: 'api.example.com',
    disabled: false,
    cert: '/path/to/cert.pem',
    key: '/path/to/key.pem'
  }
];

const requestUrl = 'https://api.example.com/endpoint';

// Certificate should be selected but isn't being used
const filtered = filterClientCertificates(clientCertificates, requestUrl, 'https:');
// Returns empty array instead of the matching certificate
```

### Expected behavior

When a client certificate is configured for a host and is not disabled, it should be selected and used for requests to that host. The certificate matching should work for both exact host matches and when ignoring port numbers.

### Additional context

This seems to have broken recently - requests that previously worked with client certificates are now failing with SSL/TLS errors because no certificate is being provided. The certificate configuration itself hasn't changed, so something in the certificate filtering logic appears to be the issue.

---
Repository: /testbed
