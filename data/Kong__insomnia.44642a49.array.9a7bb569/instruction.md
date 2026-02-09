# Bug Report

### Describe the bug

I'm experiencing an issue with Swagger 2 imports where array parameters with `collectionFormat` are being generated incorrectly. When importing a Swagger 2 spec, array parameters that don't use CSV format are being returned as raw values instead of arrays, and CSV format arrays are being double-wrapped.

### Reproduction

```yaml
swagger: "2.0"
paths:
  /items:
    get:
      parameters:
        - name: ids
          in: query
          type: array
          collectionFormat: multi
          items:
            type: string
        - name: tags
          in: query
          type: array
          collectionFormat: csv
          items:
            type: string
```

When importing this spec:
- The `ids` parameter (multi format) generates a single value instead of an array
- The `tags` parameter (csv format) generates a nested array `[["value"]]` instead of `["value"]`

### Expected behavior

Array parameters should be generated as:
- **Non-CSV formats** (multi, ssv, tsv, pipes): Should return an array like `["value"]`
- **CSV format**: Should return a single value that can be joined with commas

The current behavior seems reversed from what it should be.

### System Info
- Insomnia version: latest
- Import format: Swagger 2.0

---
Repository: /testbed
