# Bug Report

### Describe the bug

When importing OpenAPI 3 specs with number parameters that have `format: double`, the generated example values are not deterministic. Running the import multiple times on the same spec produces different example values each time, which makes it difficult to track changes in version control and causes unnecessary diffs.

### Reproduction

```yaml
# OpenAPI spec with double format number
parameters:
  - name: price
    in: query
    schema:
      type: number
      format: double
      minimum: 10.0
      maximum: 100.0
```

Import this spec multiple times - the generated example value for the `price` parameter changes on each import, even though the spec hasn't changed.

### Expected behavior

The generated example values should be deterministic and consistent across imports when the OpenAPI spec hasn't changed. If I import the same spec twice, I should get the same example values both times.

### System Info
- Insomnia version: latest
- Platform: macOS

---
Repository: /testbed
