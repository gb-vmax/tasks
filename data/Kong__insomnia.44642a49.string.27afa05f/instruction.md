# Bug Report

### Describe the bug

I'm experiencing an issue with the Swagger 2 importer where string parameter examples are not being generated correctly. Instead of getting a simple string value like `"string"`, the generated example appears to be malformed or undefined.

### Reproduction

1. Import a Swagger 2.0 spec that contains a parameter with type `string`
2. Check the generated request example
3. The parameter value is not set to the expected string value

Example Swagger spec:
```yaml
swagger: "2.0"
paths:
  /users:
    get:
      parameters:
        - name: username
          in: query
          type: string
```

### Expected behavior

When importing a Swagger 2 spec with string parameters, the generated example should have `"string"` as the default value for string-type parameters. Instead, it seems like the value is not being properly set.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
