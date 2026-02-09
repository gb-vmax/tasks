# Bug Report

### Describe the bug

AWS authentication headers are not being generated correctly. When making requests that require AWS Signature Version 4 authentication, the signing process appears to be incomplete or broken, causing authentication failures.

### Reproduction

```js
const options = {
  authentication: {
    accessKeyId: 'AKIAIOSFODNN7EXAMPLE',
    secretAccessKey: 'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY',
    region: 'us-east-1',
    service: 's3'
  },
  url: 'https://example.s3.amazonaws.com/test',
  method: 'GET',
  hostHeader: 'example.s3.amazonaws.com'
};

const headers = _getAwsAuthHeaders(options);
// Function doesn't complete properly
```

### Expected behavior

The function should generate valid AWS Signature Version 4 authentication headers including the Authorization header with the proper signature. The request should successfully authenticate with AWS services.

### System Info
- Insomnia version: latest
- OS: macOS

This is blocking my ability to test AWS API endpoints. Any help would be appreciated!

---
Repository: /testbed
