# Bug Report

### Describe the bug

When importing Postman collections, query parameters are not being imported correctly. The URL query parameters that are defined in the Postman collection are missing from the imported requests in Insomnia.

### Reproduction

1. Export a Postman collection that contains requests with query parameters
2. Import the collection into Insomnia
3. Check the imported requests - query parameters are missing

Example Postman collection structure:
```json
{
  "request": {
    "method": "GET",
    "url": {
      "raw": "https://api.example.com/users?page=1&limit=10",
      "query": [
        {
          "key": "page",
          "value": "1"
        },
        {
          "key": "limit",
          "value": "10"
        }
      ]
    }
  }
}
```

### Expected behavior

Query parameters defined in the Postman collection should be imported and available in the Insomnia request. The parameters array should be populated with the query parameters from the Postman collection.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
