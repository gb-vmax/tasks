# Bug Report

### Describe the bug

I'm experiencing an infinite loop when parsing markdown code blocks with fenced code syntax. The parser seems to hang and never complete when processing certain markdown documents with code fences.

### Reproduction

```js
const markdown = `
\`\`\`javascript
console.log('test');
\`\`\`
`;

// Parser hangs indefinitely when processing this
const result = remark.parse(markdown);
```

### Expected behavior

The parser should successfully parse the fenced code block and return the AST without hanging. The code fence should be properly tokenized and the parser should complete normally.

### Additional context

This seems to happen specifically with fenced code blocks. Regular inline code and other markdown elements parse fine. The issue appeared recently and causes the entire parsing process to become unresponsive.

---
Repository: /testbed
