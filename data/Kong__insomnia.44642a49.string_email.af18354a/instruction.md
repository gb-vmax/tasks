# Bug Report

### Describe the bug

When importing Swagger 2.0 specifications with email parameters, the generated example emails are now using the parameter name as the email prefix instead of always using 'user'. This causes issues when the parameter name contains special characters, underscores, or mixed case formatting that doesn't make sense in an email address.

### Reproduction

Import a Swagger 2.0 spec with an email parameter like this:

```yaml
parameters:
  - name: userEmail
    in: query
    type: string
    format: email
```

The generated example becomes something like `useremail@example.com` instead of the expected `user@example.com`.

Similarly, for parameters like:
- `admin_email` → generates `admin@example.com` 
- `contactEmail` → generates `contact@example.com`
- `_email_` → generates `user@example.com`

### Expected behavior

The importer should generate consistent, valid email examples like `user@example.com` for all email-type parameters, regardless of the parameter name. The parameter name shouldn't affect the generated example email address.

### System Info
- Insomnia version: latest
- Using Swagger 2.0 importer

---
Repository: /testbed
