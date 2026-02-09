# Bug Report

### Describe the bug

I'm encountering an issue with fenced code blocks in markdown parsing. When a fenced code block has content immediately following the closing fence (without a line break), the parser incorrectly accepts it as valid markdown instead of rejecting it.

### Reproduction

```js
const markdown = `
\`\`\`js
console.log('test');
\`\`\`invalid text here
`;

// This should be rejected but is currently being parsed as valid
```

The parser should only accept the closing fence if it's followed by either:
- End of file (null)
- A line ending

But currently it's accepting closing fences that have other characters immediately after them on the same line.

### Expected behavior

The parser should reject fenced code blocks where the closing fence is followed by non-whitespace characters on the same line. The closing fence should only be valid when followed by a line break or EOF.

### System Info
- remark version: 15.0.1
- Browser/Node: Node.js

---
Repository: /testbed
