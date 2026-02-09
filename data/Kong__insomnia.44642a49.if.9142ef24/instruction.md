# Bug Report

### Describe the bug
When importing Postman collections with Bearer token authentication, the authentication header is not being imported correctly. The bearer token seems to be lost during the import process, resulting in requests without proper authentication.

### Reproduction
1. Export a Postman collection that contains requests with Bearer token authentication
2. Import the collection into Insomnia
3. Check the imported requests - the Bearer token authentication is missing

Example Postman collection structure:
```json
{
  "auth": {
    "type": "bearer",
    "bearer": [
      {
        "key": "token",
        "value": "my-secret-token",
        "type": "string"
      }
    ]
  }
}
```

After import, the authentication header is not set on the request.

### Expected behavior
The Bearer token should be properly imported and available in the request authentication settings. Requests should maintain their authentication configuration from the original Postman collection.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
