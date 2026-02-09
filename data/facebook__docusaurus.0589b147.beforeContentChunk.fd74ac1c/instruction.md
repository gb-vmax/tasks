# Bug Report

### Describe the bug

I'm experiencing an issue with code fence parsing in markdown. When I have a code block that ends with a null character or specific line ending patterns, the parser seems to enter an infinite loop or hangs indefinitely.

### Reproduction

```js
const markdown = `
\`\`\`js
function test() {
  console.log("hello");
}
\`\`\`
`;

// Parser hangs when processing this input
const result = remark().parse(markdown);
```

The issue appears to happen specifically with fenced code blocks. The parser gets stuck and doesn't complete the parsing operation.

### Expected behavior

The parser should handle code fences normally and complete parsing without hanging, returning the expected AST structure for the code block.

### System Info
- remark version: 15.0.1
- Node.js version: 18.x

---
Repository: /testbed
