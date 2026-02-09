# Bug Report

### Describe the bug

When importing Postman collections that use AWS Signature v4 authentication with an authorization header, the authentication configuration is not being imported correctly. The imported request ends up with no authentication settings even though the original Postman collection had AWS auth configured.

### Reproduction

1. Export a Postman collection that contains a request with AWS Signature v4 authentication
2. The collection should have an `Authorization` header with AWS4-HMAC-SHA256 format
3. Import this collection into Insomnia
4. Check the imported request's authentication settings

Expected: The request should have AWS v4 authentication configured with the appropriate credentials
Actual: The request has no authentication configured (authentication is null/empty)

### Example

Here's a sample authorization header that should be parsed:
```
AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20220110/us-east-1/s3/aws4_request, SignedHeaders=host;x-amz-date, Signature=abc123...
```

After import, the authentication object should contain the access key, region, service, etc. extracted from this header, but instead it's empty.

### System Info
- Insomnia version: latest
- OS: macOS

This seems like a regression as AWS auth imports were working in previous versions. Any help would be appreciated!

---
Repository: /testbed
