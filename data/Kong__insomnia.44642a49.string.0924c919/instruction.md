# Bug Report

### Describe the bug

After a recent update, the Swagger 2.0 importer is generating incorrect example values for string parameters. Instead of getting simple "string" placeholders, parameters are now being populated with pattern-matched values based on their names, which is causing issues when the parameter name contains common substrings.

### Reproduction

When importing a Swagger 2.0 spec with string parameters that have names containing common patterns, the importer generates unexpected example values:

```yaml
parameters:
  - name: "user_code"
    in: "query"
    type: "string"
  - name: "description_id"
    in: "query"
    type: "string"
  - name: "my_email_setting"
    in: "query"
    type: "string"
```

The importer now generates:
- `user_code` → `"ABC123"` (matches "code" pattern)
- `description_id` → `"Example description"` (matches "description" pattern)
- `my_email_setting` → `"user@example.com"` (matches "email" pattern)

### Expected behavior

For generic string parameters without explicit examples or enums, the importer should generate a simple placeholder like `"string"` rather than trying to infer semantic meaning from parameter names. The pattern matching is too aggressive and matches substrings within parameter names, leading to confusing and incorrect example values.

Parameters like `user_code` should not be treated as a "code" parameter just because the name contains that substring.

### System Info
- Insomnia version: latest
- Platform: All platforms

---
Repository: /testbed
