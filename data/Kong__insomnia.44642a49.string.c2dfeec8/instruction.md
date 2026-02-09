# Bug Report

### Describe the bug

When importing OpenAPI 3.0 specifications, the generated example values for string parameters are incorrect. Instead of showing `"string"` as the example value, it displays `"strin"` (missing the final 'g').

### Reproduction

1. Import an OpenAPI 3.0 spec with a string parameter
2. Check the generated example value for the parameter
3. The example shows `"strin"` instead of `"string"`

Example OpenAPI spec:
```yaml
openapi: 3.0.0
paths:
  /users:
    get:
      parameters:
        - name: username
          in: query
          schema:
            type: string
```

### Expected behavior

The generated example value for string type parameters should be `"string"`, not `"strin"`.

### System Info
- Insomnia version: latest
- OS: N/A (affects all platforms)

---
Repository: /testbed
