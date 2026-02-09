# Bug Report

### Describe the bug

I'm experiencing an infinite loop when parsing markdown content with remark. The parser seems to get stuck and never completes, causing the application to hang indefinitely.

### Reproduction

```js
import {remark} from 'remark';

const markdown = `
# Test Document

Some content here with **bold** and *italic* text.

- List item 1
- List item 2
`;

// This call never returns and causes the process to hang
const result = await remark().process(markdown);
console.log(result); // Never reaches this line
```

### Expected behavior

The markdown should be parsed successfully and the process should complete normally without hanging.

### System Info
- remark version: 15.0.1
- Node version: Latest

This is blocking our production deployment. Any help would be appreciated!

---
Repository: /testbed
