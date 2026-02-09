# Bug Report

### Describe the bug

When importing OpenAPI 3 specs with security schemes, the importer is failing to parse the security definitions correctly. It looks like there's an issue with the code structure - the `parseSecurity` function appears to be malformed or incomplete, causing imports to fail.

### Reproduction

1. Try to import an OpenAPI 3.0 spec that includes security schemes
2. The spec should have authentication defined (e.g., API key, OAuth2, etc.)
3. The import process fails or produces unexpected results

Example spec that triggers the issue:
```yaml
openapi: 3.0.0
info:
  title: Test API
  version: 1.0.0
components:
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: X-API-Key
security:
  - ApiKeyAuth: []
paths:
  /test:
    get:
      summary: Test endpoint
      responses:
        '200':
          description: Success
```

### Expected behavior

The OpenAPI spec should import successfully with the security schemes properly configured in the request authentication settings.

### System Info

- Insomnia version: latest
- OS: N/A

The function definition seems to be duplicated or incorrectly structured in the code. This is blocking our ability to import specs with authentication requirements.

---
Repository: /testbed
