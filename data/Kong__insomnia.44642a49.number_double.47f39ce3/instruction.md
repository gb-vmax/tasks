# Bug Report

### Describe the bug
When importing OpenAPI 3 specs with number/double type parameters that have constraints like `minimum`, `maximum`, `exclusiveMinimum`, `exclusiveMaximum`, or `multipleOf`, the generated example values don't respect these constraints. The importer always generates `0.0` as the example value regardless of the schema constraints.

### Reproduction
```yaml
openapi: 3.0.0
paths:
  /example:
    get:
      parameters:
        - name: price
          in: query
          schema:
            type: number
            format: double
            minimum: 10.0
            maximum: 100.0
```

When importing this spec, the generated example for the `price` parameter is `0.0`, which violates the minimum constraint of `10.0`.

Similar issues occur with:
- `exclusiveMinimum` / `exclusiveMaximum` - example should be within the exclusive range
- `multipleOf` - example should be a valid multiple of the specified value
- Combination of constraints - example should satisfy all constraints simultaneously

### Expected behavior
The generated example values should respect the schema constraints:
- For `minimum`/`maximum`: generate a value within the range (e.g., midpoint)
- For `exclusiveMinimum`/`exclusiveMaximum`: generate a value within the exclusive range
- For `multipleOf`: generate a value that is a valid multiple
- When multiple constraints exist: generate a value that satisfies all of them

### System Info
- Insomnia version: latest
- Import format: OpenAPI 3.0

---
Repository: /testbed
