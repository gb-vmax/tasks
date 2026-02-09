# Bug Report

### Describe the bug
When importing Swagger 2.0 specs with array parameters, the generated examples are not correctly formatted according to the `collectionFormat` specification. Currently, array parameters with formats like `ssv` (space separated), `tsv` (tab separated), and `pipes` (pipe separated) are not being handled properly.

### Reproduction
```yaml
swagger: "2.0"
paths:
  /test:
    get:
      parameters:
        - name: tags
          in: query
          type: array
          collectionFormat: ssv
          items:
            type: string
        - name: ids
          in: query
          type: array
          collectionFormat: pipes
          items:
            type: integer
```

When importing this spec, the array parameter examples don't respect the `collectionFormat` setting. For example:
- `ssv` format should generate space-separated values like `value1 value2 value3`
- `pipes` format should generate pipe-separated values like `value1|value2|value3`
- `tsv` format should generate tab-separated values

Instead, the importer seems to only handle `csv` format correctly or returns a single-element array.

### Expected behavior
The importer should generate properly formatted example values based on the `collectionFormat` specified in the Swagger spec:
- `csv` → comma-separated: `value1,value2,value3`
- `ssv` → space-separated: `value1 value2 value3`
- `tsv` → tab-separated: `value1\tvalue2\tvalue3`
- `pipes` → pipe-separated: `value1|value2|value3`
- `multi` or default → array format: `["value1", "value2", "value3"]`

### System Info
- Insomnia version: latest
- Platform: All platforms

---
Repository: /testbed
