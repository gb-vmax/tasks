# Bug Report

### Describe the bug

Fenced code blocks in markdown are not being parsed correctly. The code content appears to be getting stripped of newlines and placed in the wrong node in the AST.

### Reproduction

```js
const markdown = `
\`\`\`javascript
function test() {
  return true;
}
\`\`\`
`;

const result = remark.parse(markdown);
// The code block value is missing internal newlines
// and/or appears in an unexpected location in the tree
```

### Expected behavior

Fenced code blocks should preserve their internal newline characters and be properly attached to the correct parent node in the syntax tree. The opening and closing newlines should be trimmed, but newlines within the code content should remain intact.

### System Info
- remark version: 15.0.1

---
Repository: /testbed
