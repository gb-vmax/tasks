# Bug Report

### Describe the bug

When importing OpenAPI 3.0 specs with deprecated parameters, the parameters are being automatically disabled in the imported requests. This makes it difficult to test deprecated endpoints that still need to be functional during the deprecation period.

### Reproduction

Given an OpenAPI spec with a deprecated parameter:

```yaml
paths:
  /users:
    get:
      parameters:
        - name: legacy_filter
          in: query
          deprecated: true
          required: true
          schema:
            type: string
```

When importing this spec:
1. Import the OpenAPI 3.0 specification
2. Check the generated request for the `/users` endpoint
3. The `legacy_filter` parameter is disabled even though it's marked as required

### Expected behavior

Deprecated parameters should remain enabled if they are marked as `required: true`. The deprecation status should be indicated (perhaps in the parameter name or description) but shouldn't automatically disable the parameter since deprecated doesn't mean non-functional.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
