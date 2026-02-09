# Bug Report

### Describe the bug

I'm experiencing an issue with inline code parsing in MDX where spaces after opening backticks are being consumed incorrectly. When I have inline code that starts with a space (like `` ` foo` ``), the space is not being preserved in the output.

### Reproduction

```markdown
This is some text with ` foo` inline code.
```

When this is parsed, the space after the opening backtick seems to be handled incorrectly, causing unexpected behavior in the tokenization process.

### Expected behavior

The space should be treated as part of the code content and preserved in the output. Inline code like `` ` foo` `` should render with the leading space intact.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
