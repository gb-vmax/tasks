# Bug Report

### Describe the bug

When importing Postman collections that use Bearer token authentication in the Authorization header, the token is not being imported correctly. The authentication information appears to be missing from the imported requests.

### Reproduction

1. Export a Postman collection that has requests with Bearer token authentication set via the Authorization header
2. Import the collection into Insomnia
3. Check the imported requests - the Bearer token authentication is missing

Example Postman collection structure:
```json
{
  "request": {
    "header": [
      {
        "key": "Authorization",
        "value": "Bearer my-secret-token"
      }
    ]
  }
}
```

After import, the Authorization header with the Bearer token should be present but it's not showing up in the imported request.

### Expected behavior

The Bearer token from the Authorization header should be properly imported and available in the request configuration.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
