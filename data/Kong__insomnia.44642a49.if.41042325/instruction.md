# Bug Report

### Describe the bug

When importing OpenAPI 3.0 specs that include security definitions, the authentication configuration is not being properly parsed and applied to the imported requests. The security schemes defined in the spec are being ignored, and all requests are imported without any authentication settings.

### Reproduction

1. Create an OpenAPI 3.0 spec with security schemes defined:
```yaml
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
security:
  - bearerAuth: []
paths:
  /api/users:
    get:
      summary: Get users
```

2. Import this spec into Insomnia
3. Check the imported request's authentication settings

### Expected behavior

The imported requests should have the bearer token authentication configured based on the security schemes defined in the OpenAPI spec. Currently, the authentication is empty even though valid security definitions are present.

### System Info
- Insomnia version: latest
- OS: macOS

This seems like a regression as security schemes were working in previous versions. Any API specs with authentication requirements are now being imported without the proper auth configuration.

---
Repository: /testbed
