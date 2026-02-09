# Bug Report

### Describe the bug

I'm encountering an issue with AWS authentication header generation where the query string is being parsed incorrectly. When making requests with query parameters, the canonical query string seems to be malformed, which causes authentication to fail.

### Reproduction

```js
const options = {
  authentication: {
    accessKeyId: 'AKIAIOSFODNN7EXAMPLE',
    secretAccessKey: 'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY',
    region: 'us-east-1',
    service: 's3'
  },
  url: 'https://example.amazonaws.com/path?param1=value1&param2=value2',
  method: 'GET'
};

const headers = _getAwsAuthHeaders(options);
// Authentication fails with signature mismatch
```

### Expected behavior

The query string should be properly extracted and included in the canonical request for AWS signature calculation. URLs with query parameters should authenticate successfully.

### Additional context

This appears to be related to how the query string is being extracted from the URL. The canonical query string is a critical component of AWS Signature Version 4, and any issues with its parsing will cause authentication failures.

---
Repository: /testbed
