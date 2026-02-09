# Bug Report

### Describe the bug

When parsing fenced code blocks in markdown, the parser enters an infinite loop and hangs indefinitely. This appears to happen with specific code block content that contains line endings.

### Reproduction

```js
const markdown = `
\`\`\`js
function test() {
  return true;
}
\`\`\`
`;

// Parser hangs here and never completes
const result = remark.parse(markdown);
```

### Expected behavior

The parser should successfully parse fenced code blocks and return the AST without hanging. Multi-line code blocks should be processed normally.

### System Info
- remark version: 15.0.1
- Node version: 18.x

This is blocking our documentation build pipeline. Any help would be appreciated!

---
Repository: /testbed
