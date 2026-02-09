# Bug Report

### Describe the bug

After a recent update, the Swagger 2 importer is generating invalid syntax when processing email format parameters. The generated code appears to have malformed structure that breaks the parameter example generation.

### Reproduction

When importing a Swagger 2.0 specification with email format parameters, the import process fails or produces corrupted output.

Example spec that triggers the issue:
```yaml
swagger: "2.0"
paths:
  /users:
    post:
      parameters:
        - name: email
          in: body
          type: string
          format: email
          description: User email address
```

### Expected behavior

The importer should successfully process the specification and generate valid parameter examples for email fields, similar to how it worked in previous versions (e.g., `user@example.com`).

### System Info
- Insomnia version: latest
- Import format: Swagger 2.0 / OpenAPI 2.0

The issue seems related to the parameter example generation logic for email fields. The importer worked fine before the recent changes.

---
Repository: /testbed
