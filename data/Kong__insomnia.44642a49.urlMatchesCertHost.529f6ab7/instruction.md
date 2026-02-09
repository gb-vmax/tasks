# Bug Report

### Describe the bug
Certificate hostname validation is not working correctly when matching URLs against certificate hosts. The validation logic appears to be checking the certificate hostname against itself instead of checking the request URL hostname against the certificate pattern.

### Reproduction
```js
// Setup a certificate with wildcard hostname
const certificateHost = '*.example.com';
const requestUrl = 'https://api.example.com';

// This should return true but may not work correctly
const matches = urlMatchesCertHost(certificateHost, requestUrl);
```

### Expected behavior
When a certificate host pattern (e.g., `*.example.com`) is provided, it should correctly match against the hostname from the request URL (e.g., `api.example.com`). The function should compare the request URL's hostname against the certificate's hostname pattern, not the certificate hostname against itself.

### Additional context
This seems to affect wildcard certificate matching where patterns like `*.domain.com` should match subdomains. The current behavior may cause valid certificate-URL combinations to fail validation.

---
Repository: /testbed
