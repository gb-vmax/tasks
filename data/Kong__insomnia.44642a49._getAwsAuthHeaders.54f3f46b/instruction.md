# Bug Report

### Describe the bug

AWS authentication headers are being generated incorrectly when query parameters are present in the URL. The canonical query string is being sorted in the wrong order (descending instead of ascending), which causes signature mismatches and authentication failures.

### Reproduction

```js
const auth = {
  accessKeyId: 'AKIAIOSFODNN7EXAMPLE',
  secretAccessKey: 'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY',
  region: 'us-east-1',
  service: 's3'
};

const url = 'https://example.amazonaws.com/path?zebra=value&alpha=value&beta=value';
const headers = _getAwsAuthHeaders({
  authentication: auth,
  url: url,
  method: 'GET',
  hostHeader: 'example.amazonaws.com'
});

// The generated signature will be incorrect because query params are sorted backwards
// Expected: alpha=value&beta=value&zebra=value
// Actual: zebra=value&beta=value&alpha=value
```

When making requests to AWS services with query parameters, the authentication fails with 403 Forbidden errors because the signature doesn't match what AWS expects.

### Expected behavior

Query parameters should be sorted in ascending lexicographical order when building the canonical query string for AWS Signature Version 4. This is required by the AWS signing specification.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
