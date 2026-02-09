# Bug Report

### Describe the bug
When importing Postman collections, the after-response scripts (test scripts) are not being imported correctly. Instead, it appears that pre-request scripts are being imported in their place.

### Reproduction
1. Create a Postman collection with test scripts defined in the `test` event
2. Export the collection
3. Import it into Insomnia
4. Check the imported requests - the after-response scripts are missing or incorrect

Example Postman collection structure:
```json
{
  "event": [
    {
      "listen": "test",
      "script": {
        "exec": [
          "pm.test('Status code is 200', function () {",
          "  pm.response.to.have.status(200);",
          "});"
        ]
      }
    },
    {
      "listen": "prerequest",
      "script": {
        "exec": [
          "console.log('Before request');"
        ]
      }
    }
  ]
}
```

### Expected behavior
The test scripts (events with `listen: 'test'`) should be imported as after-response scripts, not the pre-request scripts.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
