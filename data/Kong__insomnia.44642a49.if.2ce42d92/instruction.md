# Bug Report

### Describe the bug
When importing Postman collections that contain GraphQL requests, the GraphQL body is not being imported correctly. Instead of getting the GraphQL query and variables, the imported request ends up with no body data.

### Reproduction
```js
// Import a Postman collection with a GraphQL request
const collection = {
  item: [{
    request: {
      body: {
        mode: 'graphql',
        graphql: {
          query: 'query { users { id name } }',
          variables: '{"limit": 10}'
        }
      }
    }
  }]
}

// After importing, the GraphQL body is missing
// Expected: body should contain the query and variables
// Actual: body is empty/null
```

### Expected behavior
When importing Postman collections with GraphQL requests, the GraphQL query, variables, and other GraphQL-specific data should be properly imported and available in the request body.

### System Info
- Insomnia version: latest
- OS: macOS

This seems to have broken recently. GraphQL imports were working fine before.

---
Repository: /testbed
