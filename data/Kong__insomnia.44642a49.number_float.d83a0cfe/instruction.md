# Bug Report

### Describe the bug

When importing Swagger 2.0 specs, the generated example values for `number` type parameters with `format: float` are not respecting the `minimum`, `maximum`, `exclusiveMinimum`, `exclusiveMaximum`, and `multipleOf` constraints defined in the parameter schema.

### Reproduction

Given a Swagger 2.0 specification with a parameter like:

```yaml
parameters:
  - name: price
    in: query
    type: number
    format: float
    minimum: 10.0
    maximum: 50.0
    multipleOf: 5.0
```

When importing this spec into Insomnia, the generated example value is always `0.0`, which violates the minimum constraint of `10.0` and doesn't respect the `multipleOf: 5.0` constraint.

### Expected behavior

The importer should generate example values that:
- Fall within the specified min/max range
- Respect `exclusiveMinimum` and `exclusiveMaximum` flags when present
- Are multiples of the `multipleOf` value when specified

For the example above, valid generated values would be `10.0`, `15.0`, `20.0`, etc. up to `50.0`.

### Additional context

This only affects `number` parameters with `format: float`. Other numeric types may have similar issues but I haven't tested them extensively.

---
Repository: /testbed
