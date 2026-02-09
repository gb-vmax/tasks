# Bug Report

### Describe the bug

When importing OpenAPI 3.0 specs with security schemes defined but no security requirements at the operation level, the authentication object is being incorrectly set. This causes issues where authentication is applied even when it shouldn't be.

### Reproduction

```yaml
openapi: 3.0.0
info:
  title: Test API
  version: 1.0.0
security: []  # No global security
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
paths:
  /test:
    get:
      # No security defined for this operation
      responses:
        '200':
          description: Success
```

When importing this spec:
1. The operation has no security requirements (security array is empty/undefined)
2. Security schemes are defined in components
3. The importer incorrectly applies authentication to the request

### Expected behavior

When an operation has no security requirements defined, no authentication should be applied to that request, even if security schemes exist in the spec. The authentication object should remain null/empty for operations without security.

### System Info
- Insomnia version: latest
- Platform: All

---
Repository: /testbed
