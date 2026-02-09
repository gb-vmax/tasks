# Bug Report

### Describe the bug

I'm experiencing an issue with OpenAPI 3 import where the security scheme selection appears to be broken. After a recent update, the importer seems to fail when processing security requirements for API endpoints.

### Reproduction

When importing an OpenAPI 3 spec with security schemes defined:

```yaml
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
    apiKey:
      type: apiKey
      in: header
      name: X-API-Key
security:
  - bearerAuth: []
  - apiKey: []
```

The import process doesn't complete successfully. It looks like the security parsing logic is incomplete or corrupted.

### Expected behavior

The importer should successfully parse and import OpenAPI 3 specs with security schemes, properly handling authentication configuration for requests.

### System Info
- Insomnia version: latest
- OS: Multiple platforms affected

This seems like a critical regression as it prevents importing specs that use authentication, which is pretty common. Would appreciate a fix soon!

---
Repository: /testbed
