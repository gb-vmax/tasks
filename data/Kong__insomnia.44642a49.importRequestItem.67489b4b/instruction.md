# Bug Report

### Describe the bug

When importing Postman collections, query parameters are not being imported correctly. It seems like requests with query parameters are having them stripped out during the import process, resulting in requests without any parameters even though they were defined in the original Postman collection.

### Reproduction

1. Export a Postman collection that contains requests with query parameters (e.g., `GET https://api.example.com/users?page=1&limit=10`)
2. Import the collection into Insomnia
3. Check the imported request - the query parameters are missing

For example, a request like:
```
GET https://api.example.com/search?q=test&filter=active
```

Gets imported as:
```
GET https://api.example.com/search
```

The `q` and `filter` parameters are completely lost.

### Expected behavior

Query parameters from the Postman collection should be preserved during import and appear in the imported requests in Insomnia.

### Additional context

This seems to have started happening recently. Previously imported collections with query parameters worked fine, but re-importing the same collections now results in missing parameters.

---
Repository: /testbed
