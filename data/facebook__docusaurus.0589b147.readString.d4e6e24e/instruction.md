# Bug Report

### Describe the bug

I'm experiencing an issue with string parsing where the opening quote character is being included in the parsed string value. This appears to be affecting string literals in the code.

### Reproduction

When parsing a string literal, the opening quote is incorrectly included as part of the string content:

```js
// Input: "hello"
// Expected output: hello
// Actual output: "hello (includes the opening quote)
```

The same issue seems to occur with single quotes:

```js
// Input: 'world'
// Expected: world
// Actual: 'world (opening quote included)
```

### Expected behavior

String parsing should exclude both the opening and closing quote characters from the final string value. Only the content between the quotes should be returned.

### System Info
- Version: 3.0.0
- Node version: Latest

---
Repository: /testbed
