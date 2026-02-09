# Bug Report

### Describe the bug
When importing Postman environment files, disabled variables are being imported instead of enabled ones. The importer seems to be inverting the logic for which variables should be included in the imported environment.

### Reproduction
1. Create a Postman environment file with both enabled and disabled variables
2. Import the environment file into Insomnia
3. Only the disabled variables are imported, while enabled variables are skipped

Example Postman environment JSON:
```json
{
  "_postman_variable_scope": "environment",
  "name": "My Environment",
  "values": [
    {
      "key": "api_url",
      "value": "https://api.example.com",
      "enabled": true
    },
    {
      "key": "debug_mode",
      "value": "false",
      "enabled": false
    }
  ]
}
```

### Expected behavior
Only enabled variables should be imported. In the example above, `api_url` should be imported while `debug_mode` should be skipped.

### Actual behavior
The opposite happens - disabled variables are imported while enabled ones are ignored.

---
Repository: /testbed
