# Bug Report

### Describe the bug

When importing Postman collections with AWS4 authentication, the authentication details are not being properly imported when an Authorization header is present. The importer returns an empty authentication object and drops the headers array, causing the imported request to lose important configuration data.

### Reproduction

```js
// Import a Postman collection with AWS Signature v4 authentication
const authHeader = 'AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20220110/us-east-1/s3/aws4_request, SignedHeaders=host;x-amz-date, Signature=abc123';
const headers = [
  { key: 'X-Amz-Security-Token', value: 'session-token-value' },
  { key: 'Host', value: 'example.com' }
];

// After import, the authentication object is empty and headers are lost
const result = importАwsv4AuthenticationFromHeader(authHeader, headers);
// result = { authentication: {} }
// Expected: authentication details extracted from header AND headers preserved
```

### Expected behavior

When an AWS4 authorization header is present, the importer should:
1. Parse the credentials from the Authorization header
2. Extract the session token from X-Amz-Security-Token header
3. Return both the parsed authentication object AND preserve the headers array

Currently, when an auth header exists, it returns an empty authentication object and completely drops the headers, which breaks the imported request configuration.

### System Info
- Insomnia version: latest
- Import source: Postman Collection v2

---
Repository: /testbed
