# Bug Report

### Describe the bug

When importing OpenAPI 3 specs with numeric parameters that have constraints like `minimum`, `maximum`, `exclusiveMinimum`, `exclusiveMaximum`, or `multipleOf`, the generated example values are not respecting these constraints. The importer always generates `0` as the example value regardless of the schema constraints, which can result in invalid examples that don't satisfy the API requirements.

### Reproduction

```yaml
# OpenAPI spec with numeric constraints
parameters:
  - name: quantity
    in: query
    schema:
      type: number
      minimum: 1
      maximum: 100
  - name: price
    in: query
    schema:
      type: number
      exclusiveMinimum: 0
      multipleOf: 0.01
```

When importing this spec, the generated examples for both `quantity` and `price` are `0`, which violates the constraints:
- `quantity` should be between 1 and 100, but `0` is generated
- `price` should be greater than 0 and a multiple of 0.01, but `0` is generated (which is not > 0)

### Expected behavior

The importer should generate example values that respect the numeric constraints defined in the schema:
- For `minimum`/`maximum`, the example should be within the specified range
- For `exclusiveMinimum`/`exclusiveMaximum`, the example should be strictly greater/less than the boundary
- For `multipleOf`, the example should be a valid multiple of the specified value

For example:
- `quantity` should generate a value like `50` (midpoint between 1 and 100)
- `price` should generate a value like `0.01` (smallest valid value > 0 that's a multiple of 0.01)

### System Info
- Insomnia version: latest
- Platform: All platforms

---
Repository: /testbed
