# Bug Report

### Describe the bug

When importing Postman collections with Bearer token authentication, the auth type is not being detected correctly. The importer seems to be treating Bearer tokens as unknown authentication and applying the wrong parsing logic.

### Reproduction

1. Export a Postman collection that contains a request with Bearer token authentication
2. The Authorization header should be in the format: `Authorization: Bearer <token>`
3. Import the collection into Insomnia
4. Check the authentication settings on the imported request

The Bearer authentication is not being recognized properly and the token value appears to be incorrect or missing.

### Expected behavior

The importer should correctly identify Bearer token authentication from the Authorization header and extract the token value. The imported request should have the same Bearer token configured as in the original Postman collection.

### Additional context

This seems to affect Bearer tokens specifically. Other auth types like Basic auth might be working fine. The issue appears to be in how the Authorization header string is being parsed to determine the auth type.

---
Repository: /testbed
