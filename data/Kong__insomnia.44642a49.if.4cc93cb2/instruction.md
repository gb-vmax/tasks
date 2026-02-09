# Bug Report

### Describe the bug

When importing Postman collections with authorization headers that contain extra whitespace or irregular spacing, the authentication type is not being recognized correctly. The importer fails to parse the authorization scheme, resulting in authentication not being imported properly.

### Reproduction

Import a Postman collection with an authorization header that has extra spaces, for example:

```
Authorization: Bearer    eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

or

```
Authorization: Basic   dXNlcm5hbWU6cGFzc3dvcmQ=
```

The authentication settings are not imported correctly when there are multiple spaces between the auth scheme and the token.

### Expected behavior

The importer should handle authorization headers with extra whitespace gracefully and correctly extract the authentication scheme and credentials regardless of spacing inconsistencies. Headers with extra spaces should be normalized and parsed the same way as properly formatted headers.

### Additional context

This seems to affect all authentication types that use the Authorization header (Bearer, Basic, AWS4-HMAC-SHA256, Digest, OAuth). Collections exported from some tools or manually edited may contain irregular spacing that should still be valid.

---
Repository: /testbed
