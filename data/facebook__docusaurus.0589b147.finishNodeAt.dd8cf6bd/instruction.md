# Bug Report

### Describe the bug

I'm experiencing an issue with node position tracking in the MDX parser. When parsing MDX content, the end positions and ranges of AST nodes are being set incorrectly, which causes problems when trying to extract source code snippets or generate accurate source maps.

### Reproduction

```js
const { compile } = require('@mdx-js/mdx');

const mdxContent = `
# Hello World

This is a test paragraph.
`;

const result = await compile(mdxContent, {
  development: false
});

// Check the AST node positions
// The end position matches the start position instead of the actual end
// The range[1] is set to range[0] value instead of the actual end position
```

### Expected behavior

AST nodes should have correct `end` positions that point to where the node actually ends in the source code, not where it starts. Similarly, `range[1]` should contain the end position, not duplicate the start position from `range[0]`.

This breaks any tooling that relies on accurate source positions for:
- Syntax highlighting
- Error reporting
- Code extraction
- Source map generation

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
