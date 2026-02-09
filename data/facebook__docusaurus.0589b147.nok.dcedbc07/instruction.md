# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where certain malformed or edge-case markdown syntax causes the parser to hang or enter an infinite loop. The application becomes unresponsive when processing specific markdown input.

### Reproduction

```js
const remark = require('remark');

const markdown = `
[invalid link syntax
more text here
`;

// Parser hangs indefinitely
const result = remark().parse(markdown);
```

### Expected behavior

The parser should either handle the invalid syntax gracefully or fail with an error message, but it should not hang indefinitely. Even with malformed input, the parser should complete processing in a reasonable amount of time.

### System Info
- remark version: 15.0.1
- Node.js version: 18.x

This seems to happen specifically with certain types of incomplete or nested markdown constructs. The browser tab becomes unresponsive and needs to be force-closed.

---
Repository: /testbed
