# Bug Report

### Describe the bug

When converting request bodies to GraphQL format, escaped newlines (`\n`) in the raw body string are being incorrectly stripped. This causes issues when the body contains intentional newline characters that should be preserved.

### Reproduction

```js
const rawBody = '{"query": "query {\\n  user {\\n    name\\n  }\\n}"}';
const result = newBodyGraphQL(rawBody);

// Expected: newlines should be preserved in valid JSON
// Actual: all \n characters are removed, breaking the formatting
console.log(result.text);
```

The function now removes single backslash-n sequences (`\n`) instead of double backslash-n sequences (`\\n`), which affects properly formatted GraphQL queries that contain newlines.

### Expected behavior

Valid JSON strings with newline characters should have those newlines preserved. The function should only strip double-escaped newlines (`\\n`) when the input is parsable JSON, not single escaped newlines (`\n`).

### Additional context

This appears to have changed recently. Previously the regex was `replace(/\\\\n/g, '')` which correctly handled double-escaped newlines, but now it's using `replace(/\\n/g, '')` which strips all newline sequences.

---
Repository: /testbed
