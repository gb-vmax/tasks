# Bug Report

### Describe the bug

When importing OpenAPI 3.0 specs with integer parameters that have constraints (minimum, maximum, multipleOf), the generated example values don't respect these constraints. The importer always generates `0` as the example value regardless of the schema's validation rules.

### Reproduction

Given an OpenAPI 3.0 spec with an integer parameter like:

```yaml
parameters:
  - name: page
    in: query
    schema:
      type: integer
      minimum: 1
      maximum: 100
      multipleOf: 5
```

When importing this spec, the generated example value is `0`, which violates the minimum constraint (should be >= 1) and the multipleOf constraint (should be divisible by 5).

Similarly, for a parameter with:
```yaml
schema:
  type: integer
  minimum: 10
```

The generated example is still `0` instead of a valid value like `10`.

### Expected behavior

The importer should generate example values that satisfy the schema constraints:
- Respect `minimum` and `maximum` bounds
- Honor `exclusiveMinimum` and `exclusiveMaximum` flags
- Generate values that are multiples of `multipleOf` when specified
- Use enum values when available

For the first example above, a valid generated value could be `5`, `10`, `15`, etc. (any multiple of 5 between 1 and 100).

### System Info
- Insomnia version: latest
- Platform: All platforms

---
Repository: /testbed
