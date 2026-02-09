# Bug Report

### Describe the bug

When importing OpenAPI 3 specs, required parameters are being disabled by default instead of enabled. This is backwards from what it should be - required parameters should be enabled and optional parameters should be disabled.

### Reproduction

```yaml
openapi: 3.0.0
paths:
  /users:
    get:
      parameters:
        - name: userId
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
1. Import the above OpenAPI spec into Insomnia
2. Check the generated request parameters
3. The `userId` parameter (which is required) shows as disabled
4. The `filter` parameter (which is optional) shows as enabled

### Expected behavior

Required parameters should be enabled by default, and optional parameters should be disabled. In the example above:
- `userId` (required: true) should be enabled
- `filter` (required: false) should be disabled

### System Info
- Insomnia version: latest
- OS: N/A

---
Repository: /testbed
