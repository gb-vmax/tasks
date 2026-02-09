# Bug Report

### Describe the bug

When importing OpenAPI 3 specs with numeric parameters that have `multipleOf`, `minimum`, or `maximum` constraints, the generated example values don't respect these constraints. The importer always generates `0.0` for number/double types regardless of the schema validation rules.

### Reproduction

Given an OpenAPI 3 spec with a parameter like:

```yaml
parameters:
  - name: price
    in: query
    schema:
      type: number
      format: double
      minimum: 5.0
      maximum: 100.0
      multipleOf: 2.5
```

When importing this spec, the generated example value is `0.0`, which violates the `minimum: 5.0` constraint.

### Expected behavior

The importer should generate example values that satisfy the schema constraints:
- Should respect `minimum` and `maximum` bounds
- Should respect `exclusiveMinimum` and `exclusiveMaximum` if present
- Should generate values that are valid multiples when `multipleOf` is specified

For the example above, a valid generated value could be `5.0`, `7.5`, `10.0`, etc. - any multiple of 2.5 between 5.0 and 100.0.

### System Info
- Insomnia version: latest
- OS: N/A (importer issue)

---
Repository: /testbed
