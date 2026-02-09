# Bug Report

### Describe the bug

I'm experiencing an issue with Postman environment imports where variable references using the `{{variable}}` syntax are not being resolved. When importing a Postman environment that contains variables referencing other variables, the raw `{{variable_name}}` placeholders remain in the imported data instead of being replaced with their actual values.

### Reproduction

When importing a Postman environment JSON with variable references like:

```json
{
  "name": "My Environment",
  "_postman_variable_scope": "environment",
  "values": [
    {
      "key": "base_url",
      "value": "https://api.example.com",
      "enabled": true
    },
    {
      "key": "full_endpoint",
      "value": "{{base_url}}/users",
      "enabled": true
    }
  ]
}
```

The imported environment should have `full_endpoint` set to `https://api.example.com/users`, but instead it keeps the literal value `{{base_url}}/users`.

### Expected behavior

Variable references should be resolved during import so that:
- Variables containing `{{other_variable}}` syntax get replaced with the actual values
- Nested variable references are properly resolved
- The final imported environment contains the fully resolved values

### Additional context

This affects workflows where Postman environments use variable composition to build up URLs, tokens, or other configuration values from base components. Without resolution, these references need to be manually fixed after import.

---
Repository: /testbed
