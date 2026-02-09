# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where whitespace handling after tag markers appears to be broken. When there's whitespace (spaces or line endings) immediately following a tag marker, the parser seems to handle it incorrectly, leading to parsing failures or unexpected behavior.

### Reproduction

```mdx
< Component />
```

or

```mdx
<
Component />
```

The parser should handle whitespace after the opening `<` tag marker, but it seems to reject valid MDX syntax or process it in an unexpected way.

### Expected behavior

Whitespace after tag markers should be properly handled and the MDX should parse correctly. The parser should continue processing the tag name after consuming any whitespace that follows the opening marker.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
