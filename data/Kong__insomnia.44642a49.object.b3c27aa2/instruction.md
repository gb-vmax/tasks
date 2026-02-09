# Bug Report

### Describe the bug

When importing Swagger 2.0 specs with nested object parameters, the generated examples are returning the raw properties schema instead of the actual example object with property values. This results in incorrect request body examples being generated.

### Reproduction

```yaml
parameters:
  - in: body
    name: user
    schema:
      type: object
      properties:
        name:
          type: string
        address:
          type: object
          properties:
            street:
              type: string
            city:
              type: string
```

When importing this spec, the generated example for the `address` object shows the properties definition itself instead of an object with example values like:
```json
{
  "name": "",
  "address": {
    "street": "",
    "city": ""
  }
}
```

### Expected behavior

The importer should generate a proper example object with nested properties populated with their respective type defaults (empty strings, 0 for numbers, etc.), not return the properties schema definition.

### System Info
- Insomnia version: latest
- Platform: All platforms

---
Repository: /testbed
