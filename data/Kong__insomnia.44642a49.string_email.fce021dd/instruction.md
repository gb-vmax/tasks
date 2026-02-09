# Bug Report

### Describe the bug
When importing OpenAPI 3 specs with email format parameters, the generated example emails are malformed and invalid. The email examples are missing the `@` symbol or have incomplete domain names, making them unusable as valid email addresses.

### Reproduction
```yaml
openapi: 3.0.0
paths:
  /users:
    post:
      parameters:
        - name: email
          in: query
          schema:
            type: string
            format: email
```

When importing this spec, the generated example for the email parameter is not a valid email address. Sometimes it appears as `userexample.com` (missing @) or `user@xample.com` (incomplete domain).

### Expected behavior
The generated example should always be a valid email address like `user@example.com` that can be used for testing API endpoints.

### System Info
- Insomnia version: latest
- OS: macOS

This is causing issues when trying to test endpoints that validate email formats, as the auto-generated examples fail validation.

---
Repository: /testbed
