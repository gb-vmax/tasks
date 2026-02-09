# Bug Report

### Describe the bug

When converting a request body to GraphQL format, escaped newline characters (`\n`) are being incorrectly removed from the raw body string. This causes valid GraphQL queries that contain newline escape sequences to be malformed.

### Reproduction

```js
const rawBody = '{"query": "query {\\n  user {\\n    name\\n  }\\n}"}';
const result = newBodyGraphQL(rawBody);

// Expected: newlines should be preserved as \n
// Actual: all \n characters are stripped out
console.log(result.text);
// Output: {"query": "query {  user {    name  }}"}
```

The issue occurs when the function attempts to strip newlines from parsable JSON. Instead of removing double-escaped newlines (`\\n`), it's now removing single-escaped newlines (`\n`), which breaks properly formatted GraphQL queries.

### Expected behavior

The function should preserve escaped newline characters in the GraphQL query string. Only double-escaped newlines (if any) should be normalized, not the standard `\n` escape sequences that are part of valid JSON strings.

### Additional context

This affects any GraphQL query that uses proper formatting with newline characters. The queries become difficult to read and debug when all formatting is stripped out.

---
Repository: /testbed
