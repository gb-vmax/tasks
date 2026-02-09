# Bug Report

### Describe the bug

When importing Swagger 2.0 specs with array parameters, the generated examples are inconsistent and contain random variations. The array length varies randomly between imports, and primitive values in arrays get modified with indices/variations that weren't in the original spec.

### Reproduction

Import a Swagger 2.0 spec with an array parameter definition:

```yaml
parameters:
  - name: tags
    in: query
    type: array
    items:
      type: string
    collectionFormat: csv
```

Expected: Consistent example generation across imports (e.g., `"string"` or `"string,string"`)

Actual: Random examples like `"string1,string2"` or `"string1,string2,string3"` with varying array lengths and modified values

The same spec imported multiple times produces different results each time due to:
1. Random array length (2-3 items via `Math.floor(Math.random() * 2) + 2`)
2. Values being modified with index suffixes (e.g., `string` becomes `string1`, `string2`, etc.)
3. Different behavior for dates, emails, and base64 strings

### Expected behavior

Array parameter examples should be deterministic and predictable. The same Swagger spec imported multiple times should generate identical examples. Simple array parameters should generate simple examples without unnecessary variations.

### System Info
- Version: Latest
- Import format: Swagger 2.0

---
Repository: /testbed
