# Bug Report

### Describe the bug

I'm experiencing an issue with fenced code block parsing where the parser gets stuck in an infinite loop when processing code blocks with certain line endings. The browser tab becomes unresponsive and eventually crashes.

### Reproduction

```js
const markdown = `
\`\`\`js
function test() {
  console.log('hello');
}
\`\`\`
`;

// Parser hangs indefinitely when processing this
const result = remark.parse(markdown);
```

### Expected behavior

The parser should successfully parse fenced code blocks without hanging. The code block should be tokenized normally and return the AST.

### System Info
- remark version: 15.0.1
- Browser: Chrome 120
- Node: 18.x

This seems to have started happening recently. The parser just freezes and never completes when encountering fenced code blocks.

---
Repository: /testbed
