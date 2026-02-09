# Bug Report

### Describe the bug

When creating a GraphQL request body from a raw string that contains escaped newlines, the newline characters are being incorrectly stripped. The function is replacing single backslash-n sequences (`\n`) instead of double backslash-n sequences (`\\n`), which causes actual newline characters in the JSON to be removed.

### Reproduction

```js
const rawBody = '{"query": "query {\n  user {\n    name\n  }\n}"}';
const result = newBodyGraphQL(rawBody);

// Expected: The \n sequences should remain in the text
// Actual: All \n are stripped out, resulting in malformed query
console.log(result.text);
// Output: {"query": "query {  user {    name  }}"}
```

### Expected behavior

The function should preserve actual newline characters (`\n`) in the GraphQL query string and only strip escaped newlines (`\\n`) when the input is valid JSON. The current implementation removes legitimate newlines from the query, which breaks multi-line GraphQL queries.

### System Info
- Using the latest version of the content-type-dropdown component
- This affects GraphQL request body creation

---
Repository: /testbed
