# Bug Report

### Describe the bug

I'm experiencing an issue with fenced code blocks in markdown parsing. When using code fences with more backticks in the closing fence than the opening fence, the parser seems to hang or behave incorrectly.

### Reproduction

```js
const markdown = `
\`\`\`js
console.log('test');
\`\`\`\`
`;

// Parser hangs or produces unexpected output
const result = remark().parse(markdown);
```

The issue occurs when the closing fence has 4 backticks while the opening fence has only 3. According to the CommonMark spec, the closing fence should have at least the same number of backticks as the opening fence, but having more should close the block properly.

### Expected behavior

The parser should correctly identify and close the fenced code block when the closing fence has an equal or greater number of fence characters compared to the opening fence. The code block should be properly parsed without hanging.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
