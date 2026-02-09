# Bug Report

### Describe the bug

I'm encountering an issue when importing OpenAPI 3.0 specs where string parameters are not being generated correctly. Instead of getting actual string values in the generated examples, I'm seeing function references or unexpected output.

### Reproduction

```yaml
openapi: 3.0.0
paths:
  /users:
    get:
      parameters:
        - name: username
          in: query
          schema:
            type: string
```

When importing this spec, the generated parameter example for `username` doesn't produce a proper string value. The parameter seems to have an incorrect value type instead of a simple string like "string".

### Expected behavior

The importer should generate a string value (e.g., "string") for basic string-type parameters in OpenAPI specs, similar to how it handles other types like email, date-time, etc.

### System Info
- Insomnia version: latest
- OS: N/A (affects all platforms)

---
Repository: /testbed
