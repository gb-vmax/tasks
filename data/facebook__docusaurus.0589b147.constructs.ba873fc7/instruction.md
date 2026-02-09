# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where certain markdown constructs are not being processed correctly. It seems like some syntax extensions are being skipped or applied in the wrong order during parsing.

### Reproduction

When parsing MDX content with multiple syntax extensions, some constructs that should be recognized are being ignored or handled incorrectly. This appears to affect the order in which markdown syntax extensions are applied.

```js
// Example MDX content that fails to parse correctly
const mdxContent = `
# Header

Some content with custom syntax
`

// The parser seems to skip certain extensions or apply them out of order
```

### Expected behavior

All registered syntax extensions should be processed in the correct order, and no constructs should be skipped during parsing. The markdown content should be fully parsed with all applicable syntax extensions.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

This seems to have started happening recently and I'm not sure what changed. Any help would be appreciated!

---
Repository: /testbed
