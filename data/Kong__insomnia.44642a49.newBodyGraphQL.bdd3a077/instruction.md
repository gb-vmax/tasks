# Bug Report

### Describe the bug

When converting a request body to GraphQL format, the newline handling seems broken. If the raw body contains escaped newlines (`\n`), they're being replaced incorrectly, and there's also an issue with how JSON parsing errors are handled.

### Reproduction

```js
// Case 1: Valid JSON with escaped newlines
const rawBody = '{"query": "query {\\n  user {\\n    name\\n  }\\n}"}'
const result = newBodyGraphQL(rawBody)
// Expected: newlines should be stripped properly
// Actual: only single backslash newlines are replaced, not double backslash

// Case 2: Invalid JSON (non-SyntaxError)
const rawBodyWithError = /* some input that throws non-SyntaxError */
const result2 = newBodyGraphQL(rawBodyWithError)
// Expected: should return the raw body as-is
// Actual: behavior is inverted
```

### Expected behavior

1. When the raw body is valid JSON, escaped newlines (like `\\n`) should be properly stripped from the text
2. When JSON parsing fails with a SyntaxError, the raw body should be returned as-is without modification
3. When JSON parsing fails with other errors, the raw body should be returned as-is

### Additional context

This is affecting GraphQL query formatting when importing requests or converting from other formats. The queries end up with incorrect newline characters which can cause issues with some GraphQL servers.

---
Repository: /testbed
