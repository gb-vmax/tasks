# Bug Report

### Describe the bug

After a recent update, the Swagger 2.0 importer is generating invalid parameter examples for string parameters with `minLength` or `maxLength` constraints. The generated examples don't respect these length constraints, which causes validation errors when using the imported requests.

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

The importer generates an example value that doesn't meet the minLength requirement (e.g., "string" which is only 6 characters), when it should generate a value between 10-20 characters.

Similarly, for parameters with `maxLength` smaller than the default example:

```yaml
parameters:
  - name: code
    in: query
    type: string
    maxLength: 3
```

The generated example exceeds the maxLength constraint.

### Expected behavior

The importer should generate example values that satisfy the minLength and maxLength constraints defined in the Swagger spec. If minLength is 10, the example should be at least 10 characters. If maxLength is 3, the example should be at most 3 characters.

### System Info
- Insomnia version: latest
- Import format: Swagger 2.0

---
Repository: /testbed
