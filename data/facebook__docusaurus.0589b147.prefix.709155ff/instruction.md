# Bug Report

### Describe the bug

I'm experiencing an issue with whitespace handling in markdown parsing. When processing content with multiple consecutive spaces, the parser seems to be consuming an extra space character and incorrectly exiting the prefix state.

### Reproduction

```js
const markdown = `
Text with    multiple spaces
`;

// Parse the markdown
const result = parseMarkdown(markdown);

// The whitespace is not preserved correctly
// Expected: 4 spaces between "with" and "multiple"
// Actual: spaces are consumed incorrectly
```

### Expected behavior

The parser should correctly handle the maximum number of allowed spaces according to the limit. When the space count reaches the limit, it should exit the prefix state properly without consuming additional characters.

### System Info
- remark version: 15.0.1
- Node version: 18.x

This seems to have started happening recently. The whitespace handling was working fine before, but now consecutive spaces in markdown content are being processed incorrectly.

---
Repository: /testbed
