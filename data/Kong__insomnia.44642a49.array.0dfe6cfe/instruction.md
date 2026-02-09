# Bug Report

### Describe the bug

I'm experiencing an issue with Swagger 2.0 import where array parameters with `collectionFormat` are not being generated correctly. When importing a Swagger spec with array parameters, the example values seem to be inverted or empty depending on the collection format.

### Reproduction

When importing a Swagger 2.0 spec with array parameters:

```yaml
parameters:
  - name: ids
    in: query
    type: array
    collectionFormat: csv
    items:
      type: string
```

The generated parameter example appears to be empty instead of containing the expected value. For non-csv collection formats, the behavior also seems incorrect - getting a single value instead of an array.

### Expected behavior

- For `collectionFormat: 'csv'`, the parameter example should return the generated value from items
- For other collection formats (or when not specified), the parameter example should return an array containing the generated value

### System Info

- Insomnia version: latest
- Import format: Swagger 2.0 / OpenAPI 2.0

This is affecting my ability to test APIs with array query parameters after importing the spec. The request examples don't have the proper structure.

---
Repository: /testbed
