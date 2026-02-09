# Bug Report

### Describe the bug
Fenced code blocks in markdown are not being parsed correctly. The code content appears to be assigned to the wrong node in the AST, and leading newlines are being preserved when they should be stripped.

### Reproduction
```js
const markdown = `
\`\`\`javascript
const x = 1;
\`\`\`
`;

const result = remark().parse(markdown);
// The code block value contains leading newline and is attached to wrong parent
```

When parsing markdown with fenced code blocks, the resulting AST has the code value attached to an incorrect node in the stack. Additionally, the regex pattern for trimming newlines only removes trailing newlines but leaves leading ones intact.

### Expected behavior
- The code block value should be assigned to the correct node in the syntax tree
- Both leading and trailing newlines should be stripped from the code content
- The parsed code block should contain only the actual code content without extra whitespace

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
