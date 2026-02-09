# Bug Report

### Describe the bug

When importing Postman collections, pre-request scripts are not being imported correctly. The scripts that should run before a request is sent are completely missing or empty in the imported collection, even though they exist in the original Postman collection.

### Reproduction

1. Export a Postman collection that contains pre-request scripts
2. Import the collection into Insomnia
3. Check the imported requests - the pre-request scripts are missing

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
            "pm.environment.set('timestamp', Date.now());",
            "console.log('Pre-request script running');"
          ]
        }
      }
    ]
  }]
}
```

After import, the pre-request script section is empty even though it should contain the script code.

### Expected behavior

Pre-request scripts from Postman collections should be imported and available in Insomnia. The scripts should be preserved and executable in the imported requests.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
