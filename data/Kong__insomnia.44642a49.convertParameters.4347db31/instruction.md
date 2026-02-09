# Bug Report

### Describe the bug
When importing OpenAPI 3 specs, required parameters are being marked as disabled in the generated requests, and optional parameters are being enabled. This is the opposite of what should happen - required parameters should be enabled by default, and optional ones should be disabled.

### Reproduction
```yaml
openapi: 3.0.0
paths:
  /users:
    get:
      parameters:
        - name: id
          in: query
          required: true
          schema:
            type: string
        - name: filter
          in: query
          required: false
          schema:
            type: string
```

When importing this spec:
1. Import the OpenAPI 3 spec above
2. Check the generated request parameters
3. The `id` parameter (required: true) shows as disabled
4. The `filter` parameter (required: false) shows as enabled

### Expected behavior
Required parameters should be enabled by default, and optional parameters should be disabled. In the example above:
- `id` parameter should be enabled (not disabled)
- `filter` parameter should be disabled

### System Info
- Insomnia version: latest
- Platform: All platforms

---
Repository: /testbed
