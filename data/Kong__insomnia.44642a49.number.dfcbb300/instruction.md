# Bug Report

### Describe the bug

When importing Swagger 2.0 specifications with number parameters that have `minimum`, `maximum`, or `multipleOf` constraints, the generated example values don't respect these constraints. The importer always generates `0` as the example value regardless of the parameter's validation rules.

### Reproduction

Given a Swagger 2.0 spec with a number parameter like this:

```yaml
parameters:
  - name: quantity
    in: query
    type: number
    minimum: 10
    maximum: 100
```

When importing this spec, the generated example value is `0`, which violates the `minimum: 10` constraint.

Similarly, for parameters with `multipleOf`:

```yaml
parameters:
  - name: price
    in: query
    type: number
    multipleOf: 5
    minimum: 20
```

The example should be a value that's a multiple of 5 and at least 20, but it generates `0` instead.

### Expected behavior

The importer should generate example values that respect the parameter constraints:
- If `minimum` is set, the example should be >= minimum
- If `maximum` is set, the example should be <= maximum  
- If `multipleOf` is set, the example should be a valid multiple
- Ideally, when both min and max are present, use a value in the middle of the range

### System Info
- Insomnia version: latest
- OS: N/A (affects all platforms)

---
Repository: /testbed
