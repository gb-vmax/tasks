# Bug Report

### Describe the bug

When converting request bodies to GraphQL format, whitespace within string literals is being incorrectly normalized. The `newBodyGraphQL` function appears to collapse or modify whitespace inside quoted strings, which breaks queries that have intentional spacing or formatting within their string values.

### Reproduction

```js
const rawBody = JSON.stringify({
  query: `query {
    user(name: "John  Doe") {
      id
    }
  }`
});

const result = newBodyGraphQL(rawBody);
// The double space in "John  Doe" gets collapsed to single space
// Expected: "John  Doe"
// Actual: "John Doe"
```

Another example with newlines in strings:

```js
const rawBody = JSON.stringify({
  query: `mutation {
    updateBio(text: "Line 1
Line 2") {
      success
    }
  }`
});

const result = newBodyGraphQL(rawBody);
// The newline character inside the string literal is being modified
```

### Expected behavior

String literals within GraphQL queries should preserve their original whitespace and formatting. Only whitespace outside of strings should be normalized for query formatting purposes.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
