# Bug Report

### Describe the bug

When importing OpenAPI 3 specs with integer parameters that have `minimum`, `maximum`, `exclusiveMinimum`, or `exclusiveMaximum` constraints, the generated example values don't respect these boundaries. All integer parameters are currently generated with a value of `0`, regardless of the schema constraints.

### Reproduction

```yaml
openapi: 3.0.0
paths:
  /items:
    get:
      parameters:
        - name: page
          in: query
          schema:
            type: integer
            minimum: 1
        - name: limit
          in: query
          schema:
            type: integer
            minimum: 10
            maximum: 100
        - name: offset
          in: query
          schema:
            type: integer
            exclusiveMinimum: 0
```

When importing this spec, all the integer parameters get example value `0`, even though:
- `page` should be at least `1`
- `limit` should be between `10` and `100`
- `offset` should be greater than `0`

### Expected behavior

The importer should generate example values that respect the integer constraints defined in the OpenAPI schema:
- When `minimum` is set, the example should be >= minimum
- When `maximum` is set, the example should be <= maximum
- When `exclusiveMinimum` is set, the example should be > exclusiveMinimum
- When `exclusiveMaximum` is set, the example should be < exclusiveMaximum
- When `enum` is provided, the example should use one of the enum values

### System Info
- Insomnia version: latest
- Platform: All

---
Repository: /testbed
