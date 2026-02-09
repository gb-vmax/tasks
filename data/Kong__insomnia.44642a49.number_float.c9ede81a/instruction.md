# Bug Report

### Describe the bug

When importing Swagger 2.0 specs with number parameters that have `format: float`, the generated example values don't respect the `minimum`, `maximum`, `exclusiveMinimum`, and `exclusiveMaximum` constraints defined in the parameter schema. The importer always generates `0.0` as the example value regardless of the constraints.

### Reproduction

Import a Swagger 2.0 spec with a float parameter like this:

```yaml
parameters:
  - name: temperature
    in: query
    type: number
    format: float
    minimum: 10.0
    maximum: 100.0
    exclusiveMinimum: true
```

The generated request will use `0.0` as the example value, which violates the `minimum: 10.0` constraint.

### Expected behavior

The importer should generate example values that respect the defined constraints. For the above parameter, it should generate a value between 10.0 (exclusive) and 100.0, such as `10.01` or `55.0`.

Similarly, when only `maximum` is defined, it should generate a value less than or equal to the maximum. When only `minimum` is defined, it should generate a value greater than or equal to the minimum.

### System Info
- Insomnia version: latest
- Import format: Swagger 2.0

---
Repository: /testbed
