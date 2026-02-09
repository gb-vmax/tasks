# Bug Report

### Describe the bug

After a recent update, the Postman importer is not working correctly when importing requests with raw body content. The import process appears to fail or produce incorrect results when the raw body is an empty string.

### Reproduction

When trying to import a Postman collection that contains requests with empty raw bodies, the import doesn't complete properly. 

Example Postman request structure that triggers the issue:
```json
{
  "request": {
    "body": {
      "mode": "raw",
      "raw": ""
    }
  }
}
```

Steps to reproduce:
1. Create a Postman collection with a request that has an empty raw body
2. Export the collection
3. Try to import it into Insomnia
4. The import fails or produces unexpected results

### Expected behavior

Requests with empty raw bodies should import successfully, just like they did in previous versions. The importer should handle empty strings gracefully and create the request with an empty body.

### Additional context

This seems to have started happening recently. Collections that previously imported fine are now having issues if they contain any requests with empty raw body content.

---
Repository: /testbed
