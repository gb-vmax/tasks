# Bug Report

### Describe the bug

When importing cURL commands, the parser is not correctly extracting option values. It seems to be skipping the first value and trying to use the second value instead, which causes issues when there's only one value present for an option.

### Reproduction

Try importing a cURL command with single-value options:

```bash
curl -X POST https://example.com/api --data "test payload"
```

The `--data` option value should be "test payload", but it's not being parsed correctly. The importer appears to be looking for a second value when only one exists.

### Expected behavior

The cURL importer should correctly extract the first (and often only) value for each option. When an option like `--data` or `-X` is specified once, that value should be used.

### Additional context

This affects any cURL command where options are specified with single values, which is the most common use case. The parser logic seems to have changed to expect multiple values per option when most options only have one.

---
Repository: /testbed
