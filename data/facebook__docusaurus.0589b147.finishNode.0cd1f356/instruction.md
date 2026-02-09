# Bug Report

### Describe the bug

I'm experiencing an issue with AST node position tracking in the MDX parser. When parsing MDX content, the end positions of nodes are being set incorrectly, which causes problems with source mapping and error reporting.

### Reproduction

```js
const mdx = `
# Hello World

Some text here
`;

const result = compile(mdx);
// The AST nodes have incorrect end positions
// They point to the start of the token instead of the end
```

### Expected behavior

When finishing AST nodes, the `end` position should point to the end of the last token (`lastTokEnd`), not the start. This is breaking source maps and making it difficult to accurately report error locations in MDX files.

The positions are being set to where tokens start rather than where they end, which means:
- Error messages point to the wrong location
- Syntax highlighting breaks
- Source maps are inaccurate

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
