# Bug Report

### Describe the bug
When importing Postman collections with query parameters, requests that have exactly one query parameter are not being imported correctly. The parameter gets dropped and the request ends up with no query parameters at all.

### Reproduction
1. Export a Postman collection that contains a request with a single query parameter
2. Import the collection into Insomnia
3. Check the imported request - the query parameter is missing

Example Postman request that fails to import properly:
```json
{
  "request": {
    "method": "GET",
    "url": {
      "raw": "https://api.example.com/users?id=123",
      "query": [
        {
          "key": "id",
          "value": "123",
          "disabled": false
        }
      ]
    }
  }
}
```

### Expected behavior
The query parameter should be imported and available in the request. Requests with 0, 1, or multiple query parameters should all import correctly.

### System Info
- Insomnia version: latest
- OS: macOS

This seems to only affect requests with exactly one parameter. Requests with 0 or 2+ parameters import fine.

---
Repository: /testbed
