# Bug Report

### Describe the bug

When importing Postman collections, the after-response scripts (test scripts) are not being imported correctly. Instead, it seems like the pre-request scripts are being imported in their place.

### Reproduction

1. Create a Postman collection with a request that has both pre-request and test scripts
2. Add some test script code (e.g., `pm.test("Status code is 200", function () { pm.response.to.have.status(200); });`)
3. Export the collection and import it into Insomnia
4. Check the imported request - the after-response script section will be empty or contain the wrong script

Example Postman collection structure:
```json
{
  "item": [{
    "name": "Test Request",
    "event": [
      {
        "listen": "prerequest",
        "script": {
          "exec": ["console.log('Before request');"]
        }
      },
      {
        "listen": "test",
        "script": {
          "exec": ["pm.test('Check status', function() { pm.response.to.have.status(200); });"]
        }
      }
    ]
  }]
}
```

### Expected behavior

The test scripts (after-response scripts) from Postman should be properly imported and available in the after-response section of the imported request in Insomnia.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
