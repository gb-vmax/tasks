# Bug Report

### Describe the bug

When importing OpenAPI 3 specs with number parameters that have `multipleOf` constraints, the generated example values don't respect the `multipleOf` property. This results in invalid example values that don't match the schema constraints.

### Reproduction

```yaml
openapi: 3.0.0
paths:
  /example:
    get:
      parameters:
        - name: quantity
          in: query
          schema:
            type: number
            format: double
            multipleOf: 5
            minimum: 10
            maximum: 100
```

When importing this spec, the generated example value for the `quantity` parameter is not a multiple of 5, even though the schema explicitly requires it.

### Expected behavior

The importer should generate example values that satisfy all schema constraints, including `multipleOf`. For the above example, a valid value would be 10, 15, 20, etc. - any number between 10 and 100 that's a multiple of 5.

### Additional context

This affects API testing workflows since the auto-generated examples may not be valid according to the API specification, requiring manual adjustment of parameter values before sending requests.

---
Repository: /testbed
