# Bug Report

### Describe the bug
When converting request body to GraphQL format, the conversion logic doesn't properly handle JSON objects with GraphQL structure. If the raw body contains a JSON object with `query`, `variables`, and `operationName` fields, it should be parsed and formatted appropriately, but instead it just strips newlines from the raw string.

### Reproduction
```js
const rawBody = JSON.stringify({
  query: 'query GetUser { user { id name } }',
  variables: { userId: 123 },
  operationName: 'GetUser'
});

const result = newBodyGraphQL(rawBody);
// Currently just returns the stringified JSON with escaped newlines removed
// Expected: properly formatted GraphQL with query, variables section, and operation name
```

### Expected behavior
When the raw body is a valid JSON object containing GraphQL fields (`query`, `variables`, `operationName`), the function should:
1. Extract the query text
2. Add a variables section if present
3. Add an operation name comment if present
4. Format them properly with newlines and comments

Instead of just stripping `\\n` characters, it should parse the structure and create a properly formatted GraphQL body.

### System Info
- Insomnia version: latest
- OS: N/A

---
Repository: /testbed
