# Bug Report

### Describe the bug

I'm experiencing an issue with OpenAPI 3 imports where numeric parameters are generating incorrect example values. When importing an OpenAPI spec with multiple number-type parameters, the generated examples show unexpected negative values instead of the expected default of 0.

### Reproduction

```yaml
openapi: 3.0.0
paths:
  /api/test:
    get:
      parameters:
        - name: param1
          in: query
          schema:
            type: number
        - name: param2
          in: query
          schema:
            type: number
        - name: param3
          in: query
          schema:
            type: number
```

When importing this spec, the generated request shows:
- param1: -1
- param2: 0
- param3: 0

### Expected behavior

All number-type parameters should generate example values of 0, not -1 for the first parameter. The behavior should be consistent across all number parameters.

### System Info
- Insomnia version: latest
- OS: macOS

This seems to have started happening recently. The first number parameter in any request is getting a -1 value which doesn't make sense as a default example.

---
Repository: /testbed
