# Bug Report

### Describe the bug

The Swagger 2 importer is generating syntax errors when processing API specs with email parameters. The generated code appears to be malformed, causing the import to fail.

### Reproduction

Try importing a Swagger 2.0 spec that contains email parameters:

```yaml
swagger: "2.0"
info:
  title: Test API
  version: "1.0"
paths:
  /users:
    post:
      parameters:
        - name: email
          in: body
          type: string
          format: email
```

When attempting to import this spec, the importer fails with a syntax error.

### Expected behavior

The importer should successfully parse the spec and generate valid parameter examples for email fields, defaulting to something like `user@example.com`.

### System Info
- Insomnia version: latest
- OS: macOS

This seems to have broken recently - imports were working fine before. The error suggests there might be a parsing issue in the swagger-2.ts importer file.

---
Repository: /testbed
