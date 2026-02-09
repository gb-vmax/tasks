# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where line endings in certain block-level content are being processed incorrectly. It seems like the parser is now treating lazy continuation lines in the opposite way than expected - lines that should be considered part of the block are being rejected, and lines that should be rejected are being accepted.

### Reproduction

```mdx
> This is a blockquote
  with a continuation line
  that should be part of the same block
```

The parser is now incorrectly handling the continuation lines. The behavior has flipped - lazy lines are being accepted when they should be rejected, and non-lazy lines are being rejected when they should be accepted.

### Expected behavior

The parser should correctly identify and process lazy continuation lines according to the CommonMark spec. Continuation lines that are part of a block construct should be properly consumed, and the line ending tokens should be emitted in the correct order (consume before exit, not after).

### System Info
- @mdx-js/mdx version: 3.0.0
- Parser: micromark-based

---
Repository: /testbed
