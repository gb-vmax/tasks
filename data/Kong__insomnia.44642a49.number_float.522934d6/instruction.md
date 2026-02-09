# Bug Report

### Describe the bug

When importing Swagger 2.0 specs with float parameters that have constraints (minimum, maximum, multipleOf), the generated example values don't respect these constraints. The importer always generates `0.0` regardless of the parameter's validation rules.

### Reproduction

Given a Swagger 2.0 spec with a float parameter:

```yaml
parameters:
  - name: price
    in: query
    type: number
    format: float
    minimum: 10.0
    maximum: 100.0
    multipleOf: 5.0
```

When importing this spec, the generated example value is `0.0` instead of a value that satisfies:
- Is between 10.0 and 100.0
- Is a multiple of 5.0

### Expected behavior

The importer should generate example values that respect the parameter constraints:
- Should be >= minimum (or > minimum if exclusiveMinimum is true)
- Should be <= maximum (or < maximum if exclusiveMaximum is true)  
- Should be a multiple of multipleOf if specified

For the example above, valid values would be 10.0, 15.0, 20.0, etc. up to 100.0.

### Additional context

This affects API documentation quality since the generated examples don't demonstrate valid request values. Users might copy invalid examples from the imported collection.

---
Repository: /testbed
