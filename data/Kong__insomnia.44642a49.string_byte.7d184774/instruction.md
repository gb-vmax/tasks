# Bug Report

### Describe the bug

When importing Swagger 2.0 specs with `string_byte` parameters that have `minLength` or `maxLength` constraints, the generated example values don't respect these length constraints. The importer always generates the same default base64 string regardless of the specified length requirements.

### Reproduction

```yaml
swagger: "2.0"
info:
  version: "1.0.0"
  title: "Test API"
paths:
  /upload:
    post:
      parameters:
        - name: data
          in: body
          schema:
            type: string
            format: byte
            minLength: 50
            maxLength: 100
```

When importing this spec, the generated example for the `data` parameter is always `ZXhhbXBsZQ==` (which is only 12 characters) instead of a base64 string that respects the 50-100 character length constraint.

### Expected behavior

The importer should generate base64 example values that:
1. Respect `minLength` and `maxLength` constraints when specified
2. Use the `example` field from the parameter if it's valid base64
3. Fall back to the `default` field if it's valid base64
4. Only use the hardcoded default when no other options are available

### System Info
- Insomnia version: Latest
- OS: Any

This is causing issues when testing APIs that validate the length of base64-encoded data, as the generated examples are always too short and fail validation.

---
Repository: /testbed
