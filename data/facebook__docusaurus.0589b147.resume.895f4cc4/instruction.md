# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where the output becomes incorrect when processing certain markdown structures. It seems like the parser is returning the wrong content or null values in some cases.

### Reproduction

```js
const remark = require('remark');
const processor = remark();

// Parse some markdown with nested structures
const result = processor.processSync('# Header\n\nSome content');

// Expected to get the parsed tree with correct content
// Instead getting unexpected null or wrong node values
console.log(result);
```

The parsed output doesn't match what I'm expecting - it looks like nodes are being resolved incorrectly or returning null when they shouldn't.

### Expected behavior

The parser should correctly return the parsed markdown tree with all nodes properly populated. When processing markdown, each node should contain the expected content from the source.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
