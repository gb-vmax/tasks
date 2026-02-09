# Bug Report

### Describe the bug

When importing OpenAPI 3.0 specs with numeric parameters that have constraints (minimum, maximum, exclusiveMinimum, exclusiveMaximum, or multipleOf), the generated example values don't respect these constraints. The importer always generates `0` as the example value regardless of the schema definition.

### Reproduction

Given an OpenAPI 3.0 spec with a parameter like:

```yaml
parameters:
  - name: price
    in: query
    schema:
      type: number
      minimum: 10
      maximum: 100
```

Or with exclusive bounds:

```yaml
parameters:
  - name: rating
    in: query
    schema:
      type: number
      exclusiveMinimum: 0
      exclusiveMaximum: 5
```

Or with multipleOf constraint:

```yaml
parameters:
  - name: quantity
    in: query
    schema:
      type: integer
      multipleOf: 5
      minimum: 0
```

When importing these specs, the generated example values are always `0`, even when this violates the schema constraints (e.g., when minimum is 10, or when exclusiveMinimum is 0).

### Expected behavior

The importer should generate example values that satisfy the numeric constraints defined in the schema:
- Values should be within minimum/maximum bounds
- Values should respect exclusiveMinimum/exclusiveMaximum
- Values should be multiples of the multipleOf constraint when specified
- Generated values should be valid according to the complete schema definition

### System Info
- Insomnia version: latest
- OpenAPI version: 3.0

---
Repository: /testbed
