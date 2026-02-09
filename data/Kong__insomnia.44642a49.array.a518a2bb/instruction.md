# Bug Report

### Describe the bug

I'm encountering an issue with Swagger 2.0 import where array parameters with `collectionFormat` set to formats other than `csv` (like `ssv`, `tsv`, or `pipes`) are not being properly handled. The generated examples don't respect the specified collection format and always seem to default to a single value or array format.

### Reproduction

When importing a Swagger 2.0 spec with array parameters that use different collection formats:

```yaml
parameters:
  - name: tags
    in: query
    type: array
    collectionFormat: ssv
    items:
      type: string
```

The imported request doesn't generate the correct space-separated format for the example value. Same issue occurs with `tsv` (tab-separated) and `pipes` (pipe-separated) formats.

Additionally, when `minItems` or `maxItems` are specified on array parameters, the generated examples don't respect these constraints - they always generate a single item regardless of the minimum required.

### Expected behavior

- Array parameters with `collectionFormat: ssv` should generate space-separated values (e.g., `value1 value2`)
- Array parameters with `collectionFormat: tsv` should generate tab-separated values
- Array parameters with `collectionFormat: pipes` should generate pipe-separated values (e.g., `value1|value2`)
- When `minItems` is specified, the example should include at least that many items
- When `uniqueItems: true` is set, the generated example values should be unique

### System Info
- Insomnia version: latest
- Import format: Swagger 2.0

---
Repository: /testbed
