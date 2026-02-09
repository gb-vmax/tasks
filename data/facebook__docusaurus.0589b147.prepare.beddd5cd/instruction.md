# Bug Report

### Describe the bug

I'm experiencing an issue with front matter validation where numeric values in YAML front matter are being incorrectly converted to strings. This is causing unexpected behavior when working with numeric fields.

### Reproduction

```yaml
---
id: 123
order: 5
count: 42
---
```

When parsing the above front matter, the numeric values (`123`, `5`, `42`) are being converted to strings (`"123"`, `"5"`, `"42"`) when they should remain as numbers.

### Expected behavior

Numeric values in front matter should be preserved as numbers, not automatically converted to strings. Only Date objects and other non-numeric types should be converted to strings during the validation process.

### Additional context

This seems to affect any numeric field in the front matter. The validation logic appears to be converting numbers to strings even when that conversion isn't necessary or desired.

---
Repository: /testbed
