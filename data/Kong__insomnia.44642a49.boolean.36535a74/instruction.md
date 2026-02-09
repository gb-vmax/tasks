# Bug Report

### Describe the bug

When importing OpenAPI 3.0 specs with boolean parameters, the generated examples are not consistent with the schema definition. Boolean parameters always default to `true` regardless of what's specified in the schema's `default` value or `enum` constraints.

### Reproduction

Given an OpenAPI spec with a boolean parameter:

```yaml
parameters:
  - name: isActive
    in: query
    schema:
      type: boolean
      default: false
```

When importing this spec, the generated example always shows `true` instead of respecting the `default: false` value.

Similarly, for boolean parameters with enum constraints:

```yaml
parameters:
  - name: enabled
    in: query
    schema:
      type: boolean
      enum: [false]
```

The generated example ignores the enum restriction and still generates `true`.

### Expected behavior

- When a boolean schema has a `default` value, the generated example should use that default value
- When a boolean schema has an `enum` constraint, the generated example should respect those allowed values
- Boolean examples should be deterministic based on schema properties rather than always returning `true`

### System Info
- Insomnia version: latest
- OS: N/A (affects all platforms)

---
Repository: /testbed
