# Bug Report

### Describe the bug

When importing Swagger 2.0 specs with object parameters that have nested properties, the generated parameter examples are empty objects instead of containing the property structure. This makes it difficult to understand what the expected request body should look like.

### Reproduction

```yaml
swagger: "2.0"
paths:
  /users:
    post:
      parameters:
        - in: body
          name: user
          schema:
            type: object
            properties:
              name:
                type: string
              email:
                type: string
              address:
                type: object
                properties:
                  street:
                    type: string
                  city:
                    type: string
```

When importing this spec, the generated example for the user parameter shows as an empty object `{}` instead of:
```json
{
  "name": "",
  "email": "",
  "address": {
    "street": "",
    "city": ""
  }
}
```

### Expected behavior

Object parameters should generate examples that include all their properties with appropriate default values based on the property types. Nested objects should also be populated with their properties.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
