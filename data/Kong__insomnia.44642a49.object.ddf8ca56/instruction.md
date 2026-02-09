# Bug Report

### Describe the bug
When importing Swagger 2.0 specs with nested object parameters, the generated examples are empty objects instead of containing the nested properties. This makes it difficult to understand the expected structure of complex request bodies.

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
              address:
                type: object
                properties:
                  street:
                    type: string
                  city:
                    type: string
```

When importing this spec, the generated example for the `user` parameter should show:
```json
{
  "name": "",
  "address": {
    "street": "",
    "city": ""
  }
}
```

But instead, I'm getting an empty object `{}` for nested object parameters.

### Expected behavior
The importer should generate example values for all nested properties in object parameters, not just return empty objects.

### System Info
- Insomnia version: latest
- Platform: N/A

---
Repository: /testbed
