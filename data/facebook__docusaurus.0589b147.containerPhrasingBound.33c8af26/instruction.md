# Bug Report

### Describe the bug

I'm experiencing an issue with the markdown parser where phrasing content (inline elements like emphasis, links, etc.) inside container nodes is not being processed correctly. The content appears to be parsed but the resulting AST structure is malformed or incomplete.

### Reproduction

```js
const remark = require('remark');

const markdown = `
**bold text** and *italic text*

[link text](https://example.com)
`;

const result = remark().parse(markdown);
console.log(JSON.stringify(result, null, 2));
```

When parsing markdown with inline/phrasing elements, the output AST doesn't match what's expected. The phrasing content seems to be getting lost or not properly attached to the parent container nodes.

### Expected behavior

The parser should correctly process phrasing content and build a proper AST where inline elements (strong, emphasis, links) are properly nested within their container paragraph nodes.

### Additional context

This seems to affect any markdown with inline formatting inside block-level elements. Simple text without formatting works fine, but as soon as you add emphasis, strong, or links, the AST structure becomes incorrect.

---
Repository: /testbed
