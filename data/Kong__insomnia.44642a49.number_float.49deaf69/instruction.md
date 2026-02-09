# Bug Report

### Describe the bug

When importing OpenAPI 3.0 specs with float/number parameters that have constraints (minimum, maximum, exclusiveMinimum, exclusiveMaximum, multipleOf), the generated example values don't respect these constraints. The importer always generates `0.0` as the example value regardless of the schema constraints.

### Reproduction

Given an OpenAPI 3.0 spec with a float parameter like:

```yaml
parameters:
  - name: price
    in: query
    schema:
      type: number
      format: float
      minimum: 10.0
      maximum: 100.0
```

When importing this spec, the generated example value is `0.0`, which violates the minimum constraint of `10.0`.

Similarly, for schemas with `multipleOf`:

```yaml
schema:
  type: number
  format: float
  multipleOf: 0.5
  minimum: 5.0
  maximum: 10.0
```

The generated example should be a valid multiple of 0.5 within the range, but instead it generates `0.0`.

### Expected behavior

The importer should generate example values that satisfy all schema constraints:
- Values should be within minimum/maximum bounds
- Values should respect exclusiveMinimum/exclusiveMaximum
- Values should be valid multiples when multipleOf is specified

For the first example above, a valid example would be any value between 10.0 and 100.0 (e.g., 55.0).
For the second example, a valid example would be something like 7.5 (within range and a multiple of 0.5).

### System Info
- Insomnia version: latest
- Platform: All platforms affected

---
Repository: /testbed
