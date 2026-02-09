# Bug Report

### Describe the bug

When importing OpenAPI 3 specs with boolean parameters that have default values, the generated examples are not consistently using the default value. The behavior seems random - sometimes it uses the default, sometimes it doesn't.

### Reproduction

```yaml
openapi: 3.0.0
paths:
  /api/test:
    get:
      parameters:
        - name: enabled
          in: query
          schema:
            type: boolean
            default: false
```

When importing this spec, the parameter example for `enabled` should consistently be `false` (the default value), but instead it randomly generates either `true` or `false`.

### Expected behavior

When a boolean parameter has a `default` value specified in the schema, the generated example should use that default value consistently, not randomly choose between true and false.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
