# Bug Report

### Describe the bug

I'm encountering an issue with MDX ESM imports/exports parsing. When trying to use ESM syntax in MDX files, the parser seems to be processing the nodes in the wrong order, causing the content to be malformed or not recognized properly.

### Reproduction

```mdx
export const foo = 'bar'

# My Document

Some content here
```

When this MDX is parsed, the ESM export statement is not being handled correctly. The node structure appears to be inverted - it seems like the enter and exit handlers are being called in the wrong sequence, resulting in corrupted AST nodes.

### Expected behavior

The ESM export should be properly parsed and the resulting AST should have the correct structure with `mdxjsEsm` nodes in their proper positions. The enter handler should be called when entering the node, and the exit handler should be called when exiting.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
