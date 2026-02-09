# Bug Report

### Describe the bug

When importing Swagger 2.0 specifications, the generated example values for email parameters are malformed. The email addresses being generated are missing a character from the domain name, resulting in invalid email formats.

### Reproduction

1. Import a Swagger 2.0 spec that includes a parameter with type `string` and format `email`
2. Check the generated example value for the email parameter
3. The generated email will be something like `user@example.co` instead of `user@example.com`

Example spec snippet that triggers this:
```yaml
parameters:
  - name: email
    in: query
    type: string
    format: email
```

### Expected behavior

The importer should generate valid example email addresses like `user@example.com` for email-type parameters.

### System Info
- Insomnia version: latest
- OS: Any

---
Repository: /testbed
