# Bug Report

### Describe the bug

When importing OpenAPI 3.0 specifications with security definitions, the security schemes are not being parsed correctly. The authentication and headers are not being applied to the imported requests even when valid security schemes are defined in the spec.

### Reproduction

```yaml
openapi: 3.0.0
info:
  title: Test API
  version: 1.0.0
security:
  - apiKey: []
components:
  securitySchemes:
    apiKey:
      type: apiKey
      in: header
      name: X-API-Key
paths:
  /test:
    get:
      summary: Test endpoint
      responses:
        '200':
          description: Success
```

Steps to reproduce:
1. Import the above OpenAPI spec
2. Check the generated request
3. Notice that security headers/authentication are missing from the request

### Expected behavior

The importer should apply the security schemes defined in the OpenAPI spec to the imported requests. Authentication configurations and required headers should be added based on the security requirements.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
