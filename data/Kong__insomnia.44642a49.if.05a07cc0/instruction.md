# Bug Report

### Describe the bug

When importing Postman collections with Bearer token authentication, the authentication type is not being detected correctly. The importer fails to recognize Bearer tokens from the Authorization header, resulting in requests being imported without authentication configured.

### Reproduction

Import a Postman collection containing a request with Bearer token authentication:

```json
{
  "request": {
    "header": [
      {
        "key": "Authorization",
        "value": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
      }
    ],
    "url": "https://api.example.com/data"
  }
}
```

After import, the request shows no authentication configured even though the Authorization header contains a valid Bearer token.

### Expected behavior

The importer should correctly detect the Bearer token from the Authorization header and configure the authentication accordingly. Other auth types like Basic, Digest, and OAuth should also be properly recognized.

### Additional context

This appears to affect all authentication types that are parsed from the Authorization header when no explicit authentication object is present in the Postman collection. The authentication detection seems to be failing silently.

---
Repository: /testbed
