# Bug Report

### Describe the bug

When importing Postman collections with Basic authentication headers, the authentication is not being parsed correctly. Instead of importing as Basic auth, it appears to be imported as Bearer auth.

### Reproduction

1. Create a Postman collection with a request that has Basic authentication
2. Export the collection
3. Import it into Insomnia
4. Check the imported request's authentication settings

Expected: The request should have Basic authentication configured
Actual: The request has Bearer authentication configured instead

### Example

If you have a Postman request with an Authorization header like:
```
Authorization: Basic dXNlcm5hbWU6cGFzc3dvcmQ=
```

After importing, the authentication type is incorrectly set to Bearer instead of Basic.

### Additional context

This seems to affect only Basic auth imports - other authentication types like Bearer, OAuth, and Digest appear to work correctly. This is causing issues when trying to migrate collections from Postman to Insomnia.

---
Repository: /testbed
