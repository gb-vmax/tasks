# Bug Report

### Describe the bug

I'm encountering an issue with code fence parsing in markdown. When processing fenced code blocks, the closing fence doesn't seem to be handled correctly, causing the parser to fail or produce incorrect output.

### Reproduction

```js
const markdown = `
\`\`\`js
console.log('test');
\`\`\`
`;

// Parse the markdown with remark
const result = parse(markdown);
// The code block is not properly closed/recognized
```

### Expected behavior

The fenced code block should be properly parsed with both opening and closing fences recognized correctly. The parser should correctly identify the end of the code block and continue processing any content that follows.

### Additional context

This seems to affect code blocks with language identifiers. The opening fence is detected fine, but something goes wrong when the parser tries to match the closing fence.

---
Repository: /testbed
