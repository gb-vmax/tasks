# Bug Report

### Describe the bug

When importing Postman collections, the after-response scripts (test scripts) are not being imported correctly. Instead of importing the test event scripts, it appears that prerequest scripts are being imported in their place. Additionally, the script lines seem to be concatenated with spaces instead of newlines, which breaks the script formatting.

### Reproduction

1. Create a Postman collection with a request that has both prerequest and test scripts
2. Add some test assertions in the "Tests" tab (e.g., `pm.test("Status code is 200", ...)`)
3. Export the collection as JSON
4. Import the collection into Insomnia
5. Check the after-response script section

**Expected behavior:**
The test scripts from Postman should be imported into the after-response script section, with proper line breaks between script lines.

**Actual behavior:**
The after-response script section either appears empty or contains prerequest script content instead of test scripts. If there is content, the lines are joined with spaces instead of newlines, making the script malformed.

### Example

Given a Postman collection with:
```json
{
  "event": [
    {
      "listen": "prerequest",
      "script": {
        "exec": ["console.log('before request');"]
      }
    },
    {
      "listen": "test",
      "script": {
        "exec": [
          "pm.test('Status code is 200', function () {",
          "    pm.response.to.have.status(200);",
          "});"
        ]
      }
    }
  ]
}
```

The test script should be imported, but it's not being picked up correctly.

### System Info
- Insomnia version: latest
- OS: N/A (affects all platforms)

---
Repository: /testbed
