# Bug Report

### Describe the bug

After a recent update, the Swagger 2.0 importer is generating invalid example values for string parameters. When importing an OpenAPI/Swagger spec with string parameters that have `minLength` or `maxLength` constraints, the generated examples don't respect these validation rules.

### Reproduction

Import a Swagger 2.0 spec with a string parameter that has length constraints:

```yaml
parameters:
  - name: username
    in: query
    type: string
    minLength: 10
    maxLength: 20
```

The importer generates `'string'` as the example value, which is only 6 characters and violates the `minLength: 10` constraint.

Similarly, for parameters with only `maxLength`:
```yaml
parameters:
  - name: code
    in: query
    type: string
    maxLength: 4
```

The generated example `'string'` (6 characters) exceeds the `maxLength: 4` constraint.

### Expected behavior

The importer should generate example values that satisfy the parameter constraints:
- For `minLength: 10`, the example should be at least 10 characters long
- For `maxLength: 4`, the example should be at most 4 characters long
- For both constraints together, the example should fall within the valid range

This is causing validation errors when trying to use the imported requests, as the default examples are invalid according to the API specification.

### System Info
- Insomnia version: latest
- Platform: all platforms affected

---
Repository: /testbed
