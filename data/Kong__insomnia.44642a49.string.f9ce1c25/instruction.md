# Bug Report

### Describe the bug

When importing OpenAPI 3.0 specs, string parameter examples are not being generated correctly. The importer appears to be producing malformed or invalid string examples that don't follow the expected format.

### Reproduction

```yaml
openapi: 3.0.0
paths:
  /users:
    get:
      parameters:
        - name: userId
          in: query
          schema:
            type: string
            minLength: 5
            maxLength: 10
```

When importing this spec, the generated example string doesn't respect the constraints properly. Expected to see a string example that meets the length requirements, but instead getting unexpected output.

### Expected behavior

The importer should generate valid string examples that:
- Respect minLength and maxLength constraints when specified
- Use contextual examples based on parameter names (e.g., "email" parameters should generate email-like strings)
- Fall back to a sensible default when no context is available

### System Info
- Insomnia version: latest
- OS: macOS

This seems to have broken recently, possibly after changes to the OpenAPI 3 importer. The string generation logic doesn't seem to be working as intended.

---
Repository: /testbed
