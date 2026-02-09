# Bug Report

### Describe the bug

When importing Postman collections, pre-request scripts are not being imported correctly. The scripts appear to be missing or empty in the imported requests, even though they exist in the original Postman collection.

### Reproduction

1. Export a Postman collection that contains requests with pre-request scripts
2. Import the collection into Insomnia
3. Check the imported requests - the pre-request scripts are missing

Example Postman collection structure:
```json
{
  "item": [
    {
      "name": "Test Request",
      "event": [
        {
          "listen": "prerequest",
          "script": {
            "exec": [
              "console.log('This is a pre-request script');",
              "pm.environment.set('timestamp', Date.now());"
            ]
          }
        }
      ]
    }
  ]
}
```

After import, the pre-request script section is empty even though the original collection has the script defined.

### Expected behavior

Pre-request scripts from Postman collections should be imported and available in the corresponding Insomnia requests.

### Additional context

This seems to have started happening recently. Previously imported collections with pre-request scripts worked fine.

---
Repository: /testbed
