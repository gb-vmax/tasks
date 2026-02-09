# Bug Report

### Describe the bug

I'm experiencing an issue with the markdown parser where it seems to get stuck in an infinite loop or causes a stack overflow when trying to parse certain content. The parser becomes unresponsive and eventually crashes.

### Reproduction

```js
const remark = require('remark');

const processor = remark();

// Attempting to parse markdown content
const result = processor.parse('# Hello World');
```

When running this code, the parser hangs indefinitely or throws a "Maximum call stack size exceeded" error.

### Expected behavior

The parser should successfully parse the markdown content and return the AST without hanging or crashing.

### System Info
- remark version: 15.0.1
- Node version: 18.x

This seems to have started happening recently. Previously the same code worked fine for parsing markdown content.

---
Repository: /testbed
