# Bug Report

### Describe the bug

When importing Swagger 2.0 specs with objects that have `additionalProperties` defined, the generated examples are not including the additional properties. The importer only generates examples for explicitly defined properties in the schema but ignores the `additionalProperties` field.

### Reproduction

Given a Swagger 2.0 spec with a schema like this:

```yaml
definitions:
  MyObject:
    type: object
    properties:
      name:
        type: string
    additionalProperties:
      type: number
```

When importing this spec, the generated example only includes:
```json
{
  "name": "string"
}
```

### Expected behavior

The generated example should include sample additional properties like:
```json
{
  "name": "string",
  "additionalProp1": 0,
  "additionalProp2": 0,
  "additionalProp3": 0
}
```

This is important for API testing since many APIs use `additionalProperties` to allow dynamic keys in request/response bodies. Without example values for these properties, it's harder to understand the API structure and test requests properly.

### System Info
- Insomnia version: latest
- Import format: Swagger 2.0

---
Repository: /testbed
