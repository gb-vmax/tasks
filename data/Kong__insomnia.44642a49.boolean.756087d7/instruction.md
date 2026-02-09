# Bug Report

### Describe the bug

When importing OpenAPI 3 specs with boolean parameters, all boolean values are being generated as `true` by default. This makes it difficult to test API endpoints that have different behavior based on boolean flags, since the generated examples don't vary.

### Reproduction

```yaml
openapi: 3.0.0
paths:
  /api/users:
    get:
      parameters:
        - name: isActive
          in: query
          schema:
            type: boolean
        - name: isVerified
          in: query
          schema:
            type: boolean
```

When importing this spec, both `isActive` and `isVerified` parameters get example values of `true`. It would be more useful if the generated examples had some variation (some true, some false) to better represent different API scenarios.

### Expected behavior

Boolean parameters should generate varied example values (mix of `true` and `false`) or respect the `example`/`default` values if specified in the schema. This would make the imported requests more representative of real-world usage.

### System Info
- Insomnia version: latest
- OpenAPI spec version: 3.0.0

---
Repository: /testbed
