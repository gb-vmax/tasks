# Bug Report

### Describe the bug

I'm experiencing an issue with MDX JSX parsing where the exit handler for data tokens is not being called correctly. This appears to cause problems when processing JSX content in MDX files, as the token processing seems incomplete.

### Reproduction

When parsing MDX content with JSX tags that contain data tokens, the parser doesn't properly complete the token processing cycle. 

```mdx
<Component>
  Some text content here
</Component>
```

The data tokens within the JSX tags are entered but not properly exited, which can lead to malformed AST structures or incomplete parsing results.

### Expected behavior

Both enter and exit handlers should be called for data tokens to ensure proper token lifecycle management. The parser should correctly process the entire JSX content and produce a valid AST.

### System Info
- remark-mdx version: 3.0.0

---
Repository: /testbed
