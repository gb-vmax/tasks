# Bug Report

### Describe the bug

I'm getting a runtime error when importing Postman collections that have requests with empty query parameters. The import process crashes instead of handling the empty parameters gracefully.

### Reproduction

1. Create a Postman collection with a request that has an empty query parameters array
2. Try to import the collection into Insomnia
3. The import fails with a type error

Example collection structure that causes the issue:
```json
{
  "item": [
    {
      "request": {
        "url": {
          "query": []
        }
      }
    }
  ]
}
```

### Expected behavior

The import should complete successfully, treating empty query parameters as no parameters. The request should be created without any query parameters instead of causing the import to fail.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
