# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where content chunks are not being processed correctly. It seems like the internal state management for tracking previous chunks might be broken, causing the parser to get stuck or produce incorrect output when processing certain markdown structures.

### Reproduction

```js
const remark = require('remark');

const markdown = `
This is a paragraph with some content.

Another paragraph here.
`;

const result = remark().parse(markdown);
// The parsed output doesn't match the expected structure
```

### Expected behavior

The markdown parser should correctly process content chunks and maintain proper state between chunk boundaries. Each chunk should be linked to its previous chunk appropriately, and the parser should continue processing subsequent chunks without getting stuck.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
