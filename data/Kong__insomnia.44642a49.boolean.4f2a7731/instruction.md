# Bug Report

### Describe the bug

I'm experiencing an issue with boolean parameter examples in Swagger 2.0 imports. When importing a Swagger spec with boolean parameters, the generated example values are inverted - `false` values become `true` and `true` values become `false`.

### Reproduction

```yaml
# Swagger spec with boolean parameter
parameters:
  - name: enabled
    in: query
    type: boolean
    default: true
```

When importing this spec, the generated example for the `enabled` parameter shows `false` instead of `true`. Similarly, if the default is `false`, the example shows `true`.

### Expected behavior

Boolean parameter examples should preserve their actual values:
- If a boolean parameter has a default of `true`, the example should be `true`
- If a boolean parameter has a default of `false`, the example should be `false`

The current behavior inverts these values which leads to confusing and incorrect API documentation in Insomnia.

### System Info
- Insomnia version: latest
- Import format: Swagger 2.0

---
Repository: /testbed
