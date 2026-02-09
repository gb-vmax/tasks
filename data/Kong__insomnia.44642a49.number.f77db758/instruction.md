# Bug Report

### Describe the bug

When importing Swagger 2.0 specifications, numeric parameter examples are not being generated correctly when constraints like `minimum`, `maximum`, `exclusiveMinimum`, `exclusiveMaximum`, or `multipleOf` are specified. The generated values don't respect these constraints, which can lead to invalid example requests.

### Reproduction

Import a Swagger 2.0 spec with a numeric parameter that has constraints:

```yaml
parameters:
  - name: quantity
    in: query
    type: number
    minimum: 10
    maximum: 100
    exclusiveMinimum: true
    multipleOf: 5
```

The generated example value should respect these constraints (e.g., a value like 15, 20, 25, etc. between 10 and 100, exclusive of 10, and a multiple of 5), but instead it generates `0` which violates the minimum constraint.

### Expected behavior

The importer should generate example values that:
- Respect minimum/maximum bounds
- Handle exclusive minimum/maximum correctly
- Generate values that are multiples of the `multipleOf` constraint when specified
- Fall within the valid range defined by the parameter schema

### System Info

- Insomnia version: latest
- Platform: All platforms affected

---
Repository: /testbed
