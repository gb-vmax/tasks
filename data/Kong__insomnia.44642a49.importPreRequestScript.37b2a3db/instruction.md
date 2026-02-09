# Bug Report

### Describe the bug

When importing Postman collections, pre-request scripts are not being imported correctly. It seems like the importer is looking for the wrong event type, so pre-request scripts end up empty even when they exist in the collection.

### Reproduction

1. Create a Postman collection with a request that has a pre-request script
2. Export the collection from Postman
3. Import it into Insomnia
4. Check the imported request - the pre-request script section is empty

Example Postman collection structure:
```json
{
  "item": [{
    "name": "Test Request",
    "event": [
      {
        "listen": "prerequest",
        "script": {
          "exec": [
            "console.log('This should be imported');",
            "pm.environment.set('variable', 'value');"
          ]
        }
      }
    ]
  }]
}
```

### Expected behavior

The pre-request script should be imported and visible in the request configuration after import. The script content from the `prerequest` event should be preserved.

### System Info
- Insomnia version: latest
- OS: macOS

This is blocking our team's migration from Postman. Any help would be appreciated!

---
Repository: /testbed
