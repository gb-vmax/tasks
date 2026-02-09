# Bug Report

### Describe the bug

The Swagger 2.0 importer is generating invalid base64 strings for `byte` format parameters when `minLength` or `maxLength` constraints are specified. The generated example values don't properly account for base64 encoding overhead, resulting in strings that don't meet the length requirements.

### Reproduction

When importing a Swagger 2.0 spec with a parameter like this:

```yaml
parameters:
  - name: data
    in: body
    schema:
      type: string
      format: byte
      minLength: 20
      maxLength: 50
```

The generated example value is a base64 string, but the actual decoded byte length doesn't match the specified constraints. For example, a base64 string of length 20 decodes to only 15 bytes, not 20.

### Expected behavior

When `minLength` and `maxLength` are specified for byte format parameters, the importer should generate base64 strings where the **decoded** byte content matches those length constraints, not the base64-encoded string itself.

For a `minLength: 20`, the generated base64 string should decode to at least 20 bytes of data.

### System Info
- Insomnia version: latest
- OS: N/A (affects all platforms)

---
Repository: /testbed
