# Bug Report

### Describe the bug
When importing Swagger 2.0 specs with string parameters that have `minLength` constraints, the generated example values don't respect the minimum length requirement. The importer always generates the default "string" value regardless of the `minLength` property specified in the parameter definition.

### Reproduction
```yaml
# Swagger 2.0 spec with minLength constraint
parameters:
  - name: username
    in: query
    type: string
    minLength: 10
    description: Username must be at least 10 characters
```

When importing this spec, the generated example value is just "string" (6 characters) instead of a string with at least 10 characters to satisfy the minLength constraint.

### Expected behavior
The importer should generate example values that respect the `minLength` constraint defined in the parameter. For example, if `minLength: 10` is specified, the generated value should be at least 10 characters long (e.g., "stringxxxx").

Additionally, when a parameter has an `enum` property with values, the importer should use the first enum value as the example instead of generating a generic string.

### System Info
- Insomnia version: latest
- Import format: Swagger 2.0 / OpenAPI 2.0

---
Repository: /testbed
