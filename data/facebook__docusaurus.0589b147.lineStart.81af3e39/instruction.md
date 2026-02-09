# Bug Report

### Describe the bug

I'm encountering an issue with lazy continuation parsing in MDX code blocks. It seems like the parser is incorrectly handling line continuations when checking for lazy content, causing code blocks to be parsed incorrectly or not at all.

### Reproduction

```mdx
> blockquote
> ```js
> code block
> ```
```

When parsing the above MDX content, the code block inside the blockquote doesn't get recognized properly. The lazy continuation check appears to be off by one line, which causes the parser to make wrong decisions about whether to continue parsing the current construct.

### Expected behavior

Code blocks (and other constructs) inside blockquotes should be parsed correctly. The lazy continuation logic should properly determine when a line is part of a lazy continuation and handle it accordingly.

### Additional context

This affects nested structures where lazy continuations are involved. The issue seems to be related to how the line number is used when checking the lazy parser state.

---
Repository: /testbed
