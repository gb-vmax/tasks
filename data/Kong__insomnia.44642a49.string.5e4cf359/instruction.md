# Bug Report

### Describe the bug

When importing OpenAPI 3 specifications, string parameters with patterns or formats are not generating appropriate example values. The importer always generates the generic string `"string"` regardless of the schema constraints defined in the spec.

### Reproduction

Import an OpenAPI 3 spec with a parameter that has a pattern constraint:

```yaml
parameters:
  - name: phoneNumber
    in: query
    schema:
      type: string
      pattern: '^\\d{3}-\\d{3}-\\d{4}$'
```

The generated example value is just `"string"` instead of something like `"123-456-7890"` that matches the pattern.

Same issue occurs with format constraints:

```yaml
parameters:
  - name: userId
    in: query
    schema:
      type: string
      format: uuid
```

Expected to generate a UUID-like example (e.g., `"3fa85f64-5717-4562-b3fc-2c963f66afa6"`), but instead just shows `"string"`.

### Expected behavior

The importer should generate realistic example values that:
- Match the `pattern` constraint when specified
- Use appropriate examples for common `format` values (uuid, uri, email, ipv4, etc.)
- Respect `minLength` and `maxLength` constraints
- Use the first value from `enum` if provided

This would make the imported requests much more useful for testing and development.

### System Info
- Insomnia version: latest
- OS: N/A

---
Repository: /testbed
