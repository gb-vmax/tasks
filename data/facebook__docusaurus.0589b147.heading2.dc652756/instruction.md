# Bug Report

### Describe the bug

I'm experiencing an issue with MDX heading rendering. When I try to use headings in my MDX files, they're not being processed correctly and the output structure seems malformed.

### Reproduction

```mdx
# My Heading

Some content here

## Another Heading

More content
```

When this MDX is compiled, the headings don't render properly. The AST structure appears to be incorrect - instead of getting proper heading nodes, I'm getting something else entirely.

### Expected behavior

Headings should be compiled into proper heading nodes with the correct type and structure. The children array should be initialized properly so that heading content can be added.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems like a regression - headings were working fine in previous versions. Any help would be appreciated!

---
Repository: /testbed
