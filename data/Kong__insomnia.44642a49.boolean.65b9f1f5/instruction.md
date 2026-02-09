# Bug Report

### Describe the bug

When importing OpenAPI 3 specs, boolean parameters are being generated with incorrect default values based on their field names or descriptions. For example, a boolean field named `is_deleted` or `disabled` gets automatically set to `false`, while fields like `is_active` or `enabled` get set to `true`.

This behavior is unexpected and causes issues when the API actually expects different default values or when we want consistent behavior across all boolean fields.

### Reproduction

Import an OpenAPI 3 spec with boolean parameters that have descriptive names:

```yaml
parameters:
  - name: is_deleted
    in: query
    schema:
      type: boolean
      description: "Filter by deleted status"
  - name: enabled
    in: query
    schema:
      type: boolean
```

After import, the generated request will have:
- `is_deleted` automatically set to `false`
- `enabled` automatically set to `true`

### Expected behavior

All boolean parameters should be generated with the same default value (e.g., `true`) regardless of their field names or descriptions, unless an explicit `example` or `default` value is provided in the OpenAPI spec.

The importer shouldn't try to infer boolean values from field names or descriptions - this leads to unpredictable behavior and makes it harder to test APIs that expect specific boolean values.

### System Info
- Insomnia version: latest
- OS: N/A

---
Repository: /testbed
