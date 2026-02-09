# Bug Report

### Describe the bug

Inline code blocks with backticks are not being parsed correctly in MDX content. When using single or multiple backticks to create inline code, the text is not being recognized as code and is rendering as plain text instead.

### Reproduction

```mdx
This is `inline code` that should be formatted.

This is ``code with backticks`` inside.

Regular text with `code` mixed in.
```

Expected: The text between backticks should be rendered as inline code.
Actual: The backticks and text are being treated as plain text or not rendering at all.

### Steps to reproduce
1. Create an MDX file with inline code using backticks
2. Process the MDX content
3. Observe that inline code blocks are not being recognized

This seems to have broken recently. Inline code was working fine before but now backtick sequences aren't being tokenized properly.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
