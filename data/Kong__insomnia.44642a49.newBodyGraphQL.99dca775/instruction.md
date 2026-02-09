# Bug Report

### Describe the bug

When converting request body to GraphQL format, the `newBodyGraphQL` function is not handling plain GraphQL query strings correctly. If you pass a raw GraphQL query (not wrapped in JSON), it gets wrapped in a JSON object with a `query` field, but this only happens when the input is not valid JSON and doesn't start with `{`.

This creates inconsistent behavior depending on the input format.

### Reproduction

```js
// Case 1: Plain GraphQL query string
const body1 = `
  query GetUser {
    user(id: "123") {
      name
      email
    }
  }
`;
const result1 = newBodyGraphQL(body1);
// Result gets wrapped as: { "query": "..." }

// Case 2: GraphQL query starting with whitespace/newlines
const body2 = `
{
  user(id: "123") {
    name
  }
}
`;
const result2 = newBodyGraphQL(body2);
// This behaves differently - not wrapped consistently
```

### Expected behavior

The function should handle GraphQL queries consistently regardless of whether they:
- Start with whitespace/newlines
- Are plain query strings vs JSON-wrapped
- Contain mutations or subscriptions instead of queries

All GraphQL content should be properly formatted and wrapped in a consistent JSON structure.

### Additional context

This seems to affect how GraphQL requests are stored and displayed in the UI. Sometimes the query appears properly formatted, other times it doesn't get the expected JSON wrapping.

---
Repository: /testbed
