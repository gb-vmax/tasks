# Bug Report

### Describe the bug

I'm experiencing an issue with the markdown parser where nested content structures are being built incorrectly. It seems like child nodes are being added in the wrong order or to the wrong parent container.

When parsing markdown with nested elements (like lists within lists, or code blocks within blockquotes), the resulting AST structure has elements appearing in reverse order or attached to unexpected parent nodes.

### Reproduction

```js
const markdown = `
- Item 1
  - Nested item 1
  - Nested item 2
- Item 2
`;

const result = parse(markdown);
// The nested items appear in wrong positions in the tree
// or the fragment type is incorrect
```

### Expected behavior

The parser should build the AST with proper parent-child relationships, maintaining the correct order of sibling nodes. Nested elements should be properly contained within their parent nodes, and the node types should accurately reflect the markdown structure.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
