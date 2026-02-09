# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where the parser seems to be calling callbacks in an incorrect order. This is causing problems with content processing - specifically, the parser appears to be exiting content chunks before properly completing the tokenization flow.

### Reproduction

```js
// When parsing markdown content with nested structures
const markdown = `
Some content here
With multiple lines
`;

const processor = remark();
const result = processor.parse(markdown);

// The content tokens are being processed in the wrong order
// This causes the AST to be malformed
```

### Expected behavior

The tokenizer should complete the callback flow before exiting content chunks. The current behavior is causing the parser to exit states prematurely, which breaks the expected token structure.

### System Info
- remark version: 15.0.1
- Node version: 18.x

This seems like it might be related to the tokenization state machine logic. The order of operations when finishing content parsing doesn't seem right.

---
Repository: /testbed
