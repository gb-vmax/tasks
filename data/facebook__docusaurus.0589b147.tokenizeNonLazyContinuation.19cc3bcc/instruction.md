# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where lazy continuation lines are being handled incorrectly. It seems like the parser is treating lazy lines as non-lazy and vice versa, which breaks the proper parsing of certain markdown constructs.

### Reproduction

When parsing MDX content with constructs that involve lazy continuation (like list items or block quotes), the parser incorrectly determines whether a line should continue the current block or not.

```mdx
> This is a blockquote
that should continue lazily

* List item
  that continues here
```

The parser seems to be inverting the logic for lazy line detection - lines that should be treated as lazy continuations are being rejected, and lines that shouldn't be lazy are being accepted.

### Expected behavior

The parser should correctly identify lazy continuation lines and handle them according to the CommonMark specification. Lazy lines should be properly associated with their parent block, and non-lazy lines should terminate the block as expected.

### Additional context

This appears to affect block-level constructs that support lazy continuation. The issue manifests when the parser evaluates whether a line belongs to an existing block or starts a new one.

---
Repository: /testbed
