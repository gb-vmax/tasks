# Bug Report

### Describe the bug

When importing Postman collections that contain GraphQL requests, the GraphQL body is not being imported correctly. The request body ends up empty instead of containing the GraphQL query and variables.

### Reproduction

1. Export a Postman collection that includes a GraphQL request with a query
2. Import the collection into Insomnia
3. Check the imported GraphQL request

Expected: The GraphQL query and variables should be present in the request body
Actual: The request body is empty

### Additional context

This appears to affect all GraphQL requests in Postman collections. Regular REST requests import fine, but any request with GraphQL body type loses its content during import.

---
Repository: /testbed
