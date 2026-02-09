# Bug Report

### Describe the bug

I'm experiencing an issue with nested container parsing in markdown documents. When processing documents with multiple nested containers (like blockquotes or lists), the container exit order appears to be incorrect, causing the parser state to become inconsistent.

### Reproduction

```js
const remark = require('remark');

const markdown = `
> outer blockquote
> > nested blockquote
> > content here
> back to outer
`;

const result = remark().parse(markdown);
// Parser state becomes inconsistent during container exit
```

The issue seems to occur when exiting from deeply nested structures. The container state doesn't match what's expected when unwinding the stack.

### Expected behavior

Containers should exit in the correct order, maintaining proper state throughout the unwinding process. The parser should handle nested structures cleanly without state corruption.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
