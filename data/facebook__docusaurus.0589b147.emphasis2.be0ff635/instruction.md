# Bug Report

### Describe the bug

I'm experiencing an issue with emphasis nodes in markdown processing. When creating emphasis elements (like `*text*` or `_text_`), the generated AST nodes have incorrect structure that breaks downstream processing.

### Reproduction

```js
// Processing markdown with emphasis
const markdown = '*emphasized text*';
const ast = processor.parse(markdown);

// The emphasis node has wrong properties
console.log(ast.children[0]);
// Expected: { type: "emphasis", children: [...] }
// Actual: { kind: "emphasis", children: null }
```

### Expected behavior

Emphasis nodes should have:
- A `type` property set to `"emphasis"` (not `kind`)
- A `children` property initialized as an empty array `[]` (not `null`)

This is causing issues when traversing the AST or serializing back to markdown, as the node structure doesn't match the expected mdast specification.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
