# Bug Report

### Describe the bug

The Swagger 2.0 importer is generating invalid syntax when processing parameters with `number_double` type. The code appears to have malformed structure that breaks the parameter example generation.

### Reproduction

1. Import a Swagger 2.0 specification that contains a parameter with type `number` and format `double`
2. The importer fails to process the specification correctly
3. Parameter examples are not generated as expected

Example Swagger spec that triggers the issue:
```yaml
swagger: "2.0"
paths:
  /test:
    get:
      parameters:
        - name: value
          in: query
          type: number
          format: double
          minimum: 0
          maximum: 100
```

### Expected behavior

The importer should successfully parse the Swagger specification and generate appropriate example values for `number_double` type parameters, respecting constraints like minimum, maximum, and multipleOf.

### Additional context

This seems to affect any Swagger 2.0 spec that uses double-precision floating point parameters. The parameter example generation logic appears to be broken for this specific type.

---
Repository: /testbed
