# Bug Report

### Describe the bug
When importing OpenAPI 3 specs, required parameters are being marked as disabled in the generated requests. This is the opposite of what should happen - required parameters should be enabled by default, while optional parameters should be disabled.

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
1. Import the OpenAPI 3 spec above
2. Check the generated request parameters
3. The `userId` parameter (which is required) shows as disabled
4. The `filter` parameter (which is optional) shows as enabled

### Expected behavior
Required parameters should be enabled by default, and optional parameters should be disabled. The current behavior has this backwards.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
