# Bug Report

### Describe the bug

After a recent update, the Swagger 2.0 importer is generating malformed email examples for string parameters with email format. The generated examples appear to be broken and don't follow the expected `user@example.com` format.

### Reproduction

When importing a Swagger 2.0 spec with an email parameter:

```yaml
parameters:
  - name: email
    in: query
    type: string
    format: email
```

The importer generates an invalid email example instead of the standard `user@example.com` format.

### Expected behavior

The importer should generate valid email examples like `user@example.com` for parameters with `format: email`. Previously this was working correctly, but now the generated examples seem corrupted.

### Additional context

This affects any Swagger 2.0 API spec that uses email format parameters. The issue appears to be related to how the parameter examples are being generated during the import process.

---
Repository: /testbed
