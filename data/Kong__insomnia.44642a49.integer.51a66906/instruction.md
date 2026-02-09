# Bug Report

### Describe the bug

After importing a Swagger 2.0 specification, integer parameters with `minimum`, `maximum`, or `multipleOf` constraints are generating values that don't respect these constraints. The generated example values are sometimes outside the specified range or don't align with the `multipleOf` requirement.

### Reproduction

When importing a Swagger 2.0 spec with integer parameters like:

```yaml
parameters:
  - name: page
    in: query
    type: integer
    minimum: 1
    maximum: 100
    multipleOf: 5
```

The generated example value might be `0` or another value that doesn't satisfy the constraints. Expected behavior would be to generate a value between 1-100 that's a multiple of 5 (like 5, 10, 15, etc.).

Similarly, for parameters with only `minimum` or `maximum`:
```yaml
parameters:
  - name: count
    in: query
    type: integer
    minimum: 10
```

The generated value is `0`, which violates the minimum constraint.

### Expected behavior

Integer parameters should generate example values that:
- Fall within the `minimum` and `maximum` range when specified
- Are multiples of `multipleOf` when specified
- Respect all constraints simultaneously

### System Info
- Insomnia version: latest
- OS: N/A (affects all platforms)

---
Repository: /testbed
