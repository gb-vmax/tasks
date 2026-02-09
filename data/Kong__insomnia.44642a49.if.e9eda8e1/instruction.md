# Bug Report

### Describe the bug

When importing OpenAPI 3 specs, security schemes are not being properly applied to requests when only one of `security` or `securitySchemes` is defined. The authentication configuration is being skipped entirely in cases where it should still be processed.

### Reproduction

Import an OpenAPI 3 spec with the following characteristics:

```yaml
openapi: 3.0.0
info:
  title: Test API
  version: 1.0.0
security:
  - apiKey: []
paths:
  /test:
    get:
      summary: Test endpoint
      responses:
        '200':
          description: Success
components:
  securitySchemes:
    apiKey:
      type: apiKey
      in: header
      name: X-API-Key
```

When importing this spec, the security configuration is not applied to the generated requests even though both `security` and `securitySchemes` are defined at different levels.

### Expected behavior

The importer should process security schemes when either `security` OR `securitySchemes` is present, not require both to be defined simultaneously. Authentication headers should be properly configured on imported requests.

### System Info
- Insomnia version: latest
- Platform: All

---
Repository: /testbed
