# Bug Report

### Describe the bug

I'm encountering an issue with code fence parsing in remark where the buffer content appears to be duplicated or incorrectly handled when processing fenced code blocks. It seems like the buffer is being called at the wrong time, causing the code content to be processed multiple times or in an unexpected order.

### Reproduction

```js
const remark = require('remark');
const markdown = `
\`\`\`javascript
console.log('test');
\`\`\`
`;

const result = remark().parse(markdown);
console.log(result);
```

When parsing markdown with fenced code blocks, the resulting AST or output contains duplicated or incorrectly ordered content from the code fence.

### Expected behavior

The code fence content should be captured exactly once and in the correct order. The buffer should be called before setting the `flowCodeInside` flag to ensure proper sequencing of the parsing operations.

### System Info

- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
