# Bug Report

### Describe the bug

When importing Postman collections, requests with empty raw body (`""`) are not being imported correctly. The body should be preserved as an empty string, but instead it seems to be getting lost during the import process.

### Reproduction

1. Create a Postman collection with a request that has an empty raw body (empty string, not null/undefined)
2. Import the collection into Insomnia
3. The request body is not properly set

Example Postman request structure:
```json
{
  "request": {
    "method": "POST",
    "body": {
      "mode": "raw",
      "raw": ""
    }
  }
}
```

### Expected behavior

Requests with empty string bodies should still create a body object with the appropriate mime type. An empty string is a valid body value and should be treated differently from null/undefined.

### System Info
- Insomnia version: latest
- Import format: Postman Collection v2

---
Repository: /testbed
