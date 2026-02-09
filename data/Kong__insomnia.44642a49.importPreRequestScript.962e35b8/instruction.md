# Bug Report

### Describe the bug

When importing Postman collections that have pre-request scripts with disabled events, the scripts are still being imported and executed. According to Postman's behavior, disabled pre-request scripts should be ignored during import.

### Reproduction

1. Create a Postman collection with a pre-request script
2. Disable the pre-request script event in Postman (set `disabled: true`)
3. Export the collection
4. Import the collection into Insomnia

The disabled pre-request script is imported and will execute, even though it should be skipped.

Example of a Postman collection structure with a disabled event:
```json
{
  "event": [
    {
      "listen": "prerequest",
      "disabled": true,
      "script": {
        "exec": [
          "console.log('This should not run');"
        ]
      }
    }
  ]
}
```

### Expected behavior

Disabled pre-request scripts should not be imported. The importer should check the `disabled` property on events and skip them if set to `true`, matching Postman's behavior.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
