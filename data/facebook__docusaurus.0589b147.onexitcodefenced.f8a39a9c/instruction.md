# Bug Report

### Describe the bug

I'm experiencing an issue with fenced code blocks in markdown parsing. When a code block ends with a newline, the trailing newline is not being removed from the code value. This causes the rendered output to have extra blank lines at the end of code blocks.

### Reproduction

```js
const markdown = `
\`\`\`js
console.log('test');

\`\`\`
`;

// After parsing, the code block value includes the trailing newline
// Expected: "console.log('test');"
// Actual: "console.log('test');\n"
```

### Expected behavior

Fenced code blocks should have both leading and trailing newlines stripped from their content, just like they did in previous versions. The code value should be clean without extra whitespace at the beginning or end.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
