# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where the parser seems to hang or fail to properly finalize document flow when processing certain markdown structures. The document doesn't get properly closed/flushed, which causes subsequent parsing operations to behave incorrectly.

### Reproduction

```js
const processor = remark();

// Parse a document with nested container structures
const result = processor.processSync(`
# Heading

> Blockquote with content
> Multiple lines

Regular paragraph
`);

// The flow doesn't close properly, causing issues with the parsed output
console.log(result);
```

### Expected behavior

The markdown parser should properly close and flush the document flow, ensuring all container structures are finalized correctly. The parsed AST should reflect the complete and properly terminated document structure.

### System Info
- remark version: 15.0.1
- Node version: Latest

This seems to affect documents with blockquotes and other container elements. The parser appears to not be sending the proper termination signal when closing the flow.

---
Repository: /testbed
