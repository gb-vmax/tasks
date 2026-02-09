# Bug Report

### Describe the bug

I'm experiencing a crash when parsing MDX content. The parser seems to be failing with incorrect node positioning information, causing the AST to be malformed.

### Reproduction

```js
const mdxContent = `
# Hello World

Some paragraph text here.

<Component prop="value" />
`;

// Parsing this throws an error or produces incorrect AST
const ast = parseMDX(mdxContent);
```

When trying to parse even simple MDX documents, the parser is producing nodes with swapped or incorrect position data. This causes downstream tools that rely on accurate source locations to fail.

### Expected behavior

The parser should correctly track token positions and produce a valid AST with accurate location information for all nodes. Each node should have proper `start`, `end`, and `loc` properties that correspond to the actual positions in the source text.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
