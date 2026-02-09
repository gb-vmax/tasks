# Bug Report

### Describe the bug

I'm experiencing an issue with source position tracking in MDX parsing. When parsing MDX content, the end positions of AST nodes appear to be incorrect - they're pointing to the start position instead of the actual end position of the node.

This is causing problems when trying to extract source code snippets or generate accurate source maps from the parsed AST.

### Reproduction

```js
import { parse } from 'remark-mdx';

const mdxContent = `
# Hello World

Some text here
`;

const ast = parse(mdxContent);

// Check the position of any node
console.log(ast.children[0].position);
// Expected: end position should be after "Hello World"
// Actual: end position is the same as start position
```

### Expected behavior

AST nodes should have accurate `end` positions that reflect where the node actually ends in the source text. The `position.end` should point to the character after the last character of the node, not to where it starts.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

This seems like it might be a regression since earlier versions tracked positions correctly. Any help would be appreciated!

---
Repository: /testbed
