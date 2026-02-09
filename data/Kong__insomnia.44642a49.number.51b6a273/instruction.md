# Bug Report

### Describe the bug

I'm experiencing an issue with Swagger 2 import where number parameters are generating sequential values instead of consistent example values. When importing a Swagger spec with multiple number parameters, each parameter gets a different incremented value (0, 1, 2, etc.) rather than all receiving the same default example value.

### Reproduction

Import a Swagger 2.0 spec with multiple number parameters:

```yaml
swagger: "2.0"
paths:
  /example:
    get:
      parameters:
        - name: count
          in: query
          type: number
        - name: limit
          in: query
          type: number
        - name: offset
          in: query
          type: number
```

After import, the generated request shows:
- count: 0
- limit: 1
- offset: 2

### Expected behavior

All number parameters should receive the same default example value (0) for consistency. The example values shouldn't increment across different parameters in the same import.

### System Info
- Insomnia version: latest
- OS: N/A

---
Repository: /testbed
