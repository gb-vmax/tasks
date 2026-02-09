# Bug Report

### Describe the bug

When importing Postman collections, request items are not being imported correctly. The importer appears to be skipping valid request objects and returning empty results instead.

### Reproduction

1. Create a Postman collection with standard request items
2. Try to import the collection into Insomnia
3. The requests don't appear in the imported workspace

Here's an example of a typical Postman request structure that should be imported:

```json
{
  "name": "Get Users",
  "request": {
    "method": "GET",
    "header": [],
    "url": {
      "raw": "https://api.example.com/users",
      "protocol": "https",
      "host": ["api", "example", "com"],
      "path": ["users"],
      "query": [
        {
          "key": "page",
          "value": "1"
        }
      ]
    }
  }
}
```

### Expected behavior

All valid request items from the Postman collection should be imported successfully, including their URLs, methods, headers, and query parameters.

### Additional context

This seems to have started happening recently. Previously, Postman collections were importing without issues. The problem affects both simple GET requests and more complex requests with authentication and body data.

---
Repository: /testbed
