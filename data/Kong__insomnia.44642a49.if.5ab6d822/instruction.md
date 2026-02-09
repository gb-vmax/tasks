# Bug Report

### Describe the bug

When importing Postman collections that contain GraphQL requests, the GraphQL body is not being imported correctly. The request body ends up empty even though the Postman collection has valid GraphQL query and variables defined.

### Reproduction

1. Export a Postman collection that contains a GraphQL request with a query body
2. Import the collection into Insomnia
3. Open the imported GraphQL request
4. The request body is empty instead of containing the GraphQL query

Example Postman collection structure:
```json
{
  "request": {
    "method": "POST",
    "body": {
      "mode": "graphql",
      "graphql": {
        "query": "query { users { id name } }",
        "variables": "{}"
      }
    }
  }
}
```

### Expected behavior

The GraphQL query and variables should be imported and visible in the request body after importing the Postman collection.

### Additional context

This seems to affect all GraphQL requests when importing from Postman. Regular REST requests import fine, but GraphQL-specific body content is lost during the import process.

---
Repository: /testbed
