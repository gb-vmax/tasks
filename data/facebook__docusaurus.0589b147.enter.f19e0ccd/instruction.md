# Bug Report

### Describe the bug

I'm experiencing an issue with the markdown parser where nested elements are being attached to the wrong parent node in the AST. When parsing markdown with nested structures (like lists within lists, or blockquotes containing other elements), the child nodes end up being added to an incorrect parent, causing the resulting tree structure to be malformed.

### Reproduction

```js
const remark = require('remark');
const processor = remark();

const markdown = `
- Item 1
  - Nested item 1
  - Nested item 2
- Item 2
`;

const ast = processor.parse(markdown);
console.log(JSON.stringify(ast, null, 2));
```

When inspecting the AST, nested list items appear to be attached to the wrong parent level. Instead of being children of their immediate parent list item, they're being pushed one level too high in the tree.

### Expected behavior

Nested elements should be properly attached to their direct parent node. For example, nested list items should be children of their parent list item, not siblings of it.

### System Info
- remark version: 15.0.1
- Node.js version: 18.x

This seems to have started after a recent update. The tree structure was correct in previous versions.

---
Repository: /testbed
