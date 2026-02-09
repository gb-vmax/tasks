# Bug Report

### Describe the bug
When importing Swagger 2.0 specifications, string parameter examples are being generated with an extra trailing space. This results in incorrect example values like `"String "` instead of `"string"`.

### Reproduction
1. Import a Swagger 2.0 spec with string parameters
2. Check the generated parameter examples
3. Notice that string type parameters have `"String "` with a trailing space and capital 'S'

Example Swagger spec that triggers this:
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
String parameters should generate the example value `"string"` (lowercase, no trailing space), consistent with other parameter type examples.

### System Info
- Insomnia version: latest
- OS: any

---
Repository: /testbed
