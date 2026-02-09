# Bug Report

### Describe the bug

When importing OpenAPI 3 specs with float/number parameters that have range constraints (minimum, maximum, exclusiveMinimum, exclusiveMaximum), the generated example values are not respecting these constraints. The importer always generates `0.0` as the example value regardless of the specified range.

### Reproduction

```yaml
openapi: 3.0.0
paths:
  /test:
    get:
      parameters:
        - name: temperature
          in: query
          schema:
            type: number
            format: float
            minimum: 10.0
            maximum: 100.0
```

When importing this spec, the generated example for the `temperature` parameter is `0.0`, which is outside the valid range of 10.0-100.0.

### Expected behavior

The importer should generate example values that fall within the specified constraints:
- For `minimum: 10.0, maximum: 100.0`, it should generate something like `55.0` (midpoint)
- For `exclusiveMinimum: 0.0, exclusiveMaximum: 1.0`, it should generate a value between 0 and 1 (exclusive)
- If `example` or `default` is provided in the schema, those should be used instead

### Additional context

This affects API specs where parameter validation is strict and example values need to be within valid ranges. The current behavior can be confusing when testing imported endpoints since the default examples fail validation.

---
Repository: /testbed
