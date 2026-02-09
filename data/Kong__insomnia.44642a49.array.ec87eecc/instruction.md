# Bug Report

### Describe the bug

When importing Swagger 2.0 specs with array parameters, the `collectionFormat` handling appears to be broken. Array parameters are not being formatted correctly regardless of the `collectionFormat` value specified in the spec.

### Reproduction

```yaml
swagger: "2.0"
paths:
  /items:
    get:
      parameters:
        - name: tags
          in: query
          type: array
          items:
            type: string
          collectionFormat: csv
```

When importing this spec, the array parameter doesn't get formatted as a CSV string. Instead, it seems to always return the same format regardless of whether `collectionFormat` is set to `csv`, `ssv`, `tsv`, `pipes`, or `multi`.

### Expected behavior

Array parameters should be formatted according to their `collectionFormat`:
- `csv` (default) - comma separated values: `tags=foo,bar,baz`
- `ssv` - space separated values: `tags=foo bar baz`
- `tsv` - tab separated values: `tags=foo\tbar\tbaz`
- `pipes` - pipe separated values: `tags=foo|bar|baz`
- `multi` - multiple parameter instances: `tags=foo&tags=bar&tags=baz`

Currently, all formats seem to produce the same output, which breaks the expected behavior for APIs that rely on specific collection formats.

### System Info
- Insomnia version: latest
- OS: N/A (affects all platforms)

---
Repository: /testbed
