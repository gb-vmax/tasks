# Bug Report

### Describe the bug

When importing Swagger 2.0 specs with email parameters, the generated example emails have malformed domains. The domain parts appear to be reversed (e.g., `com.example` instead of `example.com`), resulting in invalid email addresses.

### Reproduction

```yaml
# swagger.yaml
swagger: "2.0"
paths:
  /users:
    post:
      parameters:
        - name: email
          in: formData
          type: string
          format: email
```

Import this spec and check the generated example for the email parameter. The domain will be reversed like `user@com.example` instead of `user@example.com`.

### Expected behavior

The generated email examples should have properly formatted domains (e.g., `user@example.com`, `user@gmail.com`, etc.) that are valid email addresses.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
