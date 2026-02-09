# Bug Report

### Describe the bug

When importing Postman collections, the after-response scripts (test scripts) are not being imported correctly. Instead, it seems like the importer is looking for the wrong event type and the scripts are being lost during the import process.

### Reproduction

1. Create a Postman collection with test scripts in requests
2. Add a test script to a request (e.g., `pm.test("Status code is 200", ...)`)
3. Export the collection from Postman
4. Import the collection into Insomnia
5. Check the imported request - the test script is missing

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
    }
  ]
}
```

### Expected behavior

Test scripts from Postman collections should be imported and available in the after-response script section in Insomnia.

### Additional context

This affects any Postman collection that uses test scripts, which is a pretty common feature in Postman for API testing and validation. The scripts just disappear after import.

---
Repository: /testbed
