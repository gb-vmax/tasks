# Bug Report

### Describe the bug

When converting a request body to GraphQL format, newline character handling is inverted. If the raw body is valid JSON, newlines are NOT being stripped (but they should be). If the raw body is invalid JSON, newlines ARE being stripped (but they shouldn't be).

This causes issues when working with GraphQL queries that contain escaped newlines in different formats.

### Reproduction

```js
// Case 1: Valid JSON - newlines should be stripped but aren't
const validJson = '{"query": "query {\\n  user {\\n    name\\n  }\\n}"}';
const result1 = newBodyGraphQL(validJson);
// result1.text still contains \\n characters (WRONG)

// Case 2: Invalid JSON - newlines shouldn't be stripped but are
const invalidJson = 'query {\n  user {\n    name\n  }\n}';
const result2 = newBodyGraphQL(invalidJson);
// result2.text has newlines removed (WRONG)
```

### Expected behavior

- When the input is valid JSON, escaped newlines (`\\n`) should be stripped from the output
- When the input is invalid JSON (raw GraphQL query), newlines should be preserved as-is

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
