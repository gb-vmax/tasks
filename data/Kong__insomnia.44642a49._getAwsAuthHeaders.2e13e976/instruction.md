# Bug Report

### Describe the bug
When making AWS authenticated requests, the application crashes with a syntax error. The request fails to complete and the entire authentication flow is broken.

### Reproduction
```js
const request = {
  authentication: {
    accessKeyId: 'AKIAIOSFODNN7EXAMPLE',
    secretAccessKey: 'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY',
    region: 'us-east-1',
    service: 's3'
  },
  url: 'https://example.s3.amazonaws.com/test',
  method: 'GET'
};

// This causes a crash
_getAwsAuthHeaders(request);
```

### Expected behavior
The AWS authentication headers should be generated successfully and the request should proceed without errors. The function should return an array of header objects with the proper AWS Signature Version 4 authentication.

### System Info
- Node version: 18.x
- OS: macOS

This appears to be a recent regression as AWS requests were working fine in the previous version.

---
Repository: /testbed
