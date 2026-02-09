# Bug Report

### Describe the bug

I'm experiencing an issue with inline code rendering in MDX content. The parsing seems to be broken - inline code blocks (backticks) are not being recognized correctly and the output is malformed.

### Reproduction

```md
This is a sentence with `inline code` in it.
```

When this MDX content is processed, the inline code is not being parsed properly. The token sequence appears to be incorrect, causing the code text to not render as expected.

### Expected behavior

Inline code blocks should be properly recognized and rendered. The text between backticks should be treated as code and styled accordingly.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This appears to have started happening recently. Not sure if this is related to a recent change in the tokenization logic, but inline code was working fine before.

---
Repository: /testbed
