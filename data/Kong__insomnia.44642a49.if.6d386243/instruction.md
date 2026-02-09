# Bug Report

### Describe the bug

I'm experiencing an issue with importing Postman collections that contain authorization headers. After a recent update, the import process seems to break or hang when processing collections with auth headers.

### Reproduction

When trying to import a Postman collection that includes authentication in the request headers (e.g., Bearer tokens, Basic auth, etc.), the import fails to complete properly. 

Steps to reproduce:
1. Export a Postman collection that contains requests with Authorization headers
2. Try to import this collection into Insomnia
3. The import process doesn't complete successfully

This was working fine in previous versions. I've tested with collections containing:
- Bearer token authentication
- Basic authentication  
- AWS signature authentication

### Expected behavior

The Postman collection should import successfully with all authentication headers properly converted to Insomnia's authentication format.

### Additional context

This seems to affect all types of authorization headers, not just specific auth schemes. The import process appears to get stuck when trying to parse the authentication information from the headers.

---
Repository: /testbed
