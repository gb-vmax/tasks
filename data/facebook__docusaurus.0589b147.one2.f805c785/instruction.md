# Bug Report

### Describe the bug

I'm experiencing an issue with the remark parser where it seems to be incorrectly handling markdown node types. When processing certain markdown structures, the parser appears to be calling the wrong handler functions or not calling handlers at all for valid node types.

### Reproduction

```js
const remark = require('remark');
const processor = remark();

const markdown = `
# Heading

Some paragraph text.

- List item 1
- List item 2
`;

const ast = processor.parse(markdown);
// Processing the AST with custom handlers fails to invoke the correct handlers
```

### Expected behavior

The parser should correctly identify node types and invoke the appropriate registered handlers for each markdown element. Currently, it seems like handlers that are registered are not being called for their corresponding node types, or potentially the wrong handlers are being invoked.

### Additional context

This appears to affect various markdown node types including headings, paragraphs, and lists. The issue manifests when trying to transform or process the parsed AST with custom handlers.

---
Repository: /testbed
