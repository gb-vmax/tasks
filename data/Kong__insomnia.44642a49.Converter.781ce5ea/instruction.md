# Bug Report

### Describe the bug

After a recent update, Postman collection imports are failing or producing incomplete results. The import process seems to hang or complete without importing all the expected requests and folders from the collection.

### Reproduction

When trying to import a Postman collection (v2.0 or v2.1 schema), the import either:
1. Doesn't complete successfully
2. Completes but with missing items
3. Gets stuck during the import process

Steps to reproduce:
1. Export a collection from Postman (v2.1 format)
2. Try to import it into Insomnia
3. The import process doesn't complete as expected

Example collection structure that triggers the issue:
```json
{
  "info": {
    "name": "My API Collection",
    "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
  },
  "item": [
    {
      "name": "Test Request",
      "request": {
        "method": "GET",
        "url": "https://api.example.com/test"
      }
    }
  ]
}
```

### Expected behavior

The collection should import completely with all requests and folders properly created in Insomnia.

### System Info
- Insomnia version: Latest
- OS: Multiple platforms affected

This appears to have started happening recently. Previously working collection imports are now failing.

---
Repository: /testbed
