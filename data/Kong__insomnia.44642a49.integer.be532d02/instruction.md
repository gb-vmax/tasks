# Bug Report

### Describe the bug
When importing an OpenAPI 3 specification with integer parameters, the generated example values are incorrect. Instead of getting a numeric value like `0`, the parameter examples are being set to empty objects `{}`.

### Reproduction
```yaml
openapi: 3.0.0
paths:
  /users/{userId}:
    get:
      parameters:
        - name: userId
          in: path
          required: true
          schema:
            type: integer
```

After importing this spec, the generated request shows `userId` with an empty object value instead of a numeric placeholder like `0`.

### Expected behavior
Integer type parameters should generate numeric example values (e.g., `0`) that can be used as valid placeholders in the request.

### System Info
- Insomnia version: latest
- Import format: OpenAPI 3.0

This is causing issues when testing APIs that require integer parameters, as the generated examples are not valid integers and need to be manually corrected every time.

---
Repository: /testbed
