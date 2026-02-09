# Bug Report

### Describe the bug
When importing Postman collections, request items are not being imported correctly. The requests appear to be skipped or empty after import, even though the collection file contains valid request data.

### Reproduction
1. Export a collection from Postman that contains regular HTTP requests
2. Import the collection file into Insomnia
3. Observe that the requests are missing or empty in the imported workspace

Example collection structure that fails to import:
```json
{
  "item": [
    {
      "name": "Test Request",
      "request": {
        "method": "GET",
        "url": "https://api.example.com/test",
        "header": [
          {
            "key": "Content-Type",
            "value": "application/json"
          }
        ]
      }
    }
  ]
}
```

### Expected behavior
All requests in the Postman collection should be imported successfully with their method, URL, headers, and body intact.

### System Info
- Insomnia version: latest
- OS: macOS

This seems to have started happening recently. Collections that imported fine before are now coming in empty.

---
Repository: /testbed
