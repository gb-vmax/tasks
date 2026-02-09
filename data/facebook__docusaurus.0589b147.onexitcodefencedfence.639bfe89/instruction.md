# Bug Report

### Describe the bug

I'm encountering an issue with fenced code blocks in markdown parsing. When parsing markdown with code fences, the content inside the code block is not being captured correctly. It seems like the buffer is not being populated as expected.

### Reproduction

```js
const markdown = `
\`\`\`javascript
const x = 1;
console.log(x);
\`\`\`
`;

// Parse the markdown
const result = remark().parse(markdown);

// The code block node has empty or missing value
console.log(result.children[0].value); // Expected: "const x = 1;\nconsole.log(x);\n"
```

### Expected behavior

The parser should correctly extract and store the content between code fences. The resulting AST node should have a `value` property containing the code block content.

### System Info
- remark version: 15.0.1
- Node version: 18.x

This is affecting our documentation generation pipeline where code examples are not being rendered properly.

---
Repository: /testbed
