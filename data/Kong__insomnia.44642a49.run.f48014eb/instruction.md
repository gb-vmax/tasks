# Bug Report

### Describe the bug

The JSONPath template tag is not handling multiple results correctly. When a JSONPath query returns multiple matching values, only the first result is being returned instead of all matches.

### Reproduction

```js
const jsonData = {
  users: [
    { name: "Alice", age: 30 },
    { name: "Bob", age: 25 },
    { name: "Charlie", age: 35 }
  ]
}

// Using JSONPath to query all user names
// Query: $.users[*].name
// Expected: "Alice, Bob, Charlie" or ["Alice", "Bob", "Charlie"]
// Actual: "Alice" (only the first result)
```

When using a JSONPath query that matches multiple elements (like `$.users[*].name`), I'm only getting back the first match. This makes it difficult to work with arrays or multiple matching values in templates.

### Expected behavior

When a JSONPath query returns multiple results, the template should return all matching values, not just the first one. Ideally it should:
- Join string results with commas
- Return a JSON array for mixed types
- Or provide some way to access all results

### Additional context

This is blocking our use case where we need to extract all matching values from an API response. Currently we have to make multiple queries with specific indices which is not ideal.

---
Repository: /testbed
