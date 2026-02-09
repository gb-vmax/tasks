# Bug Report

### Describe the bug

I'm experiencing an issue with MDX code block parsing where indented code blocks with exactly 4 spaces are not being recognized correctly. The parser seems to be rejecting valid indented code blocks that should be accepted according to the CommonMark spec.

### Reproduction

```markdown
Here's some text.

    This should be an indented code block
    with exactly 4 spaces of indentation
    
More regular text here.
```

When parsing this MDX content, the indented code block (which has exactly 4 spaces) is not being treated as a code block. Instead, it's being processed as regular paragraph text.

### Expected behavior

According to CommonMark, any line indented with 4 or more spaces should be treated as an indented code block. The parser should recognize and properly handle code blocks with exactly 4 spaces of indentation.

### Additional context

This appears to be related to the line prefix checking logic. Code blocks with 5+ spaces work fine, but exactly 4 spaces doesn't trigger the code block behavior anymore.

---
Repository: /testbed
