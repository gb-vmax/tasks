# Bug Report

### Describe the bug

When importing OpenAPI 3 specs with number schemas that have `minimum`, `maximum`, or `multipleOf` constraints, the generated example values are always `0` regardless of the schema constraints. This makes the generated requests invalid when the constraints don't allow `0` as a valid value.

### Reproduction

```yaml
openapi: 3.0.0
paths:
  /api/example:
    post:
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                price:
                  type: number
                  minimum: 10
                  maximum: 100
                quantity:
                  type: number
                  multipleOf: 5
                  minimum: 5
```

When importing this spec, the generated example request body shows:
```json
{
  "price": 0,
  "quantity": 0
}
```

### Expected behavior

The generated examples should respect the schema constraints:
- `price` should be a value between 10 and 100 (e.g., `55` or `10`)
- `quantity` should be a multiple of 5 and at least 5 (e.g., `5`, `10`, `15`, etc.)

This is especially problematic when the API has validation that rejects values outside the specified ranges, making it impossible to test the endpoint without manually editing the generated values.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
