# Bug Report

### Describe the bug

After a recent update, importing Postman collections is failing. The importer crashes when trying to process requests that have test scripts (after-response events). It looks like the function that handles test script import was accidentally replaced with some unrelated code.

### Reproduction

1. Create a Postman collection with a request that has a test script
2. Try to import the collection into Insomnia
3. The import fails with an error

Example Postman collection structure:
```json
{
  "item": [
    {
      "name": "Test Request",
      "request": {
        "method": "GET",
        "url": "https://example.com"
      },
      "event": [
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
  ]
}
```

### Expected behavior

The Postman collection should import successfully and the test scripts should be converted to Insomnia's format.

### Additional context

This seems to have broken in the latest version. Collections without test scripts import fine, but any collection with test events fails to import properly.

---
Repository: /testbed
