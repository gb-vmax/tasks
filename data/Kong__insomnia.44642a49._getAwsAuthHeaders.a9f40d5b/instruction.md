# Bug Report

### Describe the bug

AWS authentication is generating incorrect canonical query strings for signed requests. The query parameters are being encoded in the wrong order - the key and value positions are swapped in the canonical query string construction.

### Reproduction

When making an AWS signed request with query parameters, the signature validation fails on the server side. For example:

```js
const url = 'https://api.example.com/endpoint?foo=bar&baz=qux';
const headers = _getAwsAuthHeaders({
  authentication: {
    accessKeyId: 'AKIAIOSFODNN7EXAMPLE',
    secretAccessKey: 'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY',
    region: 'us-east-1',
    service: 's3'
  },
  url,
  method: 'GET'
});

// The generated signature doesn't match AWS expectations
// Server returns 403 Forbidden with SignatureDoesNotMatch error
```

### Expected behavior

Query parameters should be canonicalized according to AWS Signature Version 4 specification:
- Parameters should be sorted by key name
- Format should be `key=value` pairs joined with `&`
- Both keys and values should be URL encoded

The current implementation appears to have the key-value pairs reversed, causing signature mismatches.

### System Info
- Insomnia version: latest
- Platform: All platforms affected

---
Repository: /testbed
