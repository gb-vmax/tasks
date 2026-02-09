# Bug Report

### Describe the bug

The OpenAPI 3 importer is generating incorrect example values for string parameters. When importing an OpenAPI spec with string schema properties that have `minLength` or `maxLength` constraints, the generated examples don't respect these constraints.

### Reproduction

When importing an OpenAPI 3 spec with a string parameter defined like this:

```yaml
parameters:
  - name: code
    in: query
    schema:
      type: string
      minLength: 10
      maxLength: 20
```

The importer generates `'string'` as the example value, which is only 6 characters long and violates the `minLength: 10` constraint.

Similarly, for parameters with format specifications:

```yaml
parameters:
  - name: id
    in: query
    schema:
      type: string
      format: uuid
```

The example generated is still just `'string'` instead of a proper UUID format like `'3fa85f64-5717-4562-b3fc-2c963f66afa6'`.

### Expected behavior

The importer should generate example values that:
1. Respect `minLength` and `maxLength` constraints when specified
2. Use appropriate format-specific examples for common formats like `uuid`, `uri`, `ipv4`, `ipv6`, `hostname`, etc.

For the examples above:
- A string with `minLength: 10` should generate an example that's at least 10 characters
- A string with `format: uuid` should generate a UUID-formatted string

### System Info
- Insomnia version: latest
- OS: N/A (affects all platforms)

---
Repository: /testbed
