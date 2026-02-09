# Bug Report

### Describe the bug

I'm having an issue importing Postman environment files into Insomnia. When I try to import a valid Postman environment JSON file, it's being rejected and returning null instead of creating the environment.

### Reproduction

1. Export an environment from Postman (standard environment, not globals)
2. Try to import the exported JSON file into Insomnia
3. The import fails silently - no environment is created

Here's a sample of the Postman environment JSON structure I'm trying to import:

```json
{
  "_postman_variable_scope": "environment",
  "name": "My Test Environment",
  "values": [
    {
      "key": "api_url",
      "value": "https://api.example.com",
      "enabled": true
    },
    {
      "key": "api_key",
      "value": "secret123",
      "enabled": true
    }
  ]
}
```

### Expected behavior

The Postman environment should be imported successfully and create a new environment in Insomnia with all the enabled variables.

### Additional context

This used to work in previous versions. I'm not sure if the Postman export format changed or if something broke in the importer. Also noticed that disabled variables in Postman might not be getting filtered correctly during import.

---
Repository: /testbed
