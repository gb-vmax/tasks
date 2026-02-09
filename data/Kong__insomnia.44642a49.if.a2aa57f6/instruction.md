# Bug Report

### Describe the bug

When importing Postman collections with Basic authentication headers, the authentication is not being properly extracted and applied. The imported requests end up with empty authentication configuration even though the Authorization header contains valid Basic auth credentials.

### Reproduction

1. Create a Postman collection with a request that has Basic authentication
2. Export the collection
3. Import the collection into Insomnia
4. Check the imported request - the Basic auth configuration is missing/empty

Example Authorization header that fails to import correctly:
```
Authorization: Basic dXNlcm5hbWU6cGFzc3dvcmQ=
```

### Expected behavior

The Basic authentication should be properly parsed from the Authorization header and the imported request should have the authentication configuration populated with the decoded username and password.

### Additional context

This seems to affect Basic auth specifically - other authentication types like Bearer tokens appear to import correctly. The issue started appearing in recent versions.

---
Repository: /testbed
