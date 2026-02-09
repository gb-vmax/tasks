# Bug Report

### Describe the bug

When importing Swagger 2.0 specs with boolean parameters, the generated example values are not deterministic. The boolean example generation seems to be using some kind of alternating logic based on ancestor depth, which produces inconsistent and unpredictable results across different imports of the same spec.

### Reproduction

```yaml
swagger: "2.0"
paths:
  /api/test:
    get:
      parameters:
        - name: enabled
          in: query
          type: boolean
        - name: active
          in: query
          type: boolean
```

When importing this spec multiple times or with different nested structures, the boolean parameters get different example values (sometimes `true`, sometimes `false`) even though the spec hasn't changed.

### Expected behavior

Boolean parameters should have consistent example values. Ideally:
- If the parameter has an `enum` defined, use the first value
- If the parameter has an `x-example` extension, use that value
- Otherwise, default to a consistent value like `true`

The current behavior makes it difficult to rely on the generated examples for testing or documentation purposes.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
