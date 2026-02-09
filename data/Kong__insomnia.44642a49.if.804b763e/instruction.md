# Bug Report

### Describe the bug

I'm experiencing an issue with client certificate handling in the Insomnia SDK. When trying to merge client certificates, the function appears to be incomplete or corrupted. The code seems to have duplicate function definitions and the main `mergeClientCertificates` function is cut off mid-implementation.

### Reproduction

```js
const originalCerts = [
  {
    host: 'api.example.com',
    key: 'key-data',
    cert: 'cert-data'
  }
];

const request = {
  url: {
    getHost: () => 'api.example.com'
  },
  certificate: {
    key: 'new-key',
    cert: 'new-cert',
    matches: ['*.example.com']
  }
};

// Attempting to merge certificates
const result = mergeClientCertificates(originalCerts, request);
// Function doesn't complete properly
```

### Expected behavior

The `mergeClientCertificates` function should properly merge the original client certificates with the updated request certificate configuration. It should handle certificate pattern matching and return a complete merged certificate array.

### Additional context

Looking at the code, there seems to be:
1. A duplicate/incomplete function definition
2. Helper functions (`findOverlappingCertificates`, `certificateMatchesPattern`) that are defined but the main function doesn't seem to use them properly
3. The main function body appears to be truncated or malformed

This is blocking certificate-based authentication workflows in pre-request scripts.

---
Repository: /testbed
