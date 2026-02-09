# Bug Report

### Describe the bug

I'm encountering an issue with lazy continuation lines in MDX parsing. It seems like the parser is incorrectly determining whether a line should be treated as lazy or not, which is causing some content blocks to be parsed incorrectly.

### Reproduction

```mdx
> Quote block
  with continuation

Some text after
```

When parsing this MDX content, the continuation line behavior is not working as expected. The parser appears to be checking the wrong line number when determining if a line is lazy, which leads to incorrect parsing of multi-line constructs like blockquotes, lists, or other container blocks.

### Expected behavior

The parser should correctly identify lazy continuation lines and handle them appropriately. Continuation lines that should be part of a container block are being incorrectly rejected (or vice versa), breaking the expected markdown structure.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This seems to be related to how the tokenizer checks the lazy line index. The logic for determining whether to continue or exit a container block appears to be inverted or checking the wrong line reference.

---
Repository: /testbed
