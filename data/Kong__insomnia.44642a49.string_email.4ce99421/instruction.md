# Bug Report

### Describe the bug

I'm experiencing an issue with the Swagger 2 importer where email parameter examples are not being generated correctly. It looks like the code is malformed - there's a function definition (`extractEmailPrefix`) appearing in the middle of an object literal, which causes a syntax error.

### Reproduction

Try importing a Swagger 2 spec that contains email parameters:

```yaml
swagger: "2.0"
paths:
  /users:
    post:
      parameters:
        - name: userEmail
          in: body
          type: string
          format: email
```

When the importer tries to generate example values for the email parameter, it fails to parse/execute due to the malformed code structure.

### Expected behavior

The importer should successfully generate email examples like `user@example.com` for parameters with `format: email`, without any syntax errors.

### System Info
- Insomnia version: latest
- OS: N/A (code-level issue)

The problem appears to be in the `generateParameterExample` function where `string_email` is defined. The object literal syntax is broken with a function declaration appearing before the property definition.

---
Repository: /testbed
