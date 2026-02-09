# Bug Report

### Describe the bug

When importing OpenAPI 3 specs with number parameters that have `format: float`, the generated example values are always `0.0` regardless of any constraints defined in the schema (like `minimum`, `maximum`, `exclusiveMinimum`, `exclusiveMaximum`, or `multipleOf`).

### Reproduction

Given an OpenAPI 3 spec with a float parameter:

```yaml
parameters:
  - name: temperature
    in: query
    schema:
      type: number
      format: float
      minimum: 10.0
      maximum: 100.0
```

When importing this spec, the generated example value is `0.0` instead of a value that respects the minimum/maximum constraints (e.g., `55.0`).

Similarly, if the schema includes `multipleOf`:

```yaml
schema:
  type: number
  format: float
  minimum: 5.0
  maximum: 20.0
  multipleOf: 2.5
```

The generated example is still `0.0` instead of a valid value like `12.5`.

### Expected behavior

The importer should generate example values for float numbers that:
- Fall within the specified `minimum` and `maximum` range
- Respect `exclusiveMinimum` and `exclusiveMaximum` constraints
- Are valid multiples when `multipleOf` is specified
- Default to a reasonable value within the constraints (e.g., midpoint of the range)

### System Info
- Insomnia version: latest
- Import format: OpenAPI 3.x

---
Repository: /testbed
