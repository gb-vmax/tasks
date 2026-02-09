# Bug Report

### Describe the bug
When importing Postman collections with AWS Signature v4 authentication, the authentication object is being incorrectly populated with headers instead of the actual authentication credentials. This causes the imported requests to have malformed authentication configuration.

### Reproduction
```js
// Import a Postman collection with AWS v4 auth
// The Authorization header looks like:
// AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20220110/us-east-1/s3/aws4_request, SignedHeaders=host;x-amz-date, Signature=...

// After import, the authentication object contains headers instead of parsed credentials
// Expected: authentication object with accessKey, region, service, etc.
// Actual: authentication object is set to the headers array
```

### Steps to reproduce:
1. Create a Postman collection with a request using AWS Signature v4 authentication
2. Ensure the request has an Authorization header with AWS4-HMAC-SHA256 format
3. Import the collection into Insomnia
4. Check the imported request's authentication configuration

### Expected behavior
The authentication object should contain the parsed AWS credentials (access key, region, service, session token if present) extracted from the Authorization header, not the headers array itself.

### Additional context
This appears to affect any Postman collection using AWS v4 authentication. The authentication configuration becomes unusable after import, requiring manual reconfiguration of all AWS authenticated requests.

---
Repository: /testbed
