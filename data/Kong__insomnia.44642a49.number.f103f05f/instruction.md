# Bug Report

### Describe the bug

When importing OpenAPI 3 specs with numeric parameters that have constraints (minimum, maximum, exclusiveMinimum, exclusiveMaximum, multipleOf), the generated example values don't respect these constraints. The importer always generates `0` as the example value regardless of the schema validation rules.

### Reproduction

Given an OpenAPI 3 spec with a numeric parameter like this:

```yaml
parameters:
  - name: page
    in: query
    schema:
      type: number
      minimum: 1
      maximum: 100
```

When importing this spec, the generated example value is `0`, which violates the `minimum: 1` constraint.

Another example with `multipleOf`:

```yaml
parameters:
  - name: quantity
    in: query
    schema:
      type: number
      multipleOf: 5
      minimum: 10
```

The generated example should be a multiple of 5 that's at least 10 (e.g., 10, 15, 20...), but instead it generates `0`.

### Expected behavior

The importer should generate example values that satisfy all numeric constraints:
- Values should be >= minimum (or > exclusiveMinimum)
- Values should be <= maximum (or < exclusiveMaximum)  
- Values should be multiples of `multipleOf` when specified
- When both min and max are present, pick a value in between

For the examples above:
- First case: should generate something like `50` (between 1 and 100)
- Second case: should generate `10` or `15` (multiple of 5, >= 10)

### System Info
- Insomnia version: latest
- OS: N/A (importer issue)

---
Repository: /testbed
