# Bug Report

### Describe the bug
When importing Postman collections with query parameters, the import process fails or behaves unexpectedly. It seems like query parameters are not being properly imported into Insomnia.

### Reproduction
1. Export a Postman collection that contains requests with query parameters
2. Try to import the collection into Insomnia
3. The requests either fail to import or the query parameters are missing/null

Example Postman collection structure:
```json
{
  "request": {
    "url": {
      "query": [
        {
          "key": "param1",
          "value": "value1",
          "disabled": false
        },
        {
          "key": "param2",
          "value": "value2",
          "disabled": false
        }
      ]
    }
  }
}
```

### Expected behavior
Query parameters from Postman collections should be properly imported and available in the imported requests.

### Additional context
This issue seems to affect all collections with query parameters. Collections without query parameters import fine.

---
Repository: /testbed
