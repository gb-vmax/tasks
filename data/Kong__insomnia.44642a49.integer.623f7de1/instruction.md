# Bug Report

### Describe the bug

When importing OpenAPI 3 specs with integer parameters that have constraints like `minimum`, `maximum`, `exclusiveMinimum`, `exclusiveMaximum`, or `multipleOf`, the generated example values are not respecting these constraints. The importer always generates `0` as the example value regardless of the schema constraints.

### Reproduction

Given an OpenAPI 3 spec with an integer parameter:

```yaml
parameters:
  - name: page
    in: query
    schema:
      type: integer
      minimum: 1
      maximum: 100
```

When importing this spec, the generated example value is `0`, which violates the minimum constraint of `1`.

Similarly, for schemas with `multipleOf`:

```yaml
schema:
  type: integer
  multipleOf: 5
  minimum: 10
  maximum: 50
```

The generated value is still `0` instead of a valid multiple of 5 within the range.

### Expected behavior

The importer should generate example values that respect the integer constraints:
- For `minimum: 1`, it should generate at least `1`
- For `exclusiveMinimum: 5`, it should generate at least `6`
- For `multipleOf: 5` with `minimum: 10`, it should generate `10` or another valid multiple
- For `enum` values, it should use the first enum value if available

### System Info
- Insomnia version: latest
- Platform: All platforms

---
Repository: /testbed
