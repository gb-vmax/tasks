# Bug Report

### Describe the bug

When importing OpenAPI 3 specs, the parameter example generation is broken. Getting syntax errors during import that prevent the spec from being loaded properly.

### Reproduction

Try importing an OpenAPI 3.0 spec that has string parameters with patterns, enums, or length constraints. The import fails with what looks like a parsing error.

Example spec snippet that causes the issue:
```yaml
parameters:
  - name: userId
    in: path
    schema:
      type: string
      pattern: '^[a-zA-Z]+$'
  - name: status
    in: query
    schema:
      type: string
      enum: ['active', 'inactive']
```

The import process errors out and the spec can't be loaded into Insomnia.

### Expected behavior

The OpenAPI spec should import successfully and generate appropriate example values for string parameters based on their constraints (patterns, enums, length requirements).

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
