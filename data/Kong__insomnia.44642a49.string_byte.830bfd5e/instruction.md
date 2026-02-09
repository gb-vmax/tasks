# Bug Report

### Describe the bug

When importing OpenAPI 3.0 specs with `string` parameters that have `format: byte` and include `minLength` or `maxLength` constraints, the generated example values don't respect these length constraints properly. The base64-encoded examples either exceed the `maxLength` or fall short of the `minLength` specified in the schema.

### Reproduction

Given an OpenAPI 3.0 spec with a parameter like:

```yaml
parameters:
  - name: data
    in: query
    schema:
      type: string
      format: byte
      minLength: 20
      maxLength: 50
```

When importing this spec into Insomnia, the generated example value for the `data` parameter doesn't respect the length constraints. Sometimes the generated base64 string is too short (less than 20 characters) or too long (more than 50 characters).

### Expected behavior

The generated example should be a valid base64 string that:
- Has a length >= `minLength` when `minLength` is specified
- Has a length <= `maxLength` when `maxLength` is specified
- Respects both constraints when both are present

### System Info
- Insomnia version: latest
- Platform: All platforms

This is causing issues when testing APIs that have strict validation on base64-encoded parameters with length requirements.

---
Repository: /testbed
