# Bug Report

### Describe the bug

When importing Swagger 2.0 specifications with string parameters that have `minLength` or `maxLength` constraints, the generated example values don't respect these constraints. The importer always generates the default string `"string"` regardless of the length requirements specified in the schema.

### Reproduction

Given a Swagger 2.0 spec with a parameter like:

```yaml
parameters:
  - name: code
    in: query
    type: string
    minLength: 10
    maxLength: 20
```

When importing this spec, the generated example value is `"string"` (6 characters), which violates the `minLength: 10` constraint.

Similarly, for a parameter with:
```yaml
parameters:
  - name: shortCode
    in: query
    type: string
    maxLength: 3
```

The generated example is still `"string"` (6 characters), exceeding the `maxLength: 3` constraint.

### Expected behavior

The importer should generate example values that satisfy the length constraints:
- For `minLength: 10`, it should generate a string with at least 10 characters
- For `maxLength: 3`, it should generate a string with at most 3 characters
- When both constraints are present, the generated string should be within the valid range

### Additional context

This affects API testing workflows where the generated examples are used as default request values. Invalid examples can cause confusion and require manual correction.

---
Repository: /testbed
