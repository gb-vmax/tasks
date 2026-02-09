# Bug Report

### Describe the bug
When parsing string literals in MDX, the opening quote character is being included in the parsed string value. This causes strings to start with an extra quote character that shouldn't be there.

### Reproduction
```js
// When parsing a string like "hello"
// Expected result: "hello"
// Actual result: ""hello"

const mdx = `
export const greeting = "world"
`

// The parsed string value includes the opening quote
```

### Expected behavior
String parsing should skip the opening quote character and only capture the content between the quotes. The opening quote should not be part of the final string value.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
