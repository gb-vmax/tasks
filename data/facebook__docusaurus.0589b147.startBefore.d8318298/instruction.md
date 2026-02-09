# Bug Report

### Describe the bug

I'm encountering an issue with fenced code blocks in markdown parsing. When I have a fenced code block in my markdown content, the parser seems to get stuck in an infinite loop and never completes parsing.

### Reproduction

```js
const markdown = `
\`\`\`javascript
console.log('test');
\`\`\`
`;

// Parser hangs and never returns
const result = remark.parse(markdown);
```

### Expected behavior

The parser should correctly parse fenced code blocks and return the AST without hanging. The code block should be recognized and processed normally.

### Additional context

This seems to happen specifically with fenced code blocks. Regular inline code and other markdown elements parse fine. The issue appears when the parser tries to close the code fence - it just stops responding.

---
Repository: /testbed
