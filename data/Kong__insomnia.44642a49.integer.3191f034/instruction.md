# Bug Report

### Describe the bug

When importing Swagger 2.0 specs with integer parameters that have validation constraints (`minimum`, `maximum`, `exclusiveMinimum`, `exclusiveMaximum`, `multipleOf`), the generated example values don't respect these constraints. The importer always generates `0` as the example value regardless of whether it's valid according to the parameter's schema.

### Reproduction

Import a Swagger 2.0 spec with an integer parameter like this:

```yaml
parameters:
  - name: page
    in: query
    type: integer
    minimum: 1
    maximum: 100
```

The generated example value is `0`, which violates the `minimum: 1` constraint.

Another example with `multipleOf`:

```yaml
parameters:
  - name: offset
    in: query
    type: integer
    minimum: 10
    maximum: 50
    multipleOf: 5
```

Expected example: `10` (or `15`, `20`, etc.)
Actual example: `0`

### Expected behavior

The importer should generate example values that satisfy the parameter's validation rules:
- Respect `minimum` and `maximum` bounds
- Handle `exclusiveMinimum` and `exclusiveMaximum` correctly
- Generate values that are multiples of `multipleOf` when specified
- Fall back to the minimum value when it exists and is valid

### System Info
- Insomnia version: latest
- Platform: All

---
Repository: /testbed
