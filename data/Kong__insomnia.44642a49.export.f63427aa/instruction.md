# Bug Report

### Describe the bug

When importing Postman environment files, variable keys with special characters or that start with numbers are being modified, but the original key names are lost. This breaks references to those variables in requests that use the original naming.

### Reproduction

1. Create a Postman environment with variables that have special characters or start with numbers:
```json
{
  "_postman_variable_scope": "environment",
  "name": "Test Environment",
  "values": [
    {
      "key": "api-key",
      "value": "12345",
      "enabled": true
    },
    {
      "key": "123variable",
      "value": "test",
      "enabled": true
    },
    {
      "key": "my.special.var",
      "value": "value",
      "enabled": true
    }
  ]
}
```

2. Import this environment into Insomnia

3. Check the imported variable names - they've been changed to `api_key`, `_123variable`, `my_special_var`

4. Any requests that reference `{{api-key}}` or `{{my.special.var}}` no longer work because the variable names have changed

### Expected behavior

The importer should preserve the original variable key names from Postman, or at least provide a warning/mapping when keys are modified. Currently there's no indication that the variable names have been changed, which causes silent failures in imported requests.

### System Info
- Insomnia version: latest
- OS: macOS

This is particularly problematic when migrating from Postman collections that heavily use special characters in variable names.

---
Repository: /testbed
