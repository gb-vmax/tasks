# Bug Report

### Describe the bug

When importing OpenAPI 3.0 specs, the generated example values for number parameters don't respect the schema constraints. Numbers with `minimum`, `maximum`, `exclusiveMinimum`, `exclusiveMaximum`, or `multipleOf` constraints are being generated as `0` regardless of the constraints, which can produce invalid examples.

### Reproduction

Given an OpenAPI spec with a number parameter like this:

```yaml
parameters:
  - name: price
    in: query
    schema:
      type: number
      minimum: 10
      maximum: 100
      multipleOf: 5
```

When importing this spec, the generated example value is `0`, which violates the `minimum: 10` constraint.

Similarly, for a spec with exclusive bounds:

```yaml
parameters:
  - name: percentage
    in: query
    schema:
      type: number
      exclusiveMinimum: 0
      exclusiveMaximum: 100
```

The generated example is still `0`, which violates the `exclusiveMinimum: 0` constraint (value must be greater than 0).

### Expected behavior

The importer should generate example values that satisfy all numeric constraints:
- Values should be within `minimum` and `maximum` bounds
- Values should respect `exclusiveMinimum` and `exclusiveMaximum` 
- Values should be multiples of `multipleOf` when specified
- For the first example above, a valid value would be `55` (within 10-100 and multiple of 5)
- For the second example, a valid value would be something like `50` (greater than 0 and less than 100)

### System Info
- Insomnia version: latest
- Platform: All platforms

---
Repository: /testbed
