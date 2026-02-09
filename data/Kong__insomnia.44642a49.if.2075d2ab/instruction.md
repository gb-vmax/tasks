# Bug Report

### Describe the bug

When importing OpenAPI 3 specifications with security schemes defined but no security requirements at the operation level, the importer is not properly handling the authentication configuration. The security schemes from the spec are being ignored in this case.

### Reproduction

```yaml
openapi: 3.0.0
info:
  title: Test API
  version: 1.0.0
security: []
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
paths:
  /test:
    get:
      summary: Test endpoint
      responses:
        '200':
          description: Success
```

When importing this spec:
1. The `securitySchemes` are defined in components
2. No security requirements are set at the operation level (empty array)
3. Expected: Security schemes should still be available for manual selection
4. Actual: Security configuration is completely ignored

### Expected behavior

Even when security requirements are not explicitly set on operations, the defined security schemes should still be parsed and made available in the imported collection. This allows users to manually configure authentication after import.

### System Info
- Insomnia version: latest
- Platform: All platforms

---
Repository: /testbed
