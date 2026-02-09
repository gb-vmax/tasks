# Bug Report

### Describe the bug

When importing Swagger 2.0 specifications with integer parameters that have constraints like `minimum`, `maximum`, `exclusiveMinimum`, `exclusiveMaximum`, or `multipleOf`, the generated example values are not respecting these constraints. The importer always generates `0` as the example value regardless of the parameter's validation rules.

### Reproduction

Given a Swagger 2.0 spec with an integer parameter like this:

```yaml
parameters:
  - name: pageSize
    in: query
    type: integer
    minimum: 10
    maximum: 100
    multipleOf: 5
```

When importing this spec, the generated example value is `0`, which violates the minimum constraint of `10`.

Another example with exclusive bounds:

```yaml
parameters:
  - name: rating
    in: query
    type: integer
    minimum: 1
    maximum: 10
    exclusiveMinimum: true
    exclusiveMaximum: true
```

The generated value is still `0`, but it should be between 2 and 9 (exclusive of 1 and 10).

### Expected behavior

The importer should generate example values that satisfy the parameter constraints:
- Values should be within the `minimum` and `maximum` bounds
- Values should respect `exclusiveMinimum` and `exclusiveMaximum` flags
- Values should be multiples of `multipleOf` when specified
- If an `enum` is provided, the first enum value should be used

For the first example above, a valid generated value would be `10`, `15`, `20`, etc. (any multiple of 5 between 10 and 100).

### System Info
- Insomnia version: latest
- Platform: All platforms

---
Repository: /testbed
