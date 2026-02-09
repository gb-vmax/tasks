# Bug Report

### Describe the bug

I'm having an issue with Swagger 2.0 import where array parameters with `collectionFormat` are not being handled correctly. When importing a Swagger spec with array-type parameters, the generated examples don't respect the collection format anymore.

### Reproduction

Import a Swagger 2.0 spec with an array parameter like this:

```yaml
parameters:
  - name: tags
    in: query
    type: array
    collectionFormat: csv
    items:
      type: string
```

The parameter example should be generated as a comma-separated value (e.g., `value1,value2`), but instead it's being returned as just a single value regardless of the `collectionFormat` setting.

### Expected behavior

Array parameters should generate examples based on their `collectionFormat`:
- `csv` format should return the value directly (comma-separated string)
- Other formats (like `multi`, `ssv`, `tsv`, `pipes`) should return an array with the value

Currently all formats seem to return the same thing, which breaks the expected parameter format.

### System Info
- Insomnia version: latest
- Import format: Swagger 2.0

---
Repository: /testbed
