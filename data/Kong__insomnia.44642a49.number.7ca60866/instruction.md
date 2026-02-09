# Bug Report

### Describe the bug

When importing OpenAPI 3 specs with numeric parameters that have constraints (minimum, maximum, multipleOf, exclusiveMinimum, exclusiveMaximum), the generated example values don't respect these constraints. All numbers are generated as `0` regardless of the schema definition.

### Reproduction

Given an OpenAPI 3 spec with a parameter like:

```yaml
parameters:
  - name: quantity
    in: query
    schema:
      type: number
      minimum: 10
      maximum: 100
      multipleOf: 5
```

When importing this spec, the generated example value is `0` instead of a value that satisfies the constraints (e.g., `10`, `55`, etc.).

Similarly, for exclusive constraints:

```yaml
parameters:
  - name: price
    in: query
    schema:
      type: number
      minimum: 0
      exclusiveMinimum: true
      maximum: 1000
```

The generated example is still `0`, which violates the `exclusiveMinimum` constraint.

### Expected behavior

The importer should generate example values that respect the numeric constraints defined in the schema:
- Values should be >= minimum (or > minimum if exclusiveMinimum is true)
- Values should be <= maximum (or < maximum if exclusiveMaximum is true)  
- Values should be multiples of multipleOf when specified
- When only minimum is specified, use the minimum value
- When both minimum and maximum are specified, use a value in the middle of the range

### System Info
- Insomnia version: latest
- OS: N/A

---
Repository: /testbed
