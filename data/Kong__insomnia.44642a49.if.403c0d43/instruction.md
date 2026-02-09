# Bug Report

### Describe the bug

When importing Postman collections with Bearer token authentication, the auth type is not being detected correctly. The authentication information is not being extracted from the Authorization header, causing requests to lose their auth configuration during import.

### Reproduction

Import a Postman collection that contains requests with Bearer token authentication in the Authorization header:

```json
{
  "request": {
    "header": [
      {
        "key": "Authorization",
        "value": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
      }
    ]
  }
}
```

After import, the authentication is not properly configured and the Bearer token is lost.

### Expected behavior

The importer should correctly identify the Bearer token from the Authorization header and set up the authentication accordingly. The auth type should be detected as "Bearer" and the token value should be preserved.

This also affects other auth types like Basic, Digest, OAuth, and AWS4-HMAC-SHA256 when they're specified in the Authorization header without explicit authentication configuration.

### System Info
- Insomnia version: latest
- Import format: Postman Collection v2

---
Repository: /testbed
