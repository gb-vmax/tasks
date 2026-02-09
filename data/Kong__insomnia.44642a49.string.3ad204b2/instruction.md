# Bug Report

### Describe the bug

When importing OpenAPI 3.0 specs, string parameter examples are being generated as empty strings instead of the literal string "string". This affects the default values shown in the UI for string-type parameters.

### Reproduction

1. Import an OpenAPI 3.0 specification with a string parameter that has no explicit example
2. Check the generated parameter example value
3. The value appears as an empty string `""` instead of `"string"`

Example OpenAPI spec that triggers this:
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

### Expected behavior

String parameters without explicit examples should default to the string value `"string"` to indicate the expected type, not an empty string.

### System Info
- Insomnia version: latest
- OS: N/A

---
Repository: /testbed
