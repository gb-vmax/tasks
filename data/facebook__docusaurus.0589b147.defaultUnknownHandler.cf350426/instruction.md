# Bug Report

### Describe the bug

I'm experiencing an issue with node transformation where the position data from the original markdown AST nodes is not being properly transferred to the resulting HTML AST nodes. When processing unknown node types, the position information seems to be lost or not correctly applied.

### Reproduction

```js
const processor = unified()
  .use(remarkParse)
  .use(remarkRehype)
  .use(rehypeStringify);

const markdown = `
Some content with custom nodes
`;

const result = await processor.process(markdown);

// Position data is missing or incorrect on transformed nodes
// Expected the hast nodes to have position info from mdast nodes
```

When transforming markdown nodes that don't have a specific handler, the resulting HTML nodes should retain the position information from the source, but this doesn't seem to be happening consistently.

### Expected behavior

The transformed HTML AST nodes should preserve the position data (line, column, offset) from the original markdown AST nodes. This is important for source maps and error reporting.

### System Info
- remark-rehype version: 11.0.0
- Node.js version: 18.x

---
Repository: /testbed
