# Bug Report

### Describe the bug

When importing Postman collections with authorization headers that use non-standard auth type naming (like "Api-Key" or "API_KEY"), the importer fails to recognize them properly. The authorization header gets stripped but no authentication object is created, resulting in loss of authentication data.

### Reproduction

Import a Postman collection with an authorization header like:
```
Authorization: Api-Key abc123xyz
```

or

```
Authorization: API_KEY abc123xyz
```

After import, the authentication is missing from the request even though it was present in the original Postman collection.

### Expected behavior

The importer should handle various auth type naming conventions (with hyphens, underscores, different casing) and properly extract the authentication information. The auth data should be preserved in the imported request.

### Additional context

This seems to affect custom API key authentication schemes that don't follow the exact "Bearer", "Basic", etc. naming. The authorization header is being removed but not converted into an authentication object, so the credentials are lost during import.

---
Repository: /testbed
