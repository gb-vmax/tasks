# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where certain content is not being processed correctly. It seems like the parser is getting stuck or entering an infinite loop when encountering specific character sequences.

### Reproduction

When trying to parse MDX content with certain constructs, the parser hangs indefinitely and never completes. This appears to happen with content that has specific character patterns at break points.

Example content that triggers the issue:
```mdx
Some text with special characters or constructs that should be parsed normally
```

The parser seems to get into an infinite state where it keeps checking the same position without advancing.

### Expected behavior

The MDX content should parse successfully and complete in a reasonable amount of time without hanging.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This is blocking our ability to process certain MDX files. Any help would be appreciated!

---
Repository: /testbed
