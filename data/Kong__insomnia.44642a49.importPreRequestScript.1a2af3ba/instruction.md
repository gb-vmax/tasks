# Bug Report

### Describe the bug

Pre-request scripts are not being imported correctly from Postman collections. When importing a collection that contains pre-request scripts, the scripts are missing or empty in the imported requests.

### Reproduction

1. Export a Postman collection that includes pre-request scripts on requests
2. Import the collection into Insomnia
3. Open the imported requests and check the pre-request script section
4. The pre-request scripts are empty/missing even though they existed in the original Postman collection

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
              "pm.environment.set('variable', 'value');"
            ]
          }
        }
      ],
      "request": {
        "method": "GET",
        "url": "https://example.com"
      }
    }
  ]
}
```

### Expected behavior

Pre-request scripts from Postman collections should be properly imported and available in the imported requests. The script content should be preserved and functional.

### System Info
- Insomnia version: latest
- OS: Windows/Mac/Linux

---
Repository: /testbed
