# Bug Report

### Describe the bug

I'm having trouble importing Postman environment files into Insomnia. When I try to import a valid Postman environment JSON file, the import seems to fail silently or doesn't import any variables at all.

### Reproduction

1. Export an environment from Postman (with `_postman_variable_scope` set to `"environment"`)
2. Try to import the file into Insomnia
3. The environment either doesn't get created or gets created with no variables

Example Postman environment file that fails to import:
```json
{
  "name": "My Environment",
  "_postman_variable_scope": "environment",
  "values": [
    {
      "key": "api_key",
      "value": "test123",
      "enabled": true
    },
    {
      "key": "base_url",
      "value": "https://api.example.com",
      "enabled": true
    }
  ]
}
```

### Expected behavior

The Postman environment should be imported successfully with all enabled variables available in Insomnia. Disabled variables should be excluded from the import.

### Additional context

This used to work in previous versions. I'm not sure if this is related to recent changes in the Postman environment format or if something changed in the importer logic.

---
Repository: /testbed
