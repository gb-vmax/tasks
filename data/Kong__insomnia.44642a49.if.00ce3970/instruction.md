# Bug Report

### Describe the bug

When importing OpenAPI 3.0 specs, security schemes are not being properly applied to requests. The authentication, headers, and parameters that should be set based on the security definitions in the spec are missing from the imported requests.

### Reproduction

1. Import an OpenAPI 3.0 spec that includes security schemes (e.g., API key, bearer token)
2. Check the imported requests
3. Notice that authentication and security headers are not configured on the requests

Example spec snippet:
```yaml
security:
  - apiKey: []
securitySchemes:
  apiKey:
    type: apiKey
    in: header
    name: X-API-Key
```

After import, the requests don't have the X-API-Key header or any authentication configured, even though the security scheme is defined in the spec.

### Expected behavior

Requests should include the appropriate authentication configuration and headers based on the security schemes defined in the OpenAPI spec. If a global security requirement is defined, it should be applied to all imported requests.

### System Info
- Insomnia version: latest
- Platform: Windows/Mac/Linux

---
Repository: /testbed
