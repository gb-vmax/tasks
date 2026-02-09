# Bug Report

### Describe the bug

I'm experiencing an issue where markdown parsing seems to break when processing documents with null characters or at the end of input. The parser appears to be handling the flow incorrectly, causing documents to not be properly parsed or closed.

### Reproduction

```js
const remark = require('remark');

// This causes unexpected behavior
const ast = remark.parse('# Hello\n\nSome content');
console.log(ast);

// The parser seems to exit prematurely or not handle the end of document correctly
```

When parsing markdown documents, the flow continuation logic doesn't seem to work as expected. It looks like the condition for handling null codes (end of input) got inverted somehow, causing the parser to exit containers and consume tokens at the wrong time.

### Expected behavior

The parser should correctly handle the flow of markdown content and properly close/exit containers when reaching the end of the document. Documents should parse completely without prematurely terminating.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
