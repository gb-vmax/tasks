# Bug Report

### Describe the bug

I'm encountering an issue with parsing code blocks in MDX files. It seems like lazy continuation lines in code blocks are not being handled correctly. When I have indented code blocks with continuation lines, the parser is making incorrect decisions about whether to treat them as part of the code block or not.

### Reproduction

```mdx
Some text before

    indented code block
    continuation line
    another line

Text after
```

The parser seems to be checking the wrong property when determining if a line is lazy, which causes it to incorrectly accept or reject continuation lines in indented code blocks.

### Expected behavior

Indented code blocks should properly recognize lazy continuation lines and handle them according to the CommonMark spec. The parser should correctly identify when a line is part of a lazy continuation and process it appropriately.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This appears to be related to how the tokenizer checks for lazy lines in the continuation logic. The behavior changed recently and is now causing parsing issues with certain code block patterns.

---
Repository: /testbed
