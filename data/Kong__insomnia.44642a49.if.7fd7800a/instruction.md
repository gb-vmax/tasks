# Bug Report

### Describe the bug

When importing Postman collections with Authorization headers, the authentication type is not being detected correctly. Collections that use Bearer, Basic, Digest, OAuth, or AWS4-HMAC-SHA256 authentication are imported without any authentication configuration, even though the Authorization header is present in the collection.

### Reproduction

1. Export a Postman collection that has requests with Authorization headers (e.g., `Authorization: Bearer <token>`)
2. Import the collection into Insomnia
3. Check the imported requests

Expected: The authentication should be automatically configured based on the Authorization header
Actual: The requests are imported without authentication, and the Authorization header is missing

This affects all authentication types that should be parsed from the Authorization header:
- Bearer tokens
- Basic authentication
- Digest authentication
- OAuth 1.0
- AWS Signature v4

### Steps to Reproduce

```
1. Create a Postman collection with a request
2. Add an Authorization header like "Authorization: Bearer mytoken123"
3. Export the collection
4. Import into Insomnia
5. The authentication is not set up correctly
```

### Expected behavior

The importer should recognize the authentication type from the Authorization header and configure the appropriate authentication method for the imported requests.

### System Info
- Insomnia version: latest
- OS: macOS/Windows/Linux

---
Repository: /testbed
