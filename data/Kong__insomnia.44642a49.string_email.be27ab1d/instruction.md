# Bug Report

### Describe the bug

When generating example values for OpenAPI 3 email parameters, the importer is producing inconsistent and unexpected email addresses. Instead of the standard `user@example.com` format, I'm getting different email addresses with varying domains and usernames that seem to change based on context.

### Reproduction

Import an OpenAPI 3 specification with email format parameters:

```yaml
parameters:
  - name: userEmail
    in: query
    schema:
      type: string
      format: email
  - name: contactEmail
    in: query
    schema:
      type: string
      format: email
```

The generated example values are not consistent - sometimes I get `user@example.com`, other times `user@test.com`, `contactemail@demo.com`, or other variations. The behavior seems unpredictable.

### Expected behavior

Email parameters should consistently generate the same example value (e.g., `user@example.com`) for predictable and reliable API documentation and testing.

### Additional context

This appears to have changed recently. Previously, email examples were always `user@example.com` which was simple and worked well. The new behavior makes it harder to work with imported specs since the examples keep changing.

---
Repository: /testbed
