# Bug Report

### Describe the bug

When importing Swagger 2.0 specifications, parameter examples for `number` type with `format: double` are not being generated correctly when constraints like `minimum`, `maximum`, `exclusiveMinimum`, `exclusiveMaximum`, or `multipleOf` are specified. The generated example values don't respect these constraints, which can lead to invalid request examples in the imported API collection.

### Reproduction

Import a Swagger 2.0 spec with a parameter defined like this:

```yaml
parameters:
  - name: price
    in: query
    type: number
    format: double
    minimum: 10.0
    maximum: 100.0
    multipleOf: 5.0
```

The generated example value should be a valid double that satisfies:
- Is between 10.0 and 100.0
- Is a multiple of 5.0

However, the importer always generates `0.0` as the example value, which violates the minimum constraint.

### Expected behavior

The importer should generate example values that respect all the numeric constraints defined in the Swagger spec:
- `minimum` / `maximum` bounds
- `exclusiveMinimum` / `exclusiveMaximum` flags
- `multipleOf` constraint

For the example above, valid generated values would be 10.0, 15.0, 20.0, etc. up to 100.0.

### System Info
- Insomnia version: latest
- OS: N/A (affects all platforms)

---
Repository: /testbed
