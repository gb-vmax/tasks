# Bug Report

### Describe the bug

When importing Swagger 2.0 specifications, array parameters with `collectionFormat` set to `csv` are being generated incorrectly. The parameter examples are returned as single values instead of arrays, and non-csv formats are returned as arrays when they should be single values. This appears to be a logic inversion issue.

### Reproduction

Given a Swagger 2.0 spec with an array parameter:

```yaml
parameters:
  - name: tags
    in: query
    type: array
    collectionFormat: csv
    items:
      type: string
```

When importing this spec, the generated parameter example for `csv` format returns a single value instead of an array. Conversely, other collection formats (like `multi`, `pipes`, etc.) return arrays when they should return single values.

### Expected behavior

- Array parameters with `collectionFormat: 'csv'` should generate examples as arrays (e.g., `['value']`)
- Array parameters with other collection formats should generate examples as single values (e.g., `'value'`)

This is causing issues when trying to use the imported requests with array query parameters.

### System Info
- Insomnia version: latest
- Import format: Swagger 2.0

---
Repository: /testbed
