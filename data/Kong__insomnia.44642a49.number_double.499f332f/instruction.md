# Bug Report

### Describe the bug

When importing OpenAPI 3 specs with number/double type parameters that have constraints like `minimum`, `maximum`, `exclusiveMinimum`, `exclusiveMaximum`, or `multipleOf`, the generated example values are always `0.0` regardless of the schema constraints. This results in invalid example values that don't respect the schema definition.

### Reproduction

Import an OpenAPI 3 spec with a parameter defined like this:

```yaml
parameters:
  - name: price
    in: query
    schema:
      type: number
      format: double
      minimum: 10.0
      maximum: 100.0
      multipleOf: 5.0
```

The generated example value is `0.0`, which violates the `minimum: 10.0` constraint.

Another example:

```yaml
parameters:
  - name: temperature
    in: query
    schema:
      type: number
      format: double
      exclusiveMinimum: 0
      exclusiveMaximum: 100
```

Again, the example value is `0.0`, which violates the `exclusiveMinimum: 0` constraint (should be greater than 0).

### Expected behavior

The generated example values should respect the schema constraints:
- For `minimum: 10, maximum: 100`, should generate something like `55.0` (midpoint)
- For `multipleOf: 5`, should generate a value that's a multiple of 5
- For `exclusiveMinimum`/`exclusiveMaximum`, should generate values within the exclusive bounds

### System Info
- Insomnia version: latest
- Platform: All platforms

---
Repository: /testbed
