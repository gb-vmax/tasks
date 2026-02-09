# Bug Report

### Describe the bug

I'm encountering an issue with character code validation in the remark-directive parser. When processing markdown with certain Unicode characters or edge cases, the parser is producing incorrect results or failing to properly validate character codes.

### Reproduction

```js
// Example with character codes that should be validated
const input = `
:::note
Content with special characters
:::
`;

// The parser doesn't correctly handle certain character code edge cases
// Specifically when code is 0 or negative values near -1
```

When processing markdown directives with specific character codes (particularly around boundary values like 0 or -1), the validation logic doesn't work as expected. This affects how whitespace and special characters are detected in directive content.

### Expected behavior

The character code validation should correctly identify valid Unicode characters and handle edge cases like:
- Character code 0 (null character)
- Negative values 
- Proper conversion to string for regex testing

The current implementation seems to have issues with the boundary conditions in the `regexCheck` function's validation logic.

### System Info
- remark-directive version: 3.0.0
- Node version: Latest

---
Repository: /testbed
